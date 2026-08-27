from utils.logger import get_logger


logger = get_logger(__name__)


def test_logger():

    logger.info("Starting logger test")

    logger.info("Opening OrangeHRM")

    logger.info("Logger test completed")

    assert True