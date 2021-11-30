import requests



def smsapi(numbers, msg):
    # print('-----------------message called')

    full_message = msg
    receivers = numbers
    #multiple numbers '8801880871297880188087129788018808712978801880871297'

    api_key = 'C200107861a48f0156c791.24247576'
    senderid = '8809612440935'
    headers = {}

    payload = {
        'api_key': api_key,
        'type': 'text',
        'contacts': receivers,
        'senderid': senderid,
        'msg': full_message,
    }

    result = requests.post("http://202.164.208.226/smsapi", data=payload, headers=headers)

    return result
