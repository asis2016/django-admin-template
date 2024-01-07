from django.views.generic import TemplateView
from utils import get_json_data


class UserProfileTemplateView(TemplateView):
    extra_context = {'page_title': 'My Profile'}
    template_name = 'userprofile/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['profile'] = get_json_data('employee.json')
        return context


class ProfileSettingsTemplateView(TemplateView):
    template_name = 'userprofile/profile_settings.html'