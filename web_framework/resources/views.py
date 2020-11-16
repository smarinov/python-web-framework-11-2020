from django.shortcuts import render, redirect

# Create your views here.
from resources.forms import PetForm
from resources.models import Pet


def pets(request):
    form = PetForm()
    if request.method == 'GET':
        context = {
            'form': PetForm(),
            'pets': Pet.objects.all(),
        }
        return render(request, 'resources/pets_index.html', context)
    else:
        form = PetForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('pets')

        context = {
            'pets': Pet.objects.all(),
            'form': form,
        }
        return render(request, 'resources/pets_index.html', context)