from django.contrib.auth import get_user_model
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.fields.related import ForeignKey
from django.http.response import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.urls.base import reverse
from django.views.generic.base import TemplateView, View
from django.views.generic.detail import DetailView
from django.views.generic.edit import BaseFormView
from django.views.generic.list import ListView
from django.shortcuts import redirect
from django.contrib import messages
from django.utils.safestring import mark_safe
from django.db.models import Sum
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt


from therapybox import models as therapybox_models
from therapybox import services

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
        ).order_by('-template__id').distinct('template__id')
        return new_context
    


class LibraryDetail(LoginMemberRequiredMixin, DetailView):
    model = therapybox_models.TherapyBox
    template_name = 'therapybox/library/detail.html'
    context_object_name = 'therapybox'


class ShoppingCart(LoginMemberRequiredMixin, TemplateView):
    template_name = 'therapybox/shopping_cart/shopping_cart.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['object_list'] = therapybox_models.TherapyBox.objects.filter(pk__in=self.request.session['cart']['items'])
        return context


class AddToCart(LoginMemberRequiredMixin, BaseFormView):
    def post(self, request, *args, **kwargs):
        items = request.session['cart']['items']
        updated_items = list(set(items + [kwargs['pk']]))
        cart = {'items': updated_items}
        request.session['cart'] = cart
        print(request.session['cart'])
        shopping_cart = reverse_lazy('therapybox:shopping_cart')
        messages.success(request, mark_safe(f'Item added to cart! <a href="{shopping_cart}">Checkout now</a>'))
        return redirect(request.META['HTTP_REFERER'])

class RemoveFromCart(LoginMemberRequiredMixin, BaseFormView):
    def post(self, request, *args, **kwargs):
        items = request.session['cart']['items']
        items.remove(kwargs['pk'])
        cart = {'items': items}
        request.session['cart'] = cart
        print(request.session['cart'])
        messages.success(request, 'Item removed from cart!')
        return redirect(request.META['HTTP_REFERER'])


class Checkout(LoginMemberRequiredMixin, TemplateView):
    template_name = 'therapybox/shopping_cart/checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['price'] = therapybox_models.TherapyBox.objects.filter(pk__in=self.request.session['cart']['items']).aggregate(Sum('template__price'))
        context['object_list'] = therapybox_models.TherapyBox.objects.filter(pk__in=self.request.session['cart']['items'])
        context['user'] = get_user_model().objects.get(email=self.request.user.email)
        return context




class PaypalInstantPaymentNotification(BaseFormView):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        print('HELLO POST')
        print(request.POST)
        return HttpResponse(status=200)