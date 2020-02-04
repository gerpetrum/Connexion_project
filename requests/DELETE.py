# script for DELETE requests to web-server
import requests
import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('-f', '--file',
                    type=str,
                    default='./Samples/All_units.txt',
                    help='file for DELETE file from DataBase')
opt = parser.parse_args()

PARAMS = {'file_name': 'King.txt'}
response = requests.delete(url='http://127.0.0.1:8080/delete_file', params=PARAMS)

print(response.status_code)
