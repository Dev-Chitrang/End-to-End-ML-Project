from MLProject.config.configuration import ConfigurationManager
from MLProject.components.model_trainer import ModelTrainer
from MLProject import logger

STAGE_NAME = "Model Training stage"

class ModelTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_training_config = config.get_model_trainer_config()
        model_trainer = ModelTrainer(config=model_training_config)
        model_trainer.train()


if __name__ == '__main__':
    try:
        logger.info(f"<<<<<<<<<<<<<< Stage {STAGE_NAME} Started >>>>>>>>>>>>>>>>>")
        obj = ModelTrainingPipeline()
        obj.main()
        logger.info(f"<<<<<<<<<<<<<< Stage {STAGE_NAME} completed >>>>>>>>>>>>>>>>>")
    except Exception as e:
        logger.exception(e)
        raise e