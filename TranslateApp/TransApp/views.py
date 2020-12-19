from django.shortcuts import render

# Create your views here.
def Translate(request):
    data=request.POST.get('txt1')
    context={
        'datas':data
    }

    return render(request,'translate.html',context)
def Login(request):

    return render(request,'loginpage.html')
