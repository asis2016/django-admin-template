from django.views.generic import TemplateView
from django.templatetags.static import static
from django.contrib.staticfiles.finders import find


import json


class DashboardTemplateView(TemplateView):
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        json_file = find('json/dashboardQuickInfo.json')

        with open(json_file, 'r') as file:
            data = json.load(file)

        context['quick_info_data'] = data
        return context
