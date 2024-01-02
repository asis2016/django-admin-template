from django.contrib import admin
from django.urls import path
from dashboard.views import DashboardTemplateView
from products.views import ProductListTemplateView

urlpatterns = [
    path('admin/', admin.site.urls),

    #products
    path('products/', ProductListTemplateView.as_view(), name='products'),
    
    #dashboard
    path('', DashboardTemplateView.as_view(), name='dashboard'),
]
