from django.shortcuts import render,HttpResponse
from django.views.generic import View

from myapp.models import *

# Create your views here.
class TestView(View):
    def get(self,request):
        it = Items.objects.all()
        context = {'it':it}
        return render(request,'shop/test.html',context)