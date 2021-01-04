# users urls
from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView
from administration.views import (
    AdminDashboard,
    Inventory,
    Create,
)

app_name = 'administration'
urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('users:admin_login'))),
    path('dashboard/', AdminDashboard.as_view(), name='dashboard'),
    path('inventory', Inventory.as_view(), name='inventory'),
    path('create/', Create.as_view(), name='create_therapy_box_template')
]