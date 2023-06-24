import logging
logging.basicConfig(filename = "weatherapp.log", level = logging.DEBUG, format = "%(asctime)s %(levelname)s %(message)s", filemode = "w")
logger = logging.getLogger()


def logData(cityName, data):
    logger.info("Weather Forecast App started")
    logger.info("City Name: " + cityName)
    logger.info("City Data: " + str(data))
    logger.info("Weather Forecast App Ended")