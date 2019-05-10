# encoding=utf-8
import requests

response = requests.get('https://httpbin.org/ip')
# print(type(response.json()))  # <class 'dict'>
# print(type(response.json()['origin']))  # <class 'str'>
# print(response.json())  # {'origin': '123.235.145.237, 123.235.145.237'}
print('Your IP is: {0}'.format(response.json()['origin']))
