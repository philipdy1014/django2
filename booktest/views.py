from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
import os
from django.conf import settings
from .models import *
from django.core.paginator import *
from django.views.decorators.cache import cache_page
from django.core.cache import cache
from .task import *

def index(request):
    return render(request,'booktest/index.html')

#def myExp(request):
    #a1 = int('abc')
#    return HttpResponse('hello')

def uploadPic(request):
    return render(request, 'booktest/uploadPic.html')

def uploadHandle(request):
    pic1=request.FILES['pic1']
    picName=os.path.join(settings.MEDIA_ROOT, pic1.name)
    with open(picName, 'wb') as pic:
        for c in pic1.chunks():
            pic.write(c)
    return HttpResponse('<img src="/static/media/%s"/>'%pic1.name)

def herolist(request,pindex):
    if pindex == '':
        pindex = '1'
    list=HeroInfo.objects.all()
    paginator=Paginator(list,5)
    page=paginator.page(int(pindex))
    context={'page':page}
    return render(request,'booktest/herolist.html',context)

def area(request):
    return render(request,'booktest/area.html')

def pro(request):
    prolist=AreaInfo.objects.filter(parea__isnull=True)
    list=[]
    for item in prolist:
        list.append([item.id, item.title])
    return JsonResponse({'data':list})

def city(request, id):
    citylist=AreaInfo.objects.filter(parea_id=id)
    list=[]
    for item in citylist:
        list.append({'id':item.id, 'title':item.title})
    return JsonResponse({'data':list})

def dis(request, id):
    dislist=AreaInfo.objects.filter(parea_id=id)
    list=[]
    for item in dislist:
        list.append({'id':item.id, 'title':item.title})
    return JsonResponse({'data':list})

def htmlEditor(request):
    return render(request,'booktest/htmlEditor.html')

def htmlEditorHandle(request):
    html=request.POST['hcontent']
    test1=Test1.objects.get(pk=1)
    test1.content=html
    test1.save()
    #test1=Test1()
    #test1.content=html
    #test1.save()
    context={'content':html}
    return render(request,'booktest/htmlShow.html',context)

@cache_page(20)
def cache1(request):
    #cache.set('key1','value1',600)
    cache.clear()
    return render(request,'booktest/cache1.html')


def mysearch(request):
    return render(request,'booktest/mysearch.html')

def celeryTest(request):
    show.delay()
    return HttpResponse('OK')
