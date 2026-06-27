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

def student_details_filters_context(request, id):
    context = {
        "id": id,
        "name": "raghavendra rao",
        "course": "django web development",
        "students": ["Ram", "Krishna", "Sai", "Anil"]
    }
    return render(request, "students/context-filter-student.html", context)

def student_profile(request):
    context = {
        "name": "Raghavendra",
        "age": 28,
        "marks": 92,
        "is_placed": False
    }
    return render(request, "students/student-profile.html", context)