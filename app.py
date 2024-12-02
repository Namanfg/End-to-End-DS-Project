from src.endtoendproject.logger import logging
from src.endtoendproject.exception import CustomException
from src.endtoendproject.components.data_ingestion import DataIngestion
from src.endtoendproject.components.data_ingestion import DataIngestionConfig
from src.endtoendproject.components.data_transformation import DataTransformationConfig
from src.endtoendproject.components.data_transformation import DataTransformation
import sys



if __name__=="__main__":
    logging.info("The execution has started.")
    try:   
        # data_ingestion_config = DataIngestionConfig()
        data_ingestion = DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

        # data_transformation_config=data_transformation_config()
        data_transformation = DataTransformation()
        data_transformation.initiate_data_transformation(train_data_path,test_data_path)
        
    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
