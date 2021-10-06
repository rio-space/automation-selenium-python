import os

# get data directory
data_path = os.getcwd()
os.path.basename(data_path)
data_path = data_path.replace(os.path.basename(data_path), "data")

