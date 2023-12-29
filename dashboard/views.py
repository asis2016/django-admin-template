from django.views.generic import TemplateView
from django.templatetags.static import static
from django.contrib.staticfiles.finders import find


import json


class DashboardTemplateView(TemplateView):
    template_name = 'dashboard/dashboard.html'

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
        context['quick_info_data'] = self.get_json_data('dashboardQuickInfo.json')
        context['order_status'] = self.get_json_data('dashboardOrderStatus.json')
        context['vistors_browser'] = self.get_json_data('visitorsBrowser.json')
        return context
