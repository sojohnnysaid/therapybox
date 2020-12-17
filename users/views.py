from django.views.generic.edit import CreateView
from django.http import HttpResponse
from django.db.models import QuerySet
from django.db import models

class test(models.Model):
    pass

# Create your views here.
class UsersRegisterView(CreateView):
    fields = []
    model = test

    def render_to_response(self, context, **response_kwargs) :
        response = HttpResponse('<html><title>Register</title></html>')
        response.rendered_content = response.content.decode('utf8')
        return response

  