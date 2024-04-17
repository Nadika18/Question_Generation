from django.shortcuts import render

from django.http import HttpResponse

from .predictor import generate_question
# Create your views here.
def index(request):
    return render(request,'index.html')
    # return HttpResponse("hello")

def submitQ(request):
    if request.method == 'POST':
        txt=request.POST['text']
        que = generate_question(txt)
        return render(request,'index.html',{'que':que})
   
    # return HttpResponse("hello")