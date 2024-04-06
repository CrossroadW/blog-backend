from django.forms import Form
from django.shortcuts import render
from django.views.generic import ListView
from . import models


class PersonListView(ListView):
    model = models.Person
    template_name = 'person_info/person_list.html'


def RequestResponse(request):
    context = {
        'name': '李四',
        'age': 123,
        'gender': 'male',
        'email': '310@qq.com',
    }
    return render(request, 'person_info/render_demo.html', context)
