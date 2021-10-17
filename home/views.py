from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib import messages
from .models import HomeItem
from .models import DoneItem
from subprocess import check_output
import os
import time

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
