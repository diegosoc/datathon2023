
import os
import uuid

import polars as pl
from elasticsearch import Elasticsearch, helpers
from tqdm import tqdm


def _gendata(df:pl.DataFrame):

    for row in df.iter_rows():
        yield {
            "_id": uuid.uuid4(),
            "_source": row
        }




def upload_data_to_elastic(df,mapping,cloud_id=os.environ['cloud_id'],api_key=os.environ['apikey_key']):

    # api_key=(apikey_id,apikey_key)

    es=Elasticsearch(cloud_id=cloud_id,api_key=api_key)
    #check the index existe and if exist remove it
    if es.indices.exists(index='datathon2023'):
        es.indices.delete(index='datathon2023')
    es.indices.create(index='datathon2023',body={
        "settings": {'number_of_shards': 1},
        "mappings":          mapping

    })
    number_of_docs=df.shape[0]
    progress=tqdm(total=number_of_docs,desc='Uploading data to elastic')
    for ok,action in helpers.streaming_bulk(client=es,index='datathon2023',actions=_gendata(df):
        if not ok:
            print(action)
        progress.update(1)
    return
