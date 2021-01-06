# users urls
from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView
from administration.views import (
    AdminDashboard,
    Catalog,
    Create,
)

app_name = 'administration'

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('users:admin_login')), name='admin_base'),
    path('dashboard/', AdminDashboard.as_view(), name='dashboard'),
    
]

urlpatterns += [
    path('catalog/', Catalog.as_view(), name='catalog'),
    path('catalog/create', Create.as_view(), name='create_therapy_box_template'),
]