from us_visa.configuration.mongo_db_connection import MongoDBClient

ins = MongoDBClient()

from us_visa.entity.config_entity import DataIngestionConfig, DataValidationConfig
from us_visa.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact

from us_visa.components.data_ingestion import DataIngestion
from us_visa.components.data_validation import DataValidation

di_ins = DataIngestion(DataIngestionConfig)

di_artifact = di_ins.initiate_data_ingestion()

dv_ins = DataValidation(data_ingestion_artifact=di_artifact, data_validation_config=DataValidationConfig)

dv_artifact = dv_ins.initiate_data_validation()