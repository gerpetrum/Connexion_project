import pandas as pd

first = {'Filename': ['first_file.jpeg'], 'extension': ['jpeg'], 'base64_data': ['info']}

data = pd.DataFrame(first, columns=['Filename', 'extension', 'base64_data'])

data.to_csv('data_base.csv', index=None, header=True)
