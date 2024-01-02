from django.views.generic import TemplateView
from django.contrib.staticfiles.finders import find


class UserProfileTemplateView(TemplateView):
    template_name = 'userprofile/profile.html'


class ProfileSettingsTemplateView(TemplateView):
    template_name = 'userprofile/profile_settings.html'