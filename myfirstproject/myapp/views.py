from django.shortcuts import render
from django.shortcuts import render,render_to_response

from django.http import HttpResponse
# from .models import RegistrationForm

# Create your views here.
# def register(request):
#     registration_data = RegistrationForm.objects.all()
#
#     # return HttpResponse(registration_data)
#     return render_to_response('register.html',{'data':registration_data})

from .models import Marks,Registration

def marks(request):
    markslist = Marks.objects.all()

    # return HttpResponse(registration_data)
    return render_to_response('register.html',{'data':markslist})

def register_view(request):

    data = Registration.objects.all()
    return render(data)