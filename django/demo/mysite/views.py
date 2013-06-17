from django.shortcuts import render_to_response, render, redirect
from django.template import RequestContext
from django.http import HttpResponse
#from django.utils import simplejson
import datetime
#from bson import json_util
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as user_login, logout as user_logout
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.http import HttpResponseRedirect
from django.utils import timezone
from models import Doc
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def main(request):
    all_post=Doc.objects.all().order_by('-reg_date')
    paginator = Paginator(all_post, 10)

    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        contacts = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        contacts = paginator.page(paginator.num_pages)
    return render_to_response('index.html', {'all_post': contacts },
                              context_instance=RequestContext(request))


def myinfo(request):
    return render(request,'myinfo.html')

def submit(request):
    subject = request.POST['subject']
    contents = request.POST['content']
    writer = request.POST['writer']
    flag = "none"

    post=Doc(dsubject=subject, contents=contents, writer=writer, flag=flag, reg_date=timezone.now())
    post.save()
    return HttpResponseRedirect('/')



def doc_detail(Detailiw):
    model = Doc



