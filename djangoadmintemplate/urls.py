from django.contrib import admin
from django.urls import path
from dashboard.views import (
    BlankPageTemplateView, DashboardTemplateView, DocumentationTemplateView, FourZeroFourTemplateView, 
    LoginTemplateView, MailTemplateView, RegisterTemplateView, SinglePageTemplateView, SearchResultTemplateView
)
#products
from faq.views import FaqTemplateView
from products.views import (
    ProductChartTemplateView,
    ProductListTemplateView,
)
#sales
from sales.views import (
    SalesListTemplateView
)
from syslogs.views import SysLogTemplateView
from userprofile.views import UserProfileTemplateView, ProfileSettingsTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    #faq
    path('faq/', FaqTemplateView.as_view(), name='faq'),

    #products
    path('products/', ProductListTemplateView.as_view(), name='products'),
    path('products/charts/', ProductChartTemplateView.as_view(), name='charts'),
    
    #sales
    path('sales/', SalesListTemplateView.as_view(), name='sales'),


    #from dashboard.views
    #accounts
    path('accounts/login/', LoginTemplateView.as_view(), name='login'),
    path('accounts/registration/', RegisterTemplateView.as_view(), name='registration'),
    #path('accounts/password-reset/', RegisterTemplateView.as_view(), name='password_reset'),

    path('404/', FourZeroFourTemplateView.as_view(), name='404'),
    path('blank-page/', BlankPageTemplateView.as_view(), name='blank_page'),
    path('documentation/', DocumentationTemplateView.as_view(), name='documentation'),
    path('mail/', MailTemplateView.as_view(), name='mail'),
    path('single-page/', SinglePageTemplateView.as_view(), name='single-page'),
    path('search-results/', SearchResultTemplateView.as_view(), name='search_result_page'),

    #syslogs
    path('system-logs/', SysLogTemplateView.as_view(), name='syslogs'),

    #userprofile
    path('profile/', UserProfileTemplateView.as_view(), name='profile'),
    path('profile/settings/', ProfileSettingsTemplateView.as_view(), name='profile_settings'),

    path('', DashboardTemplateView.as_view(), name='dashboard'),
]
