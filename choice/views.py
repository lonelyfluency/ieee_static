# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from .forms import choiceForm
import json
# Create your views here.

global num
global cs1
global ie1
global auto1
global ep1
global cs2
global ie2
global auto2
global ep2
global work
global yan
global abroad
num = 0
cs1 = 0
ie1 = 0
auto1 = 0
ep1 = 0
cs2 = 0
ie2 = 0
auto2 = 0
ep2 = 0
work = 0
yan = 0
abroad = 0

def choose(request):
    global num
    global cs1
    global ie1
    global auto1
    global ep1
    global cs2
    global ie2
    global auto2
    global ep2
    global work
    global yan
    global abroad
    if request.method == "POST":
        form = choiceForm(request.POST)
        if form.is_valid():
            dir1 = form.cleaned_data['direction1']
            dir2 = form.cleaned_data['direction2']
            tmp = form.cleaned_data['future_plan']
            if dir1 == 1:
                cs1 += 1
            elif dir1 == 2:
                ie1 += 1
            elif dir1 == 3:
                auto1 += 1
            elif dir1 == 4:
                ep1 += 1
            else:
                return HttpResponse("Error input!")
            if dir2 == 1:
                cs2 += 1
            elif dir2 == 2:
                ie2 += 1
            elif dir2 == 3:
                auto2 += 1
            elif dir2 == 4:
                ep2 += 1
            elif dir2 == 0:
                pass
            else:
                return HttpResponse("Error input!")
            if tmp == 1:
                work += 1
            elif tmp == 2:
                yan += 1
            elif tmp == 3:
                abroad += 1
            else:
                return HttpResponse("Error input!")
            num += 1
            return HttpResponse("Submitted.")
    else:
        form = choiceForm()
    return render(request, 'choice.html', {'form': form})

def show(request):
    global num
    global cs1
    global ie1
    global auto1
    global ep1
    global cs2
    global ie2
    global auto2
    global ep2
    global work
    global yan
    global abroad
    return HttpResponse(
        json.dumps({
            "num":num,
            "CS1":cs1,
            "ie1":ie1,
            "auto1":auto1,
            "ep1":ep1,
            "CS2": cs2,
            "ie2": ie2,
            "auto2": auto2,
            "ep2": ep2,
            "work":work,
            "yan":yan,
            "abroad":abroad
        })
    )
