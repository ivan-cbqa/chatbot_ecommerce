import json
import requests
import random
from flask import Flask, request, make_response, jsonify
from responses import PRECIO_PARTE
from config import (LOGON_ID, LOGON_PASSWORD,BASIC_AUTH)

app = Flask(__name__)
log = app.logger

auth = None

@app.route('/', methods=['POST'])
def webhook():
    """This method handles the http requests for the Dialogflow webhook
    """
    req = request.get_json(silent=True, force=True)
    try:
        action = req.get('queryResult').get('action')
    except AttributeError:
        return 'json error'

    parameters = req['queryResult']['parameters']

    print('Dialogflow Parameters:')
    print(json.dumps(parameters, indent=4))

        
    if action == 'info_parte':
        res = get_part_info(parameters['any'])
    elif action == 'precio_parte':
        res = get_part_price(parameters['any'])
    else:
        log.error('Unexpected action.')

    print('Action: ' + action)
    print(res)

    return make_response(jsonify(res))

def get_part_price(part_number):
    response = part_request(part_number)

    precio = response['PriceINMXN']
    nombre = response['shortDescription']

    output_string = random.choice(PRECIO_PARTE)

    text = output_string.format(nombre = nombre, precio = precio)

    res = {"fulfillmentText": text,
            "fulfillmentMessages": [
            {
                "text": {
                  "text": [text]
                },
                "platform": "SLACK"
              },
            {"text": {
                    "text": [text]
                    }
            }
      ]
      }

    return res


def get_part_info(part_number):
    response = part_request(part_number)

    precio = response['PriceINMXN']
    nombre = response['shortDescription']

    output_string = random.choice(PRECIO_PARTE)

    text = output_string.format(nombre = nombre, precio = precio)

    res = {"fulfillmentText": text,
            "fulfillmentMessages": [
            {
                "text": {
                  "text": [text]
                },
                "platform": "SLACK"
              },
            {"text": {
                    "text": [text]
                    }
            }
      ]
      }

    return res


def part_request(part_number):
    global auth
    if auth is None:
        auth = authenticate()

    url = "https://esb.boschenlinea.com/api/productview/{}".format(part_number)
    payload = auth
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Basic {}".format(BASIC_AUTH),
        'cache-control': "no-cache"
        }

    response = requests.request("GET", url, json=payload, headers=headers)

    auth = None
    return json.loads(response.content)

    


def authenticate():

    url = "https://esb.boschenlinea.com/api/login"
    payload = {"logonId": LOGON_ID,
                "logonPassword": LOGON_PASSWORD}
    headers = {
        'Content-Type': "application/json",
        'Authorization': "Basic {}".format(BASIC_AUTH),
        'cache-control': "no-cache"
        }

    response = requests.request("POST", url, json=payload, headers=headers)

    return json.loads(response.content)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')


