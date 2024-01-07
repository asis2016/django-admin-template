from django.contrib.staticfiles.finders import find
import json


def get_json_data(json_file):
    '''Return json_data util. '''
    json_file_path = find('json/' + json_file)

    with open(json_file_path, 'r') as file:
        data = json.load(file)
    return data
