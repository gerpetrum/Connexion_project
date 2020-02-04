# HEAD of all files from DataBase
import requests
import argparse
import base64

parser = argparse.ArgumentParser(description='')
parser.add_argument('-f', '--file',
                    type=str,
                    default='./Samples/All_units.txt',
                    help='HEAD files from DataBase')
opt = parser.parse_args()

PARAMS = {'extensions': 'txt'}
response = requests.head(url='http://127.0.0.1:8080/head_file', params=PARAMS)

print(response.status_code)
print(response.content)
