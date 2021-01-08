from django.http.response import HttpResponseRedirect
from django.template.response import SimpleTemplateResponse, TemplateResponse
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import BaseFormView, CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib import messages

from therapybox import models

# Create your views here.

######################
# CustomMixins #
######################
class LoginAdminRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('users:admin_login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(self.login_url)
        user = get_user_model().objects.get(email=request.user.email)
        if not user.is_admin:
            return HttpResponseRedirect(self.login_url)
        return super().dispatch(request, *args, **kwargs)


class PaginationMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        try:
            context['current_page'] = int(self.request.GET.get('page'))
        except:
            pass
        return context


class AdminDashboard(LoginAdminRequiredMixin, TemplateView):
    template_name = 'administration/dashboard.html'


######################
# TherapyBoxTemplate #
######################

class TherapyBoxTemplateCreate(LoginAdminRequiredMixin, CreateView):
    template_name = 'administration/therapy_box_template/create.html'
    model = models.TherapyBoxTemplate
    fields = '__all__'


class TherapyBoxTemplateEdit(LoginAdminRequiredMixin, UpdateView):
    template_name = 'administration/therapy_box_template/edit.html'
    model = models.TherapyBoxTemplate
    fields = '__all__'


class TherapyBoxTemplateCatalog(LoginAdminRequiredMixin, PaginationMixin, ListView):
    template_name = 'administration/therapy_box_template/list.html'
    model = models.TherapyBoxTemplate
    paginate_by = 5


class TherapyBoxTemplateDetail(LoginAdminRequiredMixin, DetailView):
    template_name = 'administration/therapy_box_template/detail.html'
    model = models.TherapyBoxTemplate
    fields = '__all__'
    context_object_name = 'therapybox'


class TherapyBoxTemplateDelete(DeleteView):
    model = models.TherapyBoxTemplate
    template_name = 'administration/therapy_box_template/delete.html'
    success_url = reverse_lazy('administration:catalog')

    def get_success_url(self):
        messages.success(self.request, f'{self.object} was deleted')
        return super().get_success_url()


class TherapyBoxTemplateDeleteMultiple(View):

    template_name = 'administration/therapy_box_template/delete_multiple.html'
    success_url = reverse_lazy('administration:catalog')

    #confirm page
    def get(self, request):
        print(request.GET)
        GET = request.GET.copy()
        GET.pop('csrfmiddlewaretoken')
        try:
            GET.pop('all')
        except:
            pass
        key_list = [item[0] for item in GET.items()]
        query_set = models.TherapyBoxTemplate.objects.filter(pk__in=key_list)
        return TemplateResponse(request, self.template_name, {'object_list': query_set})

    # deletes and redirects
    def post(self, request):
        GET = request.GET.copy()
        GET.pop('csrfmiddlewaretoken')
        try:
            GET.pop('all')
        except:
            pass
        key_list = [item[0] for item in GET.items()]
        query_set = models.TherapyBoxTemplate.objects.filter(pk__in=key_list)
        query_set.delete()
        messages.success(self.request, f'Selected items deleted')
        return HttpResponseRedirect(self.success_url)
