from django.shortcuts import render, HttpResponse, get_object_or_404
from django.template import loader
from .models import *

# The main index of all appointments
def index(request):
    all_appointments_list = Appointment.objects.order_by('time')
    print(all_appointments_list[1])
    context = {
        'all_appointments_list': all_appointments_list,
    }
    return render(request, 'walk_scheduler/index.html', context)

# A detail view of the appointments, showind dog walker, time, and dogs w/ their pickup locatoins
def appointment(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    all_walks_list =  Walk.objects.filter(appointment = appointment)
    context = {
        'appointment': appointment,
        'all_walks_list' : all_walks_list,
    }
    return render(request, 'walk_scheduler/appointment_detail.html', context)

# Form view for scheduling a walk. If users are fully implemented we would filter the list of dogs
# to those only owned by the user
def schedule_walk(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)
    all_dogs_list = Dog.objects.all()

    context = {
        'appointment': appointment,
        'all_dogs_list' : all_dogs_list,
    }
    return render(request, 'walk_scheduler/schedule_walk_form.html', context)

# Handle a walk form submission, we will check that the appointment has fewer than 5 walks already scheduled
# as well as that the dog exists in our database, just in case
def schedule_walk_submit(request, appointment_id):
    appointment = get_object_or_404(Appointment, pk=appointment_id)

    # Check if the appointment has more than 5 walks
    if  (len(Walk.objects.filter(appointment = appointment)) > 5):
        return render(request, 'walk_scheduler/schedule_walk_form.html', {
            'appointment': appointment,
            'all_dogs_list' : Dog.objects.all(),
            'error_message' : 'This appointment is fully booked'
        })
    else:
        # Check if the dog exists in our DB
        try:
            selected_dog = Dog.objects.get(pk=request.POST['dog'])
        except (KeyError, Dog.DoesNotExist):
            return render(request, 'walk_scheduler/schedule_walk_form.html', {
                'appointment': appointment,
                'all_dogs_list' : Dog.objects.all(),
                'error_message' : ':You did not select a dog'
            })
        else:
            # Finally, check that the dog isn't already scheduled for a walk
            if Walk.objects.filter(appointment = appointment, dog=selected_dog): 
               return render(request, 'walk_scheduler/schedule_walk_form.html', {
                    'appointment': appointment,
                    'all_dogs_list' : Dog.objects.all(),
                    'error_message' : 'This dog is already scheduled for this walk'
                })
            else:
                w = Walk(dog= selected_dog, appointment=appointment,pickup_location=request.POST['pickup_location'], dropoff_location=request.POST['dropoff_location'])
                w.save()
                context = {
                    'appointment': appointment,
                    'all_walks_list' : Walk.objects.filter(appointment = appointment),
                }
                return render(request, 'walk_scheduler/appointment_detail.html', context)