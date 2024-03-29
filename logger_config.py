import logging

def setup_logging():
    # Configure the logging system
    logging.basicConfig(
        filename='app.log', 
        filemode='a', 
        format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
        level=logging.INFO
    )

    # Create a custom logger
    logger = logging.getLogger('WeatherApp')
    return logger
