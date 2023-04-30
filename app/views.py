from django.shortcuts import render

# Create your views here.
def filters(request):
    data='Chennai SUper KinGs'
    d={'data':data}
    return render(request,'filters.html',context=d)