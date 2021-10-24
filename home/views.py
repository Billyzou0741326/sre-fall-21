from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import HomeItem
from .models import DoneItem
import psutil
import os
import signal
import time
from operator import is_not
from functools import partial

# Create your views here.
def homeView(request):
    all_home_items = HomeItem.objects.all()
    return render(request, 'home.html', {'all_items': all_home_items})

def addHome(request):
    if not request.POST['content']:
        messages.error(request, 'invalid content')
        return HttpResponseRedirect('/home/')
    if not request.POST['date_created']:
        messages.error(request, 'invalid date')
        return HttpResponseRedirect('/home/')
    if not request.POST['author']:
        messages.error(request, 'invalid author')
        return HttpResponseRedirect('/home/')
    new_item = HomeItem(content = request.POST['content'],
                        date_created = request.POST['date_created'],
                        author = request.POST['author'])
    new_item.save()
    return HttpResponseRedirect('/home/')

def deleteHome(request, home_id):
    done_item = HomeItem.objects.get(id = home_id)
    done_item.delete()
    add_item = DoneItem(content = done_item.content,
                        date_completed = done_item.date_created,
                        author = done_item.author)
    add_item.save()
    return HttpResponseRedirect('/home/')

def doneItems(request):
    all_done_items = DoneItem.objects.all()
    return render(request, 'done.html', {'done_items': all_done_items})

def redirectAbout(request):
    return render(request, 'about.html')

def terminateSite(request, program):
    def get_pinfo(p):
        try:
            return p.as_dict(attrs=['pid', 'name', 'create_time'])
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        return None
    def matches_name(p, program):
        try:
            return program.lower() == p['name'].lower()
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        return False
    def get_pid(pinfo):
        try:
            return pinfo.get('pid')
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        return False
    procs = filter(partial(is_not, None), [ get_pinfo(p) for p in psutil.process_iter() ])
    procs_to_kill = [ p for p in procs if matches_name(p, program) ]
    pids = [ get_pid(p) for p in procs_to_kill ]
    for pid in pids:
        os.kill(pid, signal.SIGTERM)
    return HttpResponseRedirect('/home/')

def sleepSite(request, number):
    try:
        sleep_secs = number / 1000
        time.sleep(sleep_secs)
    except (TypeError, ValueError):
        pass
    return render(request, 'donework.html', {'time': sleep_secs})
