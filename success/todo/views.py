from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect
from .models import task_db
from django.urls import reverse

def home(request):
    tlp = loader.get_template('home.html')
    return HttpResponse(tlp.render({}, request))

def plan(request):
    tlp = loader.get_template('plan.html')
    return HttpResponse(tlp.render({}, request))

def report(request):  
    tlp = loader.get_template('report.html')
    # update report by POST:
    try:
        task_ = request.POST['task']
        expected_time_ = request.POST['expected_time']
        actual_time_ = request.POST['actual_time']
        new = task_db(task_name = task_, expected_time = expected_time_, actual_time = actual_time_)
        new.save()
    except:
        pass
    
    # load all data:
    inputs = task_db.objects.all().values()    # type: dictionary
    context = {
        "input": inputs 
    }

    return HttpResponse(tlp.render(context, request))

