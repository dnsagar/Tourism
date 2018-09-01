from django.shortcuts import render
from .models import place,hotel

# Create your views here.

def  home(request):

	query=request.POST.get("query")
	

	if query==None:
		obj =place.objects.all()
	else:
		obj =place.objects.filter(pcity__icontains=query)
		
	
		

	return render(request,"home.html",{'path':'http://localhost:8000/static/','obj':obj})
	
	
	
def  detail(request):

	id=request.POST.get("pi")
	print(id)
	
	obj = place.objects.filter(pid=id)


	return render(request,"placedetail.html",{'path':'http://localhost:8000/static/','obj':obj})




def  hotelsearch(request):

	id=request.POST.get("pid")
	print(id)
	
	obj = hotel.objects.filter(pid=id)

	return render(request,"hotelsearch.html",{'path':'http://localhost:8000/static/','hotels':obj})
	
	
def  hoteldetail(request):

	p=request.POST.get('hname')
	q=request.POST.get('pid')
	print(p)
	obj=hotel.objects.filter(hname=p,pid=q)
	return render(request,"hoteldetail.html",{'path':'http://localhost:8000/static/','hotels':obj[0]})

	

