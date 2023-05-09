from urllib import response
import requests

def sims(data):
    headers = {
        'Content-Type': 'application/json',
        'x-api-key': 'API 키',
    }

    json_data = {
        'utext': data,
        'lang': 'ja',
    }

    response = requests.post('https://wsapi.simsimi.com/190410/talk', headers=headers, json=json_data)
    response = eval(response.text)['atext']
    # print(response.text)

    return str(response)

# print(sims('hello'))
# print(sims('ハロー'))
