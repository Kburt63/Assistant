from wsgiref import headers
from arrow import get
from openai import OpenAI
client = OpenAI()
input = {
  "folder_id": "folder-id"
}
client.files.list(folder_id="folder-id")
get("https://api.openai.com/v1/files?folder_id=folder-id", headers)
#
#
# Path: List%20Files.py
from arrow import get
from openai import OpenAI
client = OpenAI()
input = {
    "folder_id": "folder-id"
}
### List Files in a Folder
client.files.list(folder_id="folder-id")
get("https://api.openai.com/v1/files?folder_id=folder-id", headers)
#
#
# Path: List%20Files.py
from arrow import get
from openai import OpenAI
client = OpenAI()
input = {
    "folder_id": "folder-id"
}
folder_id = "folder-id"
### List Files in a Folder
client.files.list(folder_id="folder-id")
get("https://api.openai.com/v1/files?folder_id=folder-id", headers)

