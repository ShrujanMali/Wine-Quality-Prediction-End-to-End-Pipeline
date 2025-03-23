from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngetionTrainingPipeline
from mlProject.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngetionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<\n\n x=====================x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"

try:
    logger.info(f">>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<")
    data_ingestion = DataValidationTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\nx============x")

except Exception as e:
    logger.exception(e)
    raise e