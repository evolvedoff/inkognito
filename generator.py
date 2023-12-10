import requests
import subprocess
from requests.structures import CaseInsensitiveDict
import json
from win10toast import ToastNotifier

token = "" # PLACE THE TOKEN IN THE STRING
previousemailPath = "" # PUT THE FULL PATH OF THE TXT FILE NAMED "previousemail.txt"

url = "https://quack.duckduckgo.com/api/email/addresses"

headers = CaseInsensitiveDict()
headers["Authorization"] = f"Bearer {token}"
headers["Content-Type"] = "application/json"
headers["Content-Length"] = "0"

resp = requests.post(url, headers=headers)

json_bytes = resp.content
json_str = json_bytes.decode('utf-8')
data = json.loads(json_str)

address_value = data.get("address")

with open(previousemailPath, "w") as text_file:
    text_file.write(f"{address_value}@duck.com")

text = f"The email that was generated is: {address_value}@duck.com"

toaster = ToastNotifier()

toaster.show_toast("Email Alias Service", text, icon_path=None, duration=0)
