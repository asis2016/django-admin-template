from django.views.generic import TemplateView
from django.contrib.staticfiles.finders import find


class SysLogTemplateView(TemplateView):
    template_name = 'syslogs/logs.html'
