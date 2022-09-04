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
    app.logger.info('json_loads: {}'.format(json.loads(payload)))
    app.logger.info('dict: {}'.format(dict(payload)))
    return 'Received task with payload: {}'.format(payload)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, threaded=True, debug=False)

    # # -------------------------------------------BQ---------------------------------------
    # Create list for convert it in json and poot to BQ
    #     rows_to_insert = []
    #     rows_to_insert.append({
    #         'data': json.dumps(raw_req_data),
    #         'request_id': raw_req_data.get('request_id'),
    #         'ad_timestamp': int(time.time_ns() / 1000)
    #     })

    # GOOGLE_APPLICATION_CREDENTIALS = 'streaming-bq-e8b723d246f1.json'
    # bigquery_client = bigquery.Client.from_service_account_json(GOOGLE_APPLICATION_CREDENTIALS)
    # dataset_id = bigquery_client.dataset('cloudRun')
    # table_id = dataset_id.table('cloud_run')
    # errors = bigquery_client.insert_rows_json(table_id, rows_to_insert)  # Make an API request.
    # if errors == []:
    #     print("New rows have been added.")
    # else:
    #     print("Encountered errors while inserting rows: {}".format(errors))
    # ------------------------------------------------------------------------------------
