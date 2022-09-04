import json
import time
from google.cloud import bigquery
from flask import Flask, request, Response, g
import logging
app = Flask(__name__)
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)
@app.route('/process',methods=['GET', 'POST'])
def log():
    raw_req_data = request

    payload = raw_req_data.get_data(as_text=True) or '(empty payload)'
    print('Received task with payload: {}'.format(payload))
    app.logger.info(type(raw_req_data))
    app.logger.info(type(payload))
    app.logger.info('testinger')
    return 'Received task with payload: {}'.format(payload)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True, debug=True)