import io
import connexion
from typing import Tuple, Dict
import pandas as pd
import csv
from PIL import Image
import base64

from logger_loader import load_logger_config
import logging
import uuid

picture_formats = ['jpeg', 'png', 'jpg']
text_formats = ['txt']

load_logger_config()


def log_msg(level, uid, msg):
    logging.log(level, "[MODEL EXEC] ID={} {}".format(str(uid), msg))


def health() -> Tuple[Dict[str, str], int]:
    return {"health_status": "running"}, 200


def post_file() -> int:
    work_id = uuid.uuid4().hex
    log_msg(logging.INFO, work_id, "Processing request started")

    # read_file
    file = connexion.request.files['file']

    # read filename and extension
    file_name = file.filename
    extension = file_name.split('.')[-1]
    print(file, file_name)

    # read data from file
    if extension in picture_formats:
        img = Image.open(file)

        # PILImage to bytes
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        byte_im = buf.getvalue()

        encoded_string = base64.b64encode(byte_im)
    elif extension in text_formats:
        text = file.read()
        encoded_string = base64.b64encode(text)
    else:
        encoded_string = base64.b64encode(b'Empty!')

    database = pd.read_csv('data_base.csv')
    if any(database['Filename'] == file_name):
        log_msg(logging.ERROR, work_id, "File {} is already exist".format(file_name))
    else:
        with open('data_base.csv', 'a') as csv_file:
            file_writer = csv.writer(csv_file, delimiter=',', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            file_writer.writerow([file_name, extension, encoded_string])
            log_msg(logging.INFO, work_id, "POST file {} to database".format(file_name))

    return 200


def put_file() -> int:
    work_id = uuid.uuid4().hex
    log_msg(logging.INFO, work_id, "Processing request started")

    # read_file
    file = connexion.request.files['file']

    # read filename and extension
    file_name = file.filename
    extension = file_name.split('.')[-1]
    print(file_name, extension)

    # read data from file
    if extension in picture_formats:
        img = Image.open(file)

        # PILImage to bytes
        buf = io.BytesIO()
        img.save(buf, format='PNG')
        byte_im = buf.getvalue()

        encoded_string = base64.b64encode(byte_im)
    elif extension in text_formats:
        text = file.read()
        encoded_string = base64.b64encode(text)
    else:
        encoded_string = base64.b64encode(b'Empty!')

    database = pd.read_csv('data_base.csv')
    if any(database['Filename'] == file_name):
        idx = database.index[database['Filename'] == file_name].tolist()
        database = database.set_value(idx[0], 'base64_data', encoded_string)
        database.to_csv('data_base.csv', index=None, header=True)
        log_msg(logging.INFO, work_id, "PUT file {} at database".format(file_name))
    else:
        log_msg(logging.ERROR, work_id, "File {} don't exist".format(file_name))

    return 200


def get_file(file_name) -> Tuple[Dict[str, str], int]:
    work_id = uuid.uuid4().hex
    log_msg(logging.INFO, work_id, "Processing request started")

    extension = file_name.split('.')[-1]
    print(type(extension))

    database = pd.read_csv('data_base.csv')
    if any(database['Filename'] == file_name):
        idx = database.index[database['Filename'] == file_name].tolist()
        encoded_string = database.at[idx[0], 'base64_data']
        log_msg(logging.INFO, work_id, "GET file {} from database".format(file_name))
    else:
        log_msg(logging.ERROR, work_id, "File {} don't exist".format(file_name))
        encoded_string = base64.b64encode(b'Empty!')

    return {"result": encoded_string}, 200


def delete_file(file_name) -> int:
    work_id = uuid.uuid4().hex
    log_msg(logging.INFO, work_id, "Processing request started")

    database = pd.read_csv('data_base.csv')
    if any(database['Filename'] == file_name):
        idx = database.index[database['Filename'] == file_name].tolist()
        database = database.drop([idx[0]])
        database.to_csv('data_base.csv', index=None, header=True)
        log_msg(logging.INFO, work_id, "DELETE file {} from database".format(file_name))
    else:
        log_msg(logging.ERROR, work_id, "File {} don't exist".format(file_name))

    return 200


def head_file(extensions) -> Tuple[Dict[str, str], int]:

    print(extensions)
    work_id = uuid.uuid4().hex
    log_msg(logging.INFO, work_id, "Processing request started")

    database = pd.read_csv('data_base.csv')
    header = database.at[0, 'Filename']
    print(header)

    return {"result": header}, 200


app = connexion.App(__name__)
app.add_api('swagger.yaml')
application = app.app

if __name__ == "__main__":
    app.run(port=8080)
