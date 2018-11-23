##	Script for downloading files from Firebase storage:
##	Place script in a Jupyter Notebook, then downloaded files will be placed in the JupyterNotebook directory.

import requests

## Change this url according to the specific file you wish to download:
URL="https://firebasestorage.googleapis.com/v0/b/storageexample-916c1.appspot.com/o/Test%2Fonlinedata.txt?alt=media&token=aaff5a9f-fcbc-48cd-befb-86bfa544c96a"

## Choose a filename for the downloaded file:
filename = "data.txt"

## Make download request:
r = requests.get(URL)
open(filename, 'wb').write(r.content)