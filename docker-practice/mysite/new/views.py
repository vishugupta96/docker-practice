from django.shortcuts import render
import numpy as np

# Create your views here.
def multiply(request):
 a = np.ones(5)
 b = np.array([6,7,8,4,2])
 x =  a*b
 return render(request,'x.html',{'x':x})
