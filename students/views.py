from django.shortcuts import render


# Create your views here.

def home(request):
    return render(request, "students/home.html")

def student_details(request, id):
    context = {
        "id": id,
        "name": "Raghavendra",
        "course": "Django",
        "duration": "30 Days",
    }
    return render(request, "students/context-student.html", context)