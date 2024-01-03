from django.views.generic import TemplateView
from django.contrib.staticfiles.finders import find

import json


class FaqTemplateView(TemplateView):
    template_name = 'faq/faq.html'

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
        context['faqs'] = self.get_json_data('faqs.json')
        context['page_title'] = "FAQs"
        context['display'] = "d-none"
        return context
