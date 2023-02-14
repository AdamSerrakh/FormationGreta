from fulllog import Full_log
import logging
Full_log('Façade')#instancie le logger par la classe "Façade"
logging.info('Start')
for i in range (10):
    logging.debug('Looping...')
logging.info('Stop')
