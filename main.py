from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngetionTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngetionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<\n\n x=====================x")
except Exception as e:
    logger.exception(e)
    raise e