from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from students.models import Student


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

def course_details(request):
    context = {
        "courses": [
        "Core Python",
        "Django",
        "REST API",
        "Data Analysis"
        ]
    }
    return render(request, "students/course-list.html", context)

def course_details_feature_name(request, feature_name):
    context = {
        "courses": [
        "Core Python",
        "Django",
        "REST API",
        "Data Analysis"
        ]
    }
    if feature_name == "extends":
        return render(request, "students/extended-course-list.html", context)
    elif feature_name == "includes":
        return render(request, "students/includes-course-list.html", context)
    else:
        return HttpResponse(f"Invalid feature name: {feature_name}")

def create_student(request):

    if request.method == "POST":

        name = request.POST.get("name")
        age = request.POST.get("age")
        course = request.POST.get("course")

        Student.objects.create(
            name=name,
            age=age,
            course=course
        )
        return redirect("student-list")

    return render(request, "students/create-student.html")

def student_list(request):
    students = Student.objects.all()
    return render(request, "students/students-list.html", {"students": students})

def update_student(request, id):

    student = get_object_or_404(Student, id=id)

    if request.method == "POST":

        student.name = request.POST.get("name")
        student.age = request.POST.get("age")
        student.course = request.POST.get("course")

        student.save()

        return redirect("student-list")

    return render(
        request,
        "students/update-student.html",
        {"student": student}
    )

def delete_student(request, id):

    student = get_object_or_404(Student, id=id)
    if request.method == "POST":

        student.delete()

        return redirect("student-list")
    return render(request, "students/delete-student.html")