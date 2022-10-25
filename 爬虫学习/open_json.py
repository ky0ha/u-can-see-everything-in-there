import json
with open('C:\\Users\\25315\\Desktop\\test_data.json', 'r', encoding='utf-8-sig') as f:
    str = f.read()
    data = json.loads(str)
    print(data)
    # name_age = data['people']
    # print(name_age)
    # target_name = name_age[1]['name']
    # target_age = name_age[1]['age']
    # print(target_name+':'+target_age)
