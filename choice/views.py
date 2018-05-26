# coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse
from .forms import choiceForm
import json
# Create your views here.

global num
global cs
global ie
global auto
global ep
global work
global yan
global abroad
num = 0
cs = 0
ie = 0
auto = 0
ep = 0

work = 0
yan = 0
abroad = 0

def choose(request):
    global num
    global cs
    global ie
    global auto
    global ep
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
                cs += 1
            elif dir1 == 2:
                ie += 1
            elif dir1 == 3:
                auto += 1
            elif dir1 == 4:
                ep += 1
            else:
                return HttpResponse("Error input!")
            if dir2 == 1:
                cs += 1
            elif dir2 == 2:
                ie += 1
            elif dir2 == 3:
                auto += 1
            elif dir2 == 4:
                ep += 1
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
    global cs
    global ie
    global auto
    global ep
    global work
    global yan
    global abroad
    return HttpResponse(
        json.dumps({
            "num":num,
            "CS":cs,
            "ie":ie,
            "auto":auto,
            "ep":ep,
            "work":work,
            "yan":yan,
            "abroad":abroad
        })
    )
