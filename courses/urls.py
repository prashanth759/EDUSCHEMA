from django.urls import path
from . import views
from django.http import HttpResponse
from .views import (
    course_list, course_add, course_edit, course_delete,
    instructor_list, instructor_add, instructor_edit, instructor_delete,
    student_list, student_add, student_edit, student_delete,
    enrollment_list, enrollment_add, enrollment_edit, enrollment_delete,
    assessment_list, assessment_add, assessment_edit, assessment_delete,
    grade_list, grade_add, grade_edit, grade_delete,
    courseinstructor_list, courseinstructor_add, courseinstructor_edit, courseinstructor_delete, student_detail, deleted_items
)

urlpatterns = [
    path('', views.index, name='index'),
    path('enter_student_id/', views.enter_student_id, name='enter_student_id'),
    path('student/<int:student_id>', student_detail, name='student_detail'),
    path('deleted_items/', deleted_items, name='deleted_items'),
    path('courses/', course_list, name='course_list'),
    path('courses/add/', course_add, name='course_add'),
    path('courses/edit/<int:pk>/', course_edit, name='course_edit'),
    path('courses/delete/<int:pk>/', course_delete, name='course_delete'),

    path('instructors/', instructor_list, name='instructor_list'),
    path('instructors/add/', instructor_add, name='instructor_add'),
    path('instructors/edit/<int:pk>/', instructor_edit, name='instructor_edit'),
    path('instructors/delete/<int:pk>/', instructor_delete, name='instructor_delete'),

    path('students/', student_list, name='student_list'),
    path('students/add/', student_add, name='student_add'),
    path('students/edit/<int:pk>/', student_edit, name='student_edit'),
    path('students/delete/<int:pk>/', student_delete, name='student_delete'),

    path('enrollments/', enrollment_list, name='enrollment_list'),
    path('enrollments/add/', enrollment_add, name='enrollment_add'),
    path('enrollments/edit/<int:pk>/', enrollment_edit, name='enrollment_edit'),
    path('enrollments/delete/<int:pk>/', enrollment_delete, name='enrollment_delete'),

    path('assessments/', assessment_list, name='assessment_list'),
    path('assessments/add/', assessment_add, name='assessment_add'),
    path('assessments/edit/<int:pk>/', assessment_edit, name='assessment_edit'),
    path('assessments/delete/<int:pk>/', assessment_delete, name='assessment_delete'),

    path('grades/', grade_list, name='grade_list'),
    path('grades/add/', grade_add, name='grade_add'),
    path('grades/edit/<int:pk>/', grade_edit, name='grade_edit'),
    path('grades/delete/<int:pk>/', grade_delete, name='grade_delete'),

    path('courseinstructors/', courseinstructor_list, name='courseinstructor_list'),
    path('courseinstructors/add/', courseinstructor_add, name='courseinstructor_add'),
    path('courseinstructors/edit/<int:pk>/', courseinstructor_edit, name='courseinstructor_edit'),
    path('courseinstructors/delete/<int:pk>/', courseinstructor_delete, name='courseinstructor_delete'),
]
