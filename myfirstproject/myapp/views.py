from django.http import HttpResponse,HttpResponseRedirect,JsonResponse

from django.shortcuts import render
from django.shortcuts import render,render_to_response
from django.views.generic import View
from .forms import RegForm


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
    return render_to_response('register.html', {'data': markslist})


def register_view(request):

    register = Registration.objects.all()
    # return render(data)
    return render_to_response('register.html', {'data1': register})


class StudentMarks(View):
    def get(self, request):
        markslist = Marks.objects.all()
        return render_to_response('register.html', {'data': markslist})

    def get(self,request):
        markslist = Marks.objects.all()
        context = {'data': markslist}
        return render_to_response('register.html', context)

def reg_form(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('success.html')

    else:
        form = RegForm()

    return render(request, 'registerform.html', {'form': form})
    return HttpResponseRedirect('success.html')