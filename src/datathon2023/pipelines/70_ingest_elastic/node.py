import os

import polars as pl
from elasticsearch import Elasticsearch, helpers
from tqdm import tqdm


def _gendata(df: pl.DataFrame):
    columns = df.columns
    for row in df.to_dicts():
        lat = row['lat']
        lon = row['lon']
        row['location'] = {'lat': float(lat), 'lon': float(lon)}
        yield row


def upload_data_to_elastic(df, mapping, index, cloud_id=os.environ['cloud_id'], api_key=os.environ['apikey_key']):
    # api_key=(apikey_id,apikey_key)

    es = Elasticsearch(cloud_id=cloud_id, api_key=api_key)
    # check the index existe and if exist remove it
    if es.indices.exists(index=index):
        es.indices.delete(index=index)
    es.indices.create(index=index, body={'settings': {'number_of_shards': 1}, 'mappings': mapping}, ignore=400)
    number_of_docs = df.shape[0]
    progress = tqdm(total=number_of_docs, desc='Uploading data to elastic')
    for ok, action in helpers.streaming_bulk(client=es, index=index, actions=_gendata(df)):
        if not ok:
            print(action)
        progress.update(1)
