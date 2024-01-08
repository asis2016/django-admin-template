from django.contrib.staticfiles.finders import find
import json


def get_json_data(json_file):
    '''Return json_data'''
    json_file_path = find('json/' + json_file)

    with open(json_file_path, 'r') as file:
        data = json.load(file)
    return data


def global_context(request):
    '''
    Global context for `modal-applications.html`
    '''
    return {
        'modal_applications': get_json_data('modalApplications.json')
    }

