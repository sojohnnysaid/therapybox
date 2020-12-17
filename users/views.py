from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.db.models import QuerySet
from django.db import models

class test(models.Model):
    pass

# Create your views here.
class RegisterView(CreateView):
    fields = []
    model = test



    def render_to_response(self, context, **response_kwargs) :
        return HttpResponse('<html><title>Register</title></html>')

  