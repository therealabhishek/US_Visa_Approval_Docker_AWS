from us_visa.configuration.mongo_db_connection import MongoDBClient

ins = MongoDBClient()

from us_visa.entity.config_entity import DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig, ModelEvaluationConfig
from us_visa.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact, DataTransformationArtifact, ModelTrainerArtifact, ModelEvaluationArtifact

from us_visa.components.data_ingestion import DataIngestion
from us_visa.components.data_validation import DataValidation
from us_visa.components.data_transformation import DataTransformation
from us_visa.components.model_trainer import ModelTrainer
from us_visa.components.model_evaluation import ModelEvaluation

# data ingestion
di_ins = DataIngestion(DataIngestionConfig)

di_artifact = di_ins.initiate_data_ingestion()

# data validation
dv_ins = DataValidation(data_ingestion_artifact=di_artifact, data_validation_config=DataValidationConfig)

dv_artifact = dv_ins.initiate_data_validation()

# data transformation
dt_ins = DataTransformation(data_ingestion_artifact=di_artifact, data_transformation_config=DataTransformationConfig, data_validation_artifact=dv_artifact)

dt_artifact = dt_ins.initiate_data_transformation()

# model trainer
mt_ins = ModelTrainer(data_transformation_artifact=dt_artifact, model_trainer_config=ModelTrainerConfig)

mt_artifact = mt_ins.initiate_model_trainer()

# model evaluation
me_ins = ModelEvaluation(model_eval_config=ModelEvaluationConfig, data_ingestion_artifact=di_artifact, model_trainer_artifact=mt_artifact)

me_artifact = me_ins.initiate_model_evaluation()