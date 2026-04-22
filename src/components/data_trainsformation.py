import sys 
import os 
from dataclasses import dataclass
import pandas as pd 
import numpy as np
from  src.logger import logging
from src.exception_handler import CustomException

@dataclass
class DataTransformationConfig :
    preprocessor_path : str = os.path.join('artifacts','preprocessor.pkl')



class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()


    def get_preprocessor_object(self):
        pass


    def initiate_data_transformation(self , train_path , test_path ):
        try : 
            logging.info('Intiating the data transformation pipeline')
            logging.info('Reading the train and test data from the given path')
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)
            logging.info('Train and Test data read successfully')
            

        
            logging.info('Seperating the input features for the train and test dataset')
            input_feature_train_df = train_df.iloc[:, :60]
            input_feature_test_df = test_df.iloc[:, :60]
            logging.info('seperation of the input features on train and test data completed')

            logging.info('Seperating the target features for the train and test dataset')
            targt_feature_train_df = train_df.iloc[:, 60]
            target_feature_test_df = test_df.iloc[:, 60]
            logging.info('seperation of the target features on train and test data completed')


            logging.info('Coverting into trainable arrays')
            train_arr = np.c_[
                input_feature_train_df,np.array(targt_feature_train_df)
            ]

            test_arr = np.c_[
                input_feature_test_df,np.array(target_feature_test_df)
            ]
            logging.info('Coversion completed!')
            return (
                train_arr,
                test_arr
            )
        
        except Exception as e :
            raise CustomException(e,sys) 
            print(e)


