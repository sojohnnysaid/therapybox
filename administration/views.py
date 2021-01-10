from django.http.response import HttpResponseRedirect
from django.template.response import TemplateResponse
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView, View
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.views.generic import ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.forms.widgets import SelectDateWidget, Select

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
        context['current_page'] = int(self.request.GET.get('page', 1))
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

    def get_form(self):
        '''add date picker in forms'''
        form = super(TherapyBoxTemplateCreate, self).get_form()
        CHOICES = tuple( [(item.name.upper(), item.name) for item in models.Tag.objects.all()])
        form.fields['tags'].widget = Select(choices=CHOICES, attrs={
            'class': 'js-example-basic-multiple',
            'name': 'states[]',
            'multiple': 'multiple'
        })
        return form


class TherapyBoxTemplateEdit(LoginAdminRequiredMixin, UpdateView):
    template_name = 'administration/therapy_box_template/edit.html'
    model = models.TherapyBoxTemplate
    fields = '__all__'

    def get_form(self):
        '''add date picker in forms'''
        form = super(TherapyBoxTemplateEdit, self).get_form()
        CHOICES = tuple( [(item.name.upper(), item.name) for item in models.Tag.objects.all()])
        form.fields['tags'].widget = Select(choices=CHOICES, attrs={
            'class': 'js-example-basic-multiple',
            'name': 'states[]',
            'multiple': 'multiple'
        })
        form.fields['description'].widget.attrs = {'rows': 5, 'cols': 35}
        return form


class TherapyBoxTemplateCatalog(LoginAdminRequiredMixin, PaginationMixin, ListView):
    template_name = 'administration/therapy_box_template/list.html'
    model = models.TherapyBoxTemplate
    paginate_by = 5


class TherapyBoxTemplateDetail(LoginAdminRequiredMixin, DetailView):
    template_name = 'administration/therapy_box_template/detail.html'
    model = models.TherapyBoxTemplate
    fields = '__all__'
    context_object_name = 'therapybox_template'


class TherapyBoxTemplateDelete(DeleteView):
    model = models.TherapyBoxTemplate
    template_name = 'administration/therapy_box_template/delete.html'
    success_url = reverse_lazy('administration:catalog')

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = self.get_success_url()
        try:
            self.object.delete()
        except:
            messages.error(self.request, f'You cannot delete a template with related invetory items. Delete related inventory first!')
            return HttpResponseRedirect(self.success_url)
        messages.success(self.request, f'Selected items deleted')
        return HttpResponseRedirect(self.success_url)



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
        try:
            query_set.delete()
        except:
            messages.error(self.request, f'You cannot delete a template with related invetory items. Delete related inventory first!')
            return HttpResponseRedirect(self.success_url)
        messages.success(self.request, f'Selected items deleted')
        return HttpResponseRedirect(self.success_url)


##############
# TherapyBox #
##############

class TherapyBoxCreate(LoginAdminRequiredMixin, CreateView):
    template_name = 'administration/therapy_box/create.html'
    model = models.TherapyBox
    fields = '__all__'
    initial = {
        'location': 'STORAGE',
        'status': 'AVAILABLE',
        'condition': 'GOOD',
    }

    def get_form(self):
        '''add date picker in forms'''
        form = super(TherapyBoxCreate, self).get_form()
        form.fields['due_back'].widget = SelectDateWidget()
        return form
    
    


class TherapyBoxEdit(LoginAdminRequiredMixin, UpdateView):
    template_name = 'administration/therapy_box/edit.html'
    model = models.TherapyBox
    fields = '__all__'

    def get_form(self):
        '''add date picker in forms'''
        form = super(TherapyBoxEdit, self).get_form()
        form.fields['due_back'].widget = SelectDateWidget()
        form.fields['borrower'].disabled = True
        return form


class TherapyBoxInventory(LoginAdminRequiredMixin, PaginationMixin, ListView):
    template_name = 'administration/therapy_box/list.html'
    model = models.TherapyBox
    paginate_by = 5


class TherapyBoxDetail(LoginAdminRequiredMixin, DetailView):
    template_name = 'administration/therapy_box/detail.html'
    model = models.TherapyBox
    fields = '__all__'
    context_object_name = 'therapybox'


class TherapyBoxDelete(DeleteView):
    template_name = 'administration/therapy_box/delete.html'
    model = models.TherapyBox
    success_url = reverse_lazy('administration:inventory')

    def get_success_url(self):
        messages.success(self.request, f'{self.object} was deleted')
        return super().get_success_url()


class TherapyBoxDeleteMultiple(View):
    template_name = 'administration/therapy_box/delete_multiple.html'
    success_url = reverse_lazy('administration:inventory')

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
        query_set = models.TherapyBox.objects.filter(pk__in=key_list)
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
        query_set = models.TherapyBox.objects.filter(pk__in=key_list)
        query_set.delete()
        messages.success(self.request, f'Selected items deleted')
        return HttpResponseRedirect(self.success_url)




##############
# Tags #
##############

class TagCreate(LoginAdminRequiredMixin, CreateView):
    template_name = 'administration/tag/create.html'
    model = models.Tag
    fields = '__all__'
    success_url = reverse_lazy('administration:tag_list')


class TagEdit(LoginAdminRequiredMixin, UpdateView):
    template_name = 'administration/tag/edit.html'
    model = models.Tag
    fields = '__all__'


class TagList(LoginAdminRequiredMixin, PaginationMixin, ListView):
    template_name = 'administration/tag/list.html'
    model = models.Tag
    paginate_by = 5


class TagDetail(LoginAdminRequiredMixin, DetailView):
    template_name = 'administration/tag/detail.html'
    model = models.Tag
    fields = '__all__'
    context_object_name = 'tag'


class TagDelete(DeleteView):
    template_name = 'administration/tag/delete.html'
    model = models.Tag
    success_url = reverse_lazy('administration:tag_list')

    def get_success_url(self):
        messages.success(self.request, f'{self.object} was deleted')
        return super().get_success_url()


class TagDeleteMultiple(View):
    template_name = 'administration/tag/delete_multiple.html'
    success_url = reverse_lazy('administration:tag_list')

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
        query_set = models.Tag.objects.filter(pk__in=key_list)
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
        query_set = models.Tag.objects.filter(pk__in=key_list)
        query_set.delete()
        messages.success(self.request, f'Selected items deleted')
        return HttpResponseRedirect(self.success_url)
