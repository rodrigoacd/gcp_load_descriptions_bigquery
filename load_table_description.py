"""
Utility to manage BigQuery table descriptions.
"""

from google.cloud import bigquery

class BigQueryTableDescription:
    """
        Manages table/view descriptions.
    """

    def __init__(self, bq_client):
        """
        Class init.
        :param `google.cloud.bigquery.Client` bq_client: BigQuery client
        """
        self.bq_client = bq_client

    def update_table_descriptions(self, target_full_table_id, table_description):

        table_ref = target_full_table_id
        table = self.bq_client.get_table(table_ref)  

        table.description = table_description
        

        table = self.bq_client.update_table(table, ["description"])  # API request

    #def update_table_descriptions_from_csv(self, csv_path)

