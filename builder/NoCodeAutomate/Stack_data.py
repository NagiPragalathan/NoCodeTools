import json


def json_to_dect(jsondata):
    output_dict = {}
    for i in jsondata:
        output_dict[i] = jsondata[i]
    return output_dict
    
def get_more(dic_data):
    stack = []
    for i in dic_data.keys():
        if isinstance(dic_data.get(i),dict):
            stack.extend(get_more(dic_data.get(i)))
        else:
            if dic_data not in stack:
                stack.append(dic_data)
    return stack

def get_stack(path):
    with open(path,'r') as data :
        read_data = data.read()
        data.close()
    dict_data = json_to_dect(json.loads(read_data))
    return get_more(dict_data)