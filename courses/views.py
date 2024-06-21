from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .forms import StudentIDForm
from .models import Course, Instructor, Student, Enrollment, Assessment, Grade, CourseInstructor
from .forms import CourseForm, InstructorForm, StudentForm, EnrollmentForm, AssessmentForm, GradeForm, CourseInstructorForm

# Courses
def course_list(request):
    courses = Course.objects.filter(is_deleted=False)
    return render(request, 'courses/course_list.html', {'courses': courses})

def course_add(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm()
    return render(request, 'courses/course_form.html', {'form': form})

def course_edit(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_list')
    else:
        form = CourseForm(instance=course)
    return render(request, 'courses/course_form.html', {'form': form})

def course_delete(request, pk):
    course = get_object_or_404(Course, pk=pk)
    if request.method == 'POST':
        course.is_deleted = True;
        course.deleted_date = datetime.now()
        course.save()
        return redirect('course_list')
    return render(request, 'courses/course_confirm_delete.html', {'course': course})

# Instructors
def instructor_list(request):
    instructors = Instructor.objects.filter(is_deleted=False)
    return render(request, 'courses/instructor_list.html', {'instructors': instructors})

def instructor_add(request):
    if request.method == 'POST':
        form = InstructorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('instructor_list')
    else:
        form = InstructorForm()
    return render(request, 'courses/instructor_form.html', {'form': form})

def instructor_edit(request, pk):
    instructor = get_object_or_404(Instructor, pk=pk)
    if request.method == 'POST':
        form = InstructorForm(request.POST, instance=instructor)
        if form.is_valid():
            form.save()
            return redirect('instructor_list')
    else:
        form = InstructorForm(instance=instructor)
    return render(request, 'courses/instructor_form.html', {'form': form})

def instructor_delete(request, pk):
    instructor = get_object_or_404(Instructor, pk=pk)
    if request.method == 'POST':
        instructor.is_deleted = True;
        instructor.deleted_date = datetime.now()
        instructor.save()
        return redirect('instructor_list')
    return render(request, 'courses/instructor_confirm_delete.html', {'instructor': instructor})

# Students
def student_list(request):
    students = Student.objects.filter(is_deleted=False)
    return render(request, 'courses/student_list.html', {'students': students})

def student_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'courses/student_form.html', {'form': form})

def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('student_list')
    else:
        form = StudentForm(instance=student)
    return render(request, 'courses/student_form.html', {'form': form})

def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == 'POST':
        student.is_deleted = True;
        student.deleted_date = datetime.now()
        student.save()
        return redirect('student_list')
    return render(request, 'courses/student_confirm_delete.html', {'student': student})

# Enrollments
def enrollment_list(request):
    enrollments = Enrollment.objects.filter(is_deleted=False)
    return render(request, 'courses/enrollment_list.html', {'enrollments': enrollments})

def enrollment_add(request):
    if request.method == 'POST':
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm()
    return render(request, 'courses/enrollment_form.html', {'form': form})

def enrollment_edit(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    if request.method == 'POST':
        form = EnrollmentForm(request.POST, instance=enrollment)
        if form.is_valid():
            form.save()
            return redirect('enrollment_list')
    else:
        form = EnrollmentForm(instance=enrollment)
    return render(request, 'courses/enrollment_form.html', {'form': form})

def enrollment_delete(request, pk):
    enrollment = get_object_or_404(Enrollment, pk=pk)
    if request.method == 'POST':
        enrollment.is_deleted = True;
        enrollment.deleted_date = datetime.now()
        enrollment.save()
        return redirect('enrollment_list')
    return render(request, 'courses/enrollment_confirm_delete.html', {'enrollment': enrollment})

# Assessments
def assessment_list(request):
    assessments = Assessment.objects.filter(is_deleted=False)
    return render(request, 'courses/assessment_list.html', {'assessments': assessments})

def assessment_add(request):
    if request.method == 'POST':
        form = AssessmentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('assessment_list')
    else:
        form = AssessmentForm()
    return render(request, 'courses/assessment_form.html', {'form': form})

def assessment_edit(request, pk):
    assessment = get_object_or_404(Assessment, pk=pk)
    if request.method == 'POST':
        form = AssessmentForm(request.POST, instance=assessment)
        if form.is_valid():
            form.save()
            return redirect('assessment_list')
    else:
        form = AssessmentForm(instance=assessment)
    return render(request, 'courses/assessment_form.html', {'form': form})

def assessment_delete(request, pk):
    assessment = get_object_or_404(Assessment, pk=pk)
    if request.method == 'POST':
        assessment.is_deleted = True;
        assessment.deleted_date = datetime.now()
        assessment.save()
        return redirect('assessment_list')
    return render(request, 'courses/assessment_confirm_delete.html', {'assessment': assessment})

# Grades
def grade_list(request):
    grades = Grade.objects.filter(is_deleted=False)
    return render(request, 'courses/grade_list.html', {'grades': grades})

def grade_add(request):
    if request.method == 'POST':
        form = GradeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
    else:
        form = GradeForm()
    return render(request, 'courses/grade_form.html', {'form': form})

def grade_edit(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    if request.method == 'POST':
        form = GradeForm(request.POST, instance=grade)
        if form.is_valid():
            form.save()
            return redirect('grade_list')
    else:
        form = GradeForm(instance=grade)
    return render(request, 'courses/grade_form.html', {'form': form})

def grade_delete(request, pk):
    grade = get_object_or_404(Grade, pk=pk)
    if request.method == 'POST':
        grade.is_deleted = True;
        grade.deleted_date = datetime.now()
        grade.save()
        return redirect('grade_list')
    return render(request, 'courses/grade_confirm_delete.html', {'grade': grade})

# CourseInstructors
def courseinstructor_list(request):
    courseinstructors = CourseInstructor.objects.filter(is_deleted=False)
    return render(request, 'courses/courseinstructor_list.html', {'courseinstructors': courseinstructors})

def courseinstructor_add(request):
    if request.method == 'POST':
        form = CourseInstructorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courseinstructor_list')
    else:
        form = CourseInstructorForm()
    return render(request, 'courses/courseinstructor_form.html', {'form': form})

def courseinstructor_edit(request, pk):
    courseinstructor = get_object_or_404(CourseInstructor, pk=pk)
    if request.method == 'POST':
        form = CourseInstructorForm(request.POST, instance=courseinstructor)
        if form.is_valid():
            form.save()
            return redirect('courseinstructor_list')
    else:
        form = CourseInstructorForm(instance=courseinstructor)
    return render(request, 'courses/courseinstructor_form.html', {'form': form})

def courseinstructor_delete(request, pk):
    courseinstructor = get_object_or_404(CourseInstructor, pk=pk)
    if request.method == 'POST':
        courseinstructor.is_deleted = True;
        courseinstructor.deleted_date = datetime.now()
        courseinstructor.save()
        return redirect('courseinstructor_list')
    return render(request, 'courses/courseinstructor_confirm_delete.html', {'courseinstructor': courseinstructor})
def index(request):
    return render(request, 'courses/index.html')

def enter_student_id(request):
    if request.method == 'POST':
        form = StudentIDForm(request.POST)
        if form.is_valid():
            student_id = form.cleaned_data['student_id']
            try:
                student = Student.objects.get(pk=student_id, is_deleted=False)
            except Student.DoesNotExist:
                form.add_error('student_id', 'Student with this ID does not exist.')
                return render(request, 'courses/enter_student_id.html', {'form': form})

            return redirect('student_detail', student_id=student_id)
    else:
        form = StudentIDForm()

    return render(request, 'courses/enter_student_id.html', {'form': form})
def student_detail(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    enrollments = Enrollment.objects.filter(Student=student)
    assessments = Assessment.objects.filter(Course__in=enrollments.values('Course'))
    course_instructors = CourseInstructor.objects.filter(Course__in=enrollments.values('Course'))
    grades = Grade.objects.filter(Student=student)

    context = {
        'student': student,
        'enrollments': enrollments,
        'grades': grades,
        'assessments': assessments,
        'course_instructors': course_instructors
    }
    return render(request, 'courses/student_assessments.html', context)
def deleted_items(request):
    deleted_courses = Course.objects.filter(is_deleted=True)
    deleted_instructors = Instructor.objects.filter(is_deleted=True)
    deleted_students = Student.objects.filter(is_deleted=True)
    deleted_assessments = Assessment.objects.filter(is_deleted=True)
    deleted_grades = Grade.objects.filter(is_deleted=True)
    deleted_enrollments = Enrollment.objects.filter(is_deleted=True)
    deleted_course_instructors = CourseInstructor.objects.filter(is_deleted=True)

    context = {
        'deleted_courses': deleted_courses,
        'deleted_instructors': deleted_instructors,
        'deleted_students': deleted_students,
        'deleted_assessments': deleted_assessments,
        'deleted_grades': deleted_grades,
        'deleted_enrollments': deleted_enrollments,
        'deleted_course_instructors': deleted_course_instructors,
    }
    return render(request, 'courses/deleted_items.html', context)