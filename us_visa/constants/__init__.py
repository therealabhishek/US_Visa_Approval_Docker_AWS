DATABASE_NAME = "US_VISA_DB"

COLLECTION_NAME = "visa_data"

MONGODB_URL_KEY = "MONGO_DB_URL"

PIPELINE_NAME: str = "usvisa"
ARTIFACT_DIR: str = "artifact"

FILE_NAME: str = "usvisa.csv"
TRAIN_FILE_NAME: str = "train.csv"
TEST_FILE_NAME: str = "test.csv"

"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""
DATA_INGESTION_COLLECTION_NAME: str = "visa_data"
DATA_INGESTION_DIR_NAME: str = "data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR: str = "feature_store"
DATA_INGESTION_INGESTED_DIR: str = "ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO: float = 0.2