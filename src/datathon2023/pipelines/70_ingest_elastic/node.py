
import os
import uuid

import polars as pl
from elasticsearch import Elasticsearch, helpers


def _gendata(df:pl.DataFrame,index,doc_type):

    for row in df.iter_rows():
        yield {
            "_index": index,
            "_type": doc_type,
            "_id": uuid.uuid4(),
            "_source": row.to_dict()
        }
    return



def upload_data(df,cloud_id=os.environ['cloud_id'],apikey_id=os.environ['apikey_id'],apikey_key=os.environ['apikey_key']):

    api_key=(apikey_id,apikey_key)
    es=Elasticsearch(cloud_id=cloud_id,api_key=api_key)
    response=helpers.bulk(es,_gendata(df,'datathon2023','test'))
    print(response)
    return
