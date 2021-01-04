from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django import forms

from therapybox.models import TherapyBoxTemplate

# Create your views here.


class LoginAdminRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('users:admin_login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(self.login_url)
        user = get_user_model().objects.get(email=request.user.email)
        if not user.is_admin:
            return HttpResponseRedirect(self.login_url)
        return super().dispatch(request, *args, **kwargs)


class AdminDashboard(LoginAdminRequiredMixin, TemplateView):
    template_name = 'administration/dashboard.html'




class Inventory(LoginAdminRequiredMixin, TemplateView):
    template_name = 'administration/inventory.html'




class Create(CreateView):
    template_name = 'administration/create.html'
    model = TherapyBoxTemplate
    fields = '__all__'

    def get_form(self, form_class=None):
        """Return an instance of the form to be used in this view."""
        if form_class is None:
            form_class = self.get_form_class()
            form_class.base_fields['image_1'].required = False
        return form_class(**self.get_form_kwargs())