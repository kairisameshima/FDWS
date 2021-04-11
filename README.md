# FDWS

# Author: Kairi Sameshima

## How to begin application:
clone repo from github
activate python virtual envronment: $ source dev_space/bin/activate

run django server: $ python manage.py runserver


The following models are currently created from the Django Admin Panel:
- Walkers (People who walk the dogs)
- Owners (Owners of the dogs)
- Dogs
- Appointments

An explanation: an Appointment has a referecne to a single dog walker and a time that the appointment occurs.
Each appointment can have up to 5 walks.

A walk is the data structure used to store data for individual dogs. The dog and appointment are foreign key references
and the walk object stores the pickup and dropoff locations.


Current Functinality:
Index of all appointments
http://127.0.0.1:8000/walk_scheduler/

From here you can view a list of all appointments with the Walker and time.

Clicking on a link will bring you to an appointment detail page, where you can see which dogs are being walked in the appointmennt as well as their pickup locations.
If an appointment has fewer than 5 walks, the "schedule a walk" button will be available so that a user can schedule a walk within the selected appointment.

In the scheduling form, you can choose a dog from a dropdown of all dogs in the database.
TODO:Once sign-in functionality is implemented we can filter the list of dogs so that the owner can only see their dogs
Here you will also fill in the pickup and dropoff locations. These fields are required and are checked on the html side to save us an extra API call.

Once the form is submitted, we validate the inputs by checking that the appointment indeed only has 4 or fewer walks scheduled already (in case another user schedules a walk in the time between the first user viewing the appointment and submitting the form).
We check that the dog object exists in the database as well. If we validated everything the walk object is saved an you will ve taken back to the appointment details page.

