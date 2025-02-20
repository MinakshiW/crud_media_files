from django.shortcuts import render, redirect
from .forms import PersonForm
from .models import Person

# Create your views here.
def personview(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/a1/sv/')
    return render(request, 'app1/pform.html', {'form': form})

def showview(request):
    obj = Person.objects.all()
    return render(request, 'app1/show.html', {'obj': obj})

def updateview(request, pk):
    obj = Person.objects.get(pk=pk)
    form = PersonForm(instance=obj)
    if request.method == 'POST':
        form = PersonForm(request.POST, request.FILES, instance=obj)
        if form.is_valid():
            form.save()
            return redirect('/a1/sv/')
    return render(request, 'app1/pform.html', {'form': form})


def deleteview(request, x):
    obj = Person.objects.get(pk=x)
    if request.method == 'POST':
        obj.delete()
        return redirect('/a1/sv')
    return render(request, 'app1/success.html', {'obj': obj})