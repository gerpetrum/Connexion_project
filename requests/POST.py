# script for post requests to web-server
import requests
import argparse

parser = argparse.ArgumentParser(description='')
parser.add_argument('-f', '--file',
                    type=str,
                    default='../Samples/All_units.txt',
                    help='file for POST to DataBase')
opt = parser.parse_args()

files = {'file': open(opt.file, 'rb')}
print(type(open(opt.file, 'rb')))
response = requests.post(url='http://127.0.0.1:8080/post_file', files=files)

print(response.status_code)
