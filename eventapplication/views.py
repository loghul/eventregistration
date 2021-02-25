from django.shortcuts import render
from .models import Participant

# Create your views here.

def home(request):
    context = {}
    return render(request, 'eventapplication/home.html',context)

def register(request):
    context = {}
    if request.method == 'POST':
        p1 = Participant()
        p1.username = request.POST.get('username','-')
        p1.email = request.POST.get('email','-')
        p1.phone = request.POST.get('phone','000')

        if len(Participant.objects.all()) > 15:
            return render(request, 'eventapplication/Failed.html',context)
        else:
            p1.save()
            return render(request, 'eventapplication/Success.html',context)

    if request.method == 'GET':
        context['username'] = ''
        context['email'] = ''
        context['phone'] = ''

    return render(request, 'eventapplication/register.html',context)

def listofparticipants(request):
    context = {}

    context['participants'] = Participant.objects.all()

    return render(request, 'eventapplication/listofparticipants.html', context)    

