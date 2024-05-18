from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import *
from .models import *
# import Q

def index(request):
    return render(request,'XYZ.html')

def code(request):
    return render(request, 'code.html',{'name': 'Alexis'})

def StudentForm(request):
    studentf= Student_form()
    if request.method == "POST":
        form = Student_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/CulturalSelect')
    else:
        studentf = Student_form()
        return render(request, 'studentform.html',{'studentf': studentf})
    
    
def select_student(request):
    select = Student.objects.all()
    return render(request,'selectstudent.html',{'select': select})

def DeleteStudent(request, id):
    user = Student.objects.get(id=id)
    user.delete()
    return redirect('/select_student')

def UpdateStudent(request, id):
    record = Student.objects.get(id=id)
    # return render(request, 'updatestudent.html')
    if request.method =="POST":
        form = Student_form(request.POST, instance=record)
        if form.is_valid():
            form.save()
            return redirect('/select_student')
    else:
        form = Student_form(instance=record)

    context = {'form': form, 'record':record}
    return render (request, 'updatestudent.html', context)

def CulturalTroupes(request):
    return render(request,'Cultural troupes.html')
#     user = Student.objects.get(id=id)
#     user.update()
#     return redirect('/select_student')

# def about(request):
#     return HttpResponse("Welcome")
# def Contact(request):
#     return HttpResponse("contact us")
# def login(request):
#     return HttpResponse("make login")




# Create your views here.




def search_troupes(request):
    location = request.GET.get('location', '')  # Get location from GET parameters
    # performance_type = request.GET.get('type', '')  # Get performance type

    # Filter troupes based on search criteria   
    if location:
        troupes = troupes.objects.filter(location_contaner=location)

    if not location:
        context = {'message': 'Please enter at least one search criteria.'}
        return render(request, 'search.html', context)
    # elif location:
    #     troupes = troupes.objects.filter(location__icontains=location)
    # elif performance_type:
    #     troupes = troupes.objects.filter(performance_type=performance_type)
    else:
        troupes = troupes.objects.all()  # Show all troupes if no criteria provided

    context = {'troupes': troupes, 'location': location}  # Pass data to template

    return render(request, 'search.html', context)

def booking(request):
     book = Booking_form()
     if request.method == "POST":
        form = Booking_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
     else:
        book = Booking_form()
        return render(request, 'Booking.html',{'book': book})
        # return render(request, 'Booking.html', {'book': book})

def CulturalSelect(request):
    list_event = Event.objects.all()
    return render (request, 'CulturalSelect.html', {'list_event': list_event})



    # if 'location' in request.GET:
    #     locations =request.GET['location','']
    #     selects = Event.objects.filter(selects__icontains=locations)
    # else:
    #     selects = Event.objects.all()
    # return render(request,'CulturalSelect.html',{'selects':selects})


    # search_query = request.GET.get('location', '')
    # if search_query:
    #     Select = Event.objects.filter(location=search_query)
#     if 'location' in request.GET:
#         search_query =request.GET['location','']
#         search_query = Event.objects.filter(Select__icontains=search_query)
#     else:
#         search_query = Event.objects.all()
   
#     context = {
#             'search_query': search_query, 
#   }

#     return render(request, 'CulturalSelect.html',{'search_query': search_query}, context)

