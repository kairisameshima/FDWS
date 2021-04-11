from django.urls import path

from . import views

app_name = 'walk_scheduler'
urlpatterns = [
    #/walk_scheduler/
    path('', views.index, name='index'),
    #/walk_scheduler/appointments/1
    path('appointments/<int:appointment_id>/', views.appointment, name='appointment'),
    path('schedule_walk/<int:appointment_id>/', views.schedule_walk, name='schedule_walk'),
    path('schedule_walk_submit/<int:appointment_id>/', views.schedule_walk_submit, name='schedule_walk_submit'),

]