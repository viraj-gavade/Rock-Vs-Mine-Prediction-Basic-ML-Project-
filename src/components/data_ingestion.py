from src.exception_handler import CustomException
from src.logger import logging
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
import os 
import sys

from src.components.data_trainsformation import DataTransformation
import pandas as pd 


@dataclass
class DataIngestionConfig : 
    train_data_path : str = os.path.join('artifacts', 'train.csv')
    test_data_path : str = os.path.join('artifacts', 'test.csv')
    raw_data_path : str = os.path.join('artifacts', 'raw.csv')

class DataIngestion:
    def __init__(self):
        self.data_ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        try : 
            logging.info('Initiating the data ingestion pipeline')
            logging.info('Reading data from the data sources ')

            df = pd.read_csv('notebooks\data.csv')
            logging.info('Data read successfully from the source ')

            logging.info(' Creating the directories fro the saving of data ')
            os.makedirs(os.path.dirname(self.data_ingestion_config.train_data_path),exist_ok=True)
            logging.info('Directories created successfully!')

            logging.info('Saving the raw data file ')
            df.to_csv(self.data_ingestion_config.raw_data_path,index=False,header=True)
            logging.info('Raw data saved successfully !')

            logging.info('Applying the train test split')
            train_set , test_set = train_test_split(df,test_size=0.2,random_state=42)
            logging.info('Train test split applied successfully ')


            logging.info('Saving the train and test data')
            train_set.to_csv(self.data_ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.data_ingestion_config.test_data_path,index=False,header=True)
            logging.info('Train and Test data saved successfully!')

            logging.info('Data Ingestion Pipeline excuted successfully!')

            return (
                self.data_ingestion_config.train_data_path,
                self.data_ingestion_config.test_data_path
            )
        except Exception as e :
            logging.info('Error Occured : ' ,e)
            raise CustomException(e,sys)
        


if __name__=="__main__":
    ingestion_object = DataIngestion()
    train_set , test_set = ingestion_object.initiate_data_ingestion()
    transformation_object = DataTransformation()
    transformation_object.initiate_data_transformation(train_set,test_set)

