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

    def clean_name(self):
        print("Inside clean_name")
        name = self.cleaned_data["name"]
        if not all(char.isalpha() or char.isspace() for char in name):
            raise forms.ValidationError(
                "Name should contain only alphabets and spaces."
            )
        return name

    def clean(self):

        cleaned_data = super().clean()

        age = cleaned_data.get("age")
        course = cleaned_data.get("course")

        if course and course == "Driving" and age < 18:
            raise forms.ValidationError(
                "Driving course requires age 18 or above."
            )

        return cleaned_data



class StudentDepartmentModelForm(forms.ModelForm):

    class Meta:
        model = StudentDepartmentFK
        fields = "__all__"

    def clean(self):
        cleaned_data = super().clean()

        age = cleaned_data.get("age")
        if cleaned_data.get("department"):
            dept = cleaned_data.get("department").name

            if dept and dept == "Management" and age and age < 21:
                raise forms.ValidationError("If the selected department is Management, then the student's age must be at least 21.")

        return cleaned_data

class StudentCourseManyToManyModelForm(forms.ModelForm):

    class Meta:
        model = StudentCourse
        fields = "__all__"