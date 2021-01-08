# users urls
from django.urls import path, reverse_lazy
from django.views.generic.base import RedirectView
from administration.views import (
    AdminDashboard,
    TherapyBoxTemplateCatalog,
    TherapyBoxTemplateCreate,
    TherapyBoxTemplateDetail,
    TherapyBoxTemplateDelete,
    TherapyBoxTemplateDeleteMultiple,
    TherapyBoxTemplateEdit,
)

app_name = 'administration'

urlpatterns = [
    path('', RedirectView.as_view(url=reverse_lazy('users:admin_login')), name='admin_base'),
    path('dashboard/', AdminDashboard.as_view(), name='dashboard'),
    
]

urlpatterns += [
    path('catalog/', TherapyBoxTemplateCatalog.as_view(), name='catalog'),
    path('catalog/<int:pk>', TherapyBoxTemplateDetail.as_view(), name='detail_therapy_box_template'),
    path('catalog/create', TherapyBoxTemplateCreate.as_view(), name='create_therapy_box_template'),
    path('catalog/delete/<int:pk>', TherapyBoxTemplateDelete.as_view(),
         name='delete_therapy_box_template'),
    path('catalog/edit/<int:pk>', TherapyBoxTemplateEdit.as_view(),
         name='edit_therapy_box_template'),
    path('catalog/delete-multiple', TherapyBoxTemplateDeleteMultiple.as_view(),
         name='delete_multiple_therapy_box_template')
]
