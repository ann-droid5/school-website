# main_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('academics/', views.academics, name='academics'),
    path('admissions/', views.admissions, name='admissions'),
    path('alumni/', views.alumni, name='alumni'),
    path('campus-facilities/', views.campus_facilities, name='campus_facilities'),
    path('faculty-staff/', views.faculty_staff, name='faculty_staff'),
    path('students-life/', views.students_life, name='students_life'),
    path('events/', views.event_details, name='event_details'),
    path('news/', views.news, name='news'),
    path('news-details/', views.news_details, name='news_details'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
]
