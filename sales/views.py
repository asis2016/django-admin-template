from django.views.generic import TemplateView
from django.contrib.staticfiles.finders import find
from utils import get_json_data

import json

class SalesListTemplateView(TemplateView):
    extra_context = {'page_title': 'Sales Report'}
    template_name = 'sales/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sales_report'] = get_json_data('sales.json')
        return context
