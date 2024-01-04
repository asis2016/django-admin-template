from django.views.generic import TemplateView
from django.contrib.staticfiles.finders import find

import json


class ProductChartTemplateView(TemplateView):
    template_name = 'products/charts.html'


class ProductCreateFormTemplateView(TemplateView):
    template_name = 'products/create.html'


class ProductEditFormTemplateView(TemplateView):
    template_name = 'products/.html'


class ProductListTemplateView(TemplateView):
    extra_context = {'page_title': 'Products'}
    template_name = 'products/list.html'

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
        context['products'] = self.get_json_data('products.json')
        return context
