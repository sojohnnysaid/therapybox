from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http.response import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic.base import TemplateView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import BaseFormView, ProcessFormView
from django.views.generic.list import ListView
from django.shortcuts import redirect
from django.contrib import messages


from therapybox import models as therapybox_models

# Create your views here.

######################
# CustomMixins #
######################
class LoginMemberRequiredMixin(LoginRequiredMixin):
    login_url = reverse_lazy('users:login')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseRedirect(self.login_url)
        user = get_user_model().objects.get(email=request.user.email)
        return super().dispatch(request, *args, **kwargs)

class PaginationMixin:
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['current_page'] = int(self.request.GET.get('page', 1))
        return context


class LibraryList(LoginMemberRequiredMixin, ListView):
    model = therapybox_models.TherapyBox
    ordering = '-id'
    template_name = 'therapybox/library/list.html'
    paginate_by = 5

    def get_queryset(self):
        new_context = self.model.objects.filter(
            status='AVAILABLE',
        ).order_by('template__id').distinct('template__id')
        return new_context
    


class LibraryDetail(LoginMemberRequiredMixin, DetailView):
    model = therapybox_models.TherapyBox
    template_name = 'therapybox/library/detail.html'
    context_object_name = 'therapybox'



class ShoppingCart(TemplateView):
    template_name = 'therapybox/shopping_cart/checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = therapybox_models.TherapyBox.objects.filter(pk__in=self.request.session['cart']['items'])
        return context

class AddToCart(BaseFormView):
    def post(self, request, *args, **kwargs):
        items = request.session['cart']['items']
        updated_items = list(set(items + [kwargs['pk']]))
        cart = {'items': updated_items}
        request.session['cart'] = cart
        print(request.session['cart'])
        messages.success(request, 'Item added to cart!')
        return redirect(request.META['HTTP_REFERER'])