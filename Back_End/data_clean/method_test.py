import logging
from method import calculator

logging.basicConfig()
logger = logging.getLogger("Calculator function test")
logger.setLevel(logging.DEBUG)

try:
    logger.debug("This is the test of create a calculator object")
    cal = calculator()
    logger.debug('Successfully create calculator object')
except exception as e:
    logger.error(e.message)

try:
    logger.info("This is a basic test for checkUnit function")
    logger.debug("cal.checkUnit('345678lbs','w')")
    result = cal.checkUnit('345678lbs','w')
    logger.debug(result)
    logger.debug("cal.checkUnit('3876597inches','h')")
    result = cal.checkUnit('3876597inches','h')
    logger.debug(result)
    logger.debug("cal.checkUnit('3876597inches','w')")
    result = cal.checkUnit('3876597inches','w')
    logger.debug(result)
    logger.info("This is the end of test for checkUnitFunction")
except exception as e:
    logger.error(e.message)

