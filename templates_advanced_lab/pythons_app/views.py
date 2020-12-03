from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

from pythons_core.decorators import group_required
from .forms import PythonCreateForm
from .models import Python


# Create your views here.
def index(request):
    pythons = Python.objects.all()
    for python in pythons:
        python.can_edit = python.created_by_id == request.user.id
    context = {
        'pythons': pythons,
    }
    return render(request, 'index.html', context)


@login_required
# @group_required(groups=['Regular User'])
def create(request):
    if request.method == 'GET':
        form = PythonCreateForm()
        return render(request, 'create.html', {'form': form})
    else:
        data = request.POST
        form = PythonCreateForm(data, request.FILES)
        # print(form)
        if form.is_valid():
            python = form.save(commit=False)
            python.created_by = request.user
            python.save()
            return redirect('index')
        else:
            context = {
                'form': form,
            }
            return render(request, 'create.html', context)
