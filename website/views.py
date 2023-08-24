from django.shortcuts import render,HttpResponse
from django.views.generic import View

from myapp.models import *
from .models import *

# Create your views here.
class TestView(View):
    def get(self,request):
        it = Items.objects.all()
        cate = Category.objects.all()
        b = BarCod.objects.all()
        cn = 'cup'
        print(cn)
        context = {'it':it, 'cn':cn, 'cate':cate, 'b':b}
        return render(request,'shop/test.html',context)

def homesite(request):
    b = BarCod.objects.all()
    it = Items.objects.all()
    cate = Category.objects.all()
    print(it.product_img)
    context = {'it':it, 'cate':cate, 'b':b}
    return render(request,'shop/index.html',context)