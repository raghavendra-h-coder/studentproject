from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404

from students.forms import StudentForm, StudentModelForm, StudentDepartmentModelForm, StudentCourseManyToManyModelForm
from students.models import Student, StudentDepartmentFK, StudentCourse


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

    return render(request, "students/create-student-bs.html")

def student_list(request):
    students = Student.objects.all()
    return render(request, "students/students-list-bs.html", {"students": students})

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

def student_home(request):
    return render(request, "students/student-home.html")

def create_student_form(request):
    if request.method == "POST":

        form = StudentForm(request.POST)

        if form.is_valid():
            Student.objects.create(
                name=form.cleaned_data.get("name"),
                age=form.cleaned_data.get("age"),
                course=form.cleaned_data.get("course")
            )

            return redirect("student-list")

    else:
        form = StudentForm()

    return render(
        request,
        "students/create-student-form.html",
        {"form": form}
    )

def create_student_modelform(request):

    if request.method == "POST":

        form = StudentModelForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("student-list")

    else:

        form = StudentModelForm()

    return render(
        request,
        "students/create-student-modelform.html",
        {"form": form}
    )

def update_student_modelform(request, id):

    student = get_object_or_404(Student, id=id)
    if request.method == "POST":

        form = StudentModelForm(request.POST, instance=student)

        if form.is_valid():

            form.save()

            return redirect("student-list")

    else:
        form = StudentModelForm(instance=student)

    return render(
        request,
        "students/update-student-modelform.html",
        {"form": form}
    )

def create_student_department_modelform(request):

    if request.method == "POST":

        form = StudentDepartmentModelForm(request.POST)

        if form.is_valid():

            form.save()

            return redirect("student-list")

    else:

        form = StudentDepartmentModelForm()

    return render(
        request,
        "students/create-student-department-modelform.html",
        {"form": form}
    )

def update_student_department_modelform(request, id):

    student = get_object_or_404(StudentDepartmentFK, id=id)
    if request.method == "POST":

        form = StudentDepartmentModelForm(request.POST, instance=student)

        if form.is_valid():

            form.save()

            return redirect("student-list")

    else:
        form = StudentDepartmentModelForm(instance=student)

    return render(
        request,
        "students/update-student-department-modelform.html",
        {"form": form}
    )

def create_student_course_manytomany_modelform(request):
    if request.method == "POST":
        form = StudentCourseManyToManyModelForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("student-course-mtm-list")
    else:
        form = StudentCourseManyToManyModelForm()
    return render(request, "students/student-course-mtm-modelform.html", {"form": form})

def update_student_course_manytomany_modelform(request, id):
    student = get_object_or_404(StudentCourse, id=id)
    if request.method == "POST":
        form = StudentCourseManyToManyModelForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect("student-course-mtm-list")
    else:
        form = StudentCourseManyToManyModelForm(instance=student)
    return render(request, "students/student-course-mtm-modelform.html", {"form": form})

def student_course_manytomany_list(request):
    students = StudentCourse.objects.all()
    return render(
        request,
        "students/student-course-mtm-list.html",
        {"students": students}
    )