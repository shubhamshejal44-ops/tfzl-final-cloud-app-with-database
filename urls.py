from django.urls import path
from . import views

app_name = 'onlinecourse'
urlpatterns = [
    # Route for course list view
    path('', views.CourseListView.as_view(), name='index'),
    # Route for registration
    path('registration/', views.registration_request, name='registration'),
    # Route for login
    path('login/', views.login_request, name='login'),
    # Route for logout
    path('logout/', views.logout_request, name='logout'),
    # Route for course details view
    path('<int:pk>/', views.CourseDetailView.as_view(), name='course_details'),
    # Route for enroll action
    path('<int:course_id>/enroll/', views.enroll, name='enroll'),
    # Route for submitting exam answers
    path('<int:course_id>/submit/', views.submit, name='submit'),
    # Route for showing exam result
    path('course/<int:course_id>/submission/<int:submission_id>/show_exam_result/', views.show_exam_result, name='show_exam_result'),
]
