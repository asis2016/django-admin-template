from django.views.generic import TemplateView
from django.templatetags.static import static
from django.contrib.staticfiles.finders import find


import json


class BlankPageTemplateView(TemplateView):
    template_name= 'blank_page.html'
    extra_context = {'page_title': 'Blank Page'}


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
        context['internal_projects'] = self.get_json_data('dashboardInternalProjects.json')
        context['modal_applications'] = self.get_json_data('modalApplications.json')
        context['order_status'] = self.get_json_data('dashboardOrderStatus.json')
        context['quick_info_data'] = self.get_json_data('dashboardQuickInfo.json')
        context['recently_added_products'] = self.get_json_data('dashboardRecentlyAddedProducts.json')
        context['vistors_browser'] = self.get_json_data('visitorsBrowser.json')
        return context


class DocumentationTemplateView(TemplateView):
    extra_context = {'page_title': 'Documentation'}
    template_name= 'documentation.html'


class FourZeroFourTemplateView(TemplateView):
    extra_context = {
        'page_title': '404',
        'display': 'd-none'
    }
    template_name= '404.html'


class LoginTemplateView(TemplateView):
    template_name= 'login.html'


class MailTemplateView(TemplateView):
    template_name= 'mail.html'


class RegisterTemplateView(TemplateView):
    template_name= 'register.html'

class SinglePageTemplateView(TemplateView):
    template_name= 'single_page.html'
