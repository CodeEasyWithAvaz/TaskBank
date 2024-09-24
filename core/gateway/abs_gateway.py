import requests

abs_url = 'http://127.0.0.1:9093/1.0.0/transaction'


def post(data):

    payload = {
        "documents": [{
            "type": "106",
            "externalId": data['externalId'],
            "sender": {
                "account": data['sender']['account'],
                "codeFilial": "01186",
                "tax": "203556638",
                "name": "Terminal active beznal Mirobod sum"
            },
            "receiver": {
                "codeFilial": "01186",
                "account": data['receiver']['account'],
                "tax": "2035000000",
                "name": "Unired p2p"
            },
            "purpose": {
                "code": "61061",
                "name": "Plastik kartadan yechish ECOM/AFT"
            },
            "amount": data['amount'],
        }]
    }

    response = requests.post(abs_url, json=payload)
    response.raise_for_status()
    return response.json()
