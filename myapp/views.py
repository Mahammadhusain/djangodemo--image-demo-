from django.shortcuts import render,redirect
from .models import HotelModel
from django.contrib import messages
# Create your views here.
def HomeView(request):
  if request.method == 'POST':
    h_name= request.POST.get('hotelname')
    h_image= request.FILES.get('hotelname')
    HotelModel.objects.create(name=h_name,pic=h_image)
    messages.success(request,'Student Successfully Inserted')
    return redirect('/')
  else:
    return render(request,'index.html')


# def HomeView(request):
#     student_data = HotelModel.objects.all() # Show data of Student Table
#     if request.method == 'POST':
#         form = Student(request.POST,request.FILES)
#         if form.is_valid():
#             form.save()
#             messages.success(request,'Student Successfully Inserted')
#             return redirect('/home/')
#     else:
#         form = Student()
#     context= {'form':form,'student_data':student_data}
#     return render(request,'home.html',context)
