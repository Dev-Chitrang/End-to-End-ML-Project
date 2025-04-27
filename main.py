from MLProject.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from MLProject.pipeline.stage_02_data_validation import DataValidaionTrainingPipeline
from MLProject.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
from MLProject import logger

if __name__ == '__main__':
    try:
        STAGE_NAME = 'Data Ingestion stage'
        logger.info(f"<<<<<<<<<<<<<< Stage {STAGE_NAME} Started >>>>>>>>>>>>>>>>>")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f"<<<<<<<<<<<<<< Stage {STAGE_NAME} completed >>>>>>>>>>>>>>>>> \n\nx============x")

    except Exception as e:
        logger.exception(e)
        raise e
    
    try:
        STAGE_NAME = 'Data Validation stage'
        obj = DataValidaionTrainingPipeline()
        obj.main()
        logger.info(f"<<<<<<<<<<<<<< Stage {STAGE_NAME} completed >>>>>>>>>>>>>>>>> \n\nx============x")

    except Exception as e:
        logger.exception(e)
        raise e

    try:
        STAGE_NAME = 'Data Transformation stage'
        obj = DataTransformationTrainingPipeline()
        obj.main()
        logger.info(f"<<<<<<<<<<<<<< Stage {STAGE_NAME} completed >>>>>>>>>>>>>>>>> \n\nx============x")

    except Exception as e:
        logger.exception(e)
        raise e