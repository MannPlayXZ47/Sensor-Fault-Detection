import os
import sys
import numpy as np
import pandas as pd
from pymongo import MongoClient
from zipfile import Path
from src.constants import *
from src.utils.main_utils import MainUtils
from src.exception import CustomException
from src.logger import logging
from dataclasses import dataclass

@dataclass
class DataIngestionConfig:
    artifact_folder:str = os.path.join(artifact_folder)

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config=DataIngestionConfig()
        self.utils = MainUtils()

    def export_collection_as_dataframe(self,collection_name,db_name):
        try:
            client = MongoClient(MONGO_DB_URL)
            collection = mongo_client[db_name][collection_name]
            df = pd.DataFrame(list(collection.find))

            if "_id" in df.collumns.to_list():
                df.drop(columns=["_id"],inplace=True, axis=1)
                df.replace({"na:":np.nan},inplace=True)
                return df
        except Exception as e:
            raise CustomException(e,sys)
    
    def export_data_into_feature_store_file_path(self) -> pd.Dataframe:
        try:
            logging.info(f"Exporting Data From MongoDB")
            raw_file_path=self.data_ingestion_config.artifact_folder
            os.makedirs(raw_file_path,exist_ok=True)

            sensor_data = self.export_collection_as_dataframe(
                collection_name=MONGO_COLLECTION_NAME
                db_name= MONGO_DATABASE_NAME
            )

            logging.info(f"saving exported data into feature store file path : {raw_file_path}")

            feature_store_file_path= os.path.join(raw_file_path, 'sensor_fault.csv')

            sensor_data.to_csv(feature_store_file_path,index = False)
            return feature_store_file_path
        
        except Exception as e:
            raise CustomException(e,sys)
        
    def initiate_data_ingestion(self) -> Path:
        logging.info("Entered initiate_data_ingestion method of data_ingestion class")

        try:
            feature_store_file_path = self.export_data_into_feature_store_file_path()
            logging.info(f"got the data from mongodb")
            logging.info("exited initiate_data_ingestion method of data_ingestion class")
            return feature_store_file_path
        except Exception as e:
            raise CustomException(e,sys)