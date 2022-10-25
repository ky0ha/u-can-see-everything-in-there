import json
dict_content = {"name":"Jack"}
with open('test.json', 'w') as f:
    json.dump(dict_content, f)