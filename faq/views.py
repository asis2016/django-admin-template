from django.views.generic import TemplateView
from django.contrib.staticfiles.finders import find


class FaqTemplateView(TemplateView):
    template_name = 'faq/faq.html'