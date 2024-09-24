import requests

csi_url = 'http://127.0.0.1:40080/camws/creditTrans'


def post(data):
    payload = {
            "requestData": {
                "callingSystem": "0588",
                "extReqId": data['extReqId'],
                "idType": "PAN",
                "idData": data['idData'],
                "paramsList": None
            },
            "terminalId": "W0000000",
            "curAmount": {
                "currency": data['currency'],
                "amount": data['amount'],
            }
    }
    response = requests.post(csi_url, json=payload)
    response.raise_for_status()
    return response.json()

