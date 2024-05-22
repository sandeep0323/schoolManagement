from django.urls import path
from .views import StudentListCreate, StudentRetrieveUpdateDestroy, CourseListCreate, CourseRetrieveUpdateDestroy, StudentCoursesListCreate, StudentCoursesRetrieveUpdateDestroy


urlpatterns = [
    path('students/', StudentListCreate.as_view(), name='student-list-create'),
    path('students/<int:pk>/', StudentRetrieveUpdateDestroy.as_view(), name='student-retrieve-update-destroy'),

    path('courses/', CourseListCreate.as_view(), name='course-list-create'),
    path('courses/<int:pk>/', CourseRetrieveUpdateDestroy.as_view(), name='course-retrieve-update-destroy'),

    # URLs for student-courses
    path('student-courses/', StudentCoursesListCreate.as_view(), name='student-courses-list-create'),
    path('student-courses/<int:pk>/', StudentCoursesRetrieveUpdateDestroy.as_view(), name='student-courses-retrieve-update-destroy'),
]
