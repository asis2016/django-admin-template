from django.views.generic import TemplateView
from django.contrib.staticfiles.finders import find

import json

class SalesListTemplateView(TemplateView):
    extra_context = {'page_title': 'Sales Report'}
    template_name = 'sales/index.html'

    def get_json_data(self, json_file):
        '''
        Return json_data
        '''
        json_file_path = find('json/' + json_file)

        with open(json_file_path, 'r') as file:
            data = json.load(file)

        return data

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sales_report'] = self.get_json_data('sales.json')
        return context
