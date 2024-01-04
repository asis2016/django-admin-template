from django.views.generic import TemplateView
from django.contrib.staticfiles.finders import find
from .context_processors import get_json_data

import json


class BlankPageTemplateView(TemplateView):
    template_name= 'blank_page.html'
    extra_context = {'page_title': 'Blank Page'}


class DashboardTemplateView(TemplateView):
    extra_context = {'page_title': 'Dashboard'}
    template_name = 'dashboard/dashboard.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['internal_projects'] = get_json_data('dashboardInternalProjects.json')
        context['order_status'] = get_json_data('dashboardOrderStatus.json')
        context['quick_info_data'] = get_json_data('dashboardQuickInfo.json')
        context['product_purchase_sales'] = get_json_data('productsPurchaseAndSales.json')
        context['recently_added_products'] = get_json_data('dashboardRecentlyAddedProducts.json')
        context['vistors_browser'] = get_json_data('visitorsBrowser.json')
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
    extra_context = {
        'page_title': 'My mail'
    }

    template_name= 'mail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['mails'] = get_json_data('mail.json')
        return context


class RegisterTemplateView(TemplateView):
    template_name= 'register.html'


class SinglePageTemplateView(TemplateView):
    extra_context = {
        'page_title': 'Single Page',
        'display': 'd-none'
    }
    template_name= 'single_page.html'


class SearchResultTemplateView(TemplateView):
    extra_context = {
        'page_title': 'Search results',
        'display': 'd-none'
    }

    template_name= 'search-results.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['results'] = get_json_data('searchResults.json')
        return context
