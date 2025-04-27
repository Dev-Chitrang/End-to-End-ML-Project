from MLProject.config.configuration import ConfigurationManager
from MLProject.components.model_evaluation import ModelEvaluation
from MLProject import logger

STAGE_NAME = "Model Evaluation stage"

class ModelEvaluationPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        model_evaluation_config = config.get_model_evaluation_config()
        model_evaluation = ModelEvaluation(config=model_evaluation_config)
        model_evaluation.eval_model()


if __name__ == '__main__':
    try:
        logger.info(f"<<<<<<<<<<<<<< Stage {STAGE_NAME} Started >>>>>>>>>>>>>>>>>")
        obj = ModelEvaluationPipeline()
        obj.main()
        logger.info(f"<<<<<<<<<<<<<< Stage {STAGE_NAME} completed >>>>>>>>>>>>>>>>>")
    except Exception as e:
        logger.exception(e)
        raise e