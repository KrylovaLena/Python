import json


a = {
    "name": "test name",
    "age": 50,
}


b = json.dumps(a)
b += "1"
c = json.loads(b)

x = 1
