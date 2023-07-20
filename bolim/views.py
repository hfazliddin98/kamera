from django.shortcuts import render, redirect
from .models import Fakultet

def home(request):
    bosh = 'bosh sahifa'
    if request.method == 'POST':
        fakultet = request.POST['fakultet']
        link = request.POST['link']
        nomer = request.POST['nomer']
        data = Fakultet.objects.create(
            fakultet=fakultet, link=link,
            nomer=nomer,
        )
        data.save()
        return redirect('/')
    
    contex = {
        'bosh':bosh,
    }
    return render(request, 'home.html', contex)
