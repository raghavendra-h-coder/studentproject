from django import forms

from students.models import Student, StudentDepartmentFK, StudentCourse


class StudentForm(forms.Form):
    name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    age = forms.IntegerField(
        widget=forms.NumberInput(
            attrs={
                "class": "form-control"
            }
        )
    )

    course = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control"
            }
        )
    )

class StudentModelForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = "__all__"

class StudentDepartmentModelForm(forms.ModelForm):

    class Meta:
        model = StudentDepartmentFK
        fields = "__all__"

class StudentCourseManyToManyModelForm(forms.ModelForm):

    class Meta:
        model = StudentCourse
        fields = "__all__"