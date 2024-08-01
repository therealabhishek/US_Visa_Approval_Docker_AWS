from us_visa.configuration.mongo_db_connection import MongoDBClient

ins = MongoDBClient()

from us_visa.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig
from us_visa.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact, DataTransformationArtifact

from us_visa.components.data_ingestion import DataIngestion
from us_visa.components.data_validation import DataValidation
from us_visa.components.data_transformation import DataTransformation


di_ins = DataIngestion(DataIngestionConfig)

di_artifact = di_ins.initiate_data_ingestion()

dv_ins = DataValidation(data_ingestion_artifact=di_artifact, data_validation_config=DataValidationConfig)

dv_artifact = dv_ins.initiate_data_validation()

dt_ins = DataTransformation(data_ingestion_artifact=di_artifact, data_transformation_config=DataTransformationConfig, data_validation_artifact=dv_artifact)

dt_artifact = dt_ins.initiate_data_transformation()