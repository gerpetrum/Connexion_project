# script for get requests to web-server
import requests
import argparse
import base64

parser = argparse.ArgumentParser(description='')
parser.add_argument('-f', '--file',
                    type=str,
                    default='./Samples/King.txt',
                    help='file for GET file from DataBase')
opt = parser.parse_args()

name = 'King.txt'
PARAMS = {'file_name': name}
response = requests.get(url='http://127.0.0.1:8080/get_file', params=PARAMS)

picture_formats = ['jpeg', 'png', 'jpg']
text_formats = ['txt']

print(response.status_code)
response_message = response.json()['result']
extension = name.split('.')[-1]
response_message = response_message[2:len(response_message) - 1]
decoded_string = base64.b64decode(response_message.encode('utf-8'))
if extension in picture_formats:
    filename = 'example_picture.' + extension
    with open(filename, 'wb') as f:
        f.write(decoded_string)
else:
    filename = 'example_text.' + extension
    with open(filename, 'wb') as f:
        f.write(decoded_string)
