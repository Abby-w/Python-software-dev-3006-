import requests
import logging

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)

fileHandle = logging.FileHandler('autompg2.log', 'w')
fileHandle.setLevel(logging.DEBUG)
logger.addHandler(fileHandle)

streamHandle= logging.StreamHandler()
streamHandle.setLevel(logging.INFO)
logger.addHandler(streamHandle)

#logging.getLogger('requests').setLevel(logging.NOTSET)


logging.debug('getting auto-mpg.data.txt')
url='https://autompgdata.azurewebsites.net/api/assignment7data'

r = requests.get(url, allow_redirects = True)

logging.debug(r.status_code)
logging.info(r.text)
with open('auto-mpg.data.txt', 'wb') as output:
    output.write(r.content)
