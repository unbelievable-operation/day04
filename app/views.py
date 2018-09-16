from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from app.models import Student


def index(request):
    if request.method == 'GET':
        stus = Student.objects.all()
        return render(request, 'stus.html', {'students': stus})


def del_stu(request, s_id):
    if request.method == 'GET':
        # 删除方法
        # 1. 获取url中id的值
        # id = request.GET.get('id')
        # 2. 获取id对应的学生对象
        stu = Student.objects.get(pk=s_id)
        # 3. 对象.delete()
        stu.delete()
        # return HttpResponse('weqerrtyu')
        return render(request, 'stu_info.html', {'student': stu})
        # return HttpResponseRedirect(reverse('app:index'))


def view_stu(request, s_id):
    stu = Student.objects.get(pk=s_id)
    return render(request, 'stu_info.html', {'student': stu})



def update_info(request):
    return HttpResponseRedirect(reverse('app:index'))
