import os
import tarfile
import urllib3

DOWNLOAD_ROOT =  "https://raw.githubusercontent.com/ageron/handson-ml2/master/"
HOUSING_PATH = os.path.join("datasets", "housing")
HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"

http = urllib3.PoolManager()
chunk_size = 8192

def fetch_data(url=HOUSING_URL, path=HOUSING_PATH):
    os.makedirs(path, exist_ok=True)
    tgz_path = os.path.join(path,'housing.tzg')
    with http.request("GET", url, preload_content = False) as response:
        with open(tgz_path, "wb") as output_file:
            for chunk in response.stream(chunk_size):
                output_file.write(chunk)
    with tarfile.open(tgz_path) as tgz_file:
        tgz_file.extractall(path = path)
    
fetch_data()
    
    