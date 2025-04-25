from MLProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline, STAGE_NAME
from MLProject import logger

if __name__ == '__main__':
    try:
        logger.info(f"<<<<<<<<<<<<<< Stage {STAGE_NAME} Started >>>>>>>>>>>>>>>>>")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"<<<<<<<<<<<<<< Stage {STAGE_NAME} completed >>>>>>>>>>>>>>>>>")
    except Exception as e:
        logger.exception(e)
        raise e