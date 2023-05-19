from django.shortcuts import render,redirect
from .models import HotelModel
from django.contrib import messages
# Create your views here.
def HomeView(request):
  if request.method == 'POST':
    h_name= request.POST.get('hotelname')
    h_image= request.FILES.get('hotelimage')
    HotelModel.objects.create(name=h_name,pic=h_image)
    messages.success(request,'Student Successfully Inserted')
    return redirect('/')
  else:
    return render(request,'index.html')


