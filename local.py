from google.cloud import bigquery
from load_table_description import BigQueryTableDescription
import pandas as pd
from google.cloud import storage


bq_client = bigquery.Client()
description_manager = BigQueryTableDescription(bq_client)


def main():
# TOBE: Use cloud functions variables and event when change to cloud function

    fileName="bch-prj-bdta-pocarq-dev-41f1/Descripcion.csv"
    bucketName="stefanini_poc_datacatalog"

    ### Vars from 
    dataList=fileName.split("/")
    project_id=dataList[0]
    fileName=dataList[1]
    logname=fileName.split(".")[0] + ".log"

    ### Create storage objects
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucketName)
    fil = bucket.blob(project_id + "/" + fileName)
    log = bucket.blob(project_id + "/" + logname)
    ### END create storage objects

    ### Reading bucket file
    logdata = f"gs://{ bucketName }/{ project_id }/{ fileName }"
    with fil.open("r") as f:
        df = pd.read_csv(f, delimiter=';',on_bad_lines='skip')
    ### End reading bucket file

    for index, row in df.iterrows():
        target_table = f"{project_id}.{ row['table_bbddname'] }.{row['table_name']}" 
        desc = row['Descripcion']
        logdata += f'\n Cambiando descripcion de tabla: {target_table } '
        try:
            description_manager.update_table_descriptions(target_table, desc)
        except Exception as e:
            logdata += f'\n Error en la carga de la tabla: {target_table } '
            logdata += f'\n Error encontrado: { e } '

    with log.open("w") as f:
        f.write(logdata)
        


main()
