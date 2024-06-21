from django import forms
from .models import Course, Instructor, Student, Enrollment, Assessment, Grade, CourseInstructor

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['CourseName', 'CourseDescription', 'StartDate', 'EndDate']

class InstructorForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = ['FirstName', 'LastName', 'Email', 'Bio']

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['FirstName', 'LastName', 'Email', 'DateOfBirth']

class EnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['Student', 'Course', 'EnrollmentDate']

class AssessmentForm(forms.ModelForm):
    class Meta:
        model = Assessment
        fields = ['Course', 'AssessmentName', 'MaxScore']

class GradeForm(forms.ModelForm):
    class Meta:
        model = Grade
        fields = ['Assessment', 'Student', 'Score']

class CourseInstructorForm(forms.ModelForm):
    class Meta:
        model = CourseInstructor
        fields = ['Course', 'Instructor', 'AssignmentDate']
class StudentIDForm(forms.Form):
    student_id = forms.IntegerField(label='             ')