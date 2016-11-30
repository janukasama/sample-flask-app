import requests
from flask import Flask
from flask import json
from flask import request

app = Flask(__name__)


@app.route('/outlook/test', methods=['GET'])
def outlook_push():
    try:
        if request.data.decode('ascii') == '':
            return (request.args.get('validationtoken'), 200, {'Content-Type': 'plain/text'})
        else:
            payload = request.data.decode('ascii')
            print("Incoming Notification : ", payload)
            response = requests.post('https://7a586aa6.ngrok.io/test', data=json.dumps(payload))
            print(response)
            return 'OK', 200
    except Exception as e:
        print('Error in outlook_push()', e)
        return 'None', 400

if __name__ == "__main__":
    app.run(port=5003)