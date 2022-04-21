import requests

# import requests



# def smsapi(numbers, msg):
#     # print('-----------------message called')

#     full_message = msg
#     receivers = numbers
#     #multiple numbers '8801880871297880188087129788018808712978801880871297'

#     api_key = 'C200107861a48f0156c791.24247576'
#     senderid = '8809612440935'
#     headers = {}

#     payload = {
#         'api_key': api_key,
#         'type': 'text',
#         'contacts': receivers,
#         'senderid': senderid,
#         'msg': full_message,
#     }

#     result = requests.post("http://202.164.208.226/smsapi", data=payload, headers=headers)

#     return result


def smsapi(msg,receiver):
    api_key = 'd2ccfbcf828e8f05'
    secretkey ='c728e1ff'
    callerID ='8809612440935'
    messageContent= msg
    numbers = receiver

    result = requests.post(f"https://smpp.ajuratech.com:7790/sendtext?apikey={api_key}&secretkey={secretkey}&callerID={callerID}&toUser={numbers}&messageContent={messageContent}")
    # cpannel url is here -----------------
     #  http://217.172.190.215/sendtext?apikey=API_KEY&secretkey=SECRET_KEY&callerID=SENDER_ID&toUser=MOBILE_NUMBER&messageContent=MESSAGE
    return result



# result = requests.post(f"https://smpp.ajuratech.com:7790/sendtext?apikey={apikey}&secretkey={secretkey}&callerID={senderid}&toUser={toUser}&messageContent={messageContent}")
#  a = requests.post("https://smpp.ajuratech.com:7790/sendtext?apikey=d2ccfbcf828e8f05&secretkey=c728e1ff&callerID=35&toUser=8801880871297&messageContent=Thisisaltaf")