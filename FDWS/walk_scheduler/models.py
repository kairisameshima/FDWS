from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


## USER MODELS
# Dog Walkers 
class Walker(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

# Dog Owners
class Owner(models.Model):
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)

    def __str__(self):
        return self.first_name + ' ' + self.last_name

# Dogs
class Dog(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE)

    sizes = models.TextChoices('Dog Size', 'SMALL MEDIUM LARGE')
    size = models.CharField(blank=True, choices=sizes.choices, max_length=20)
    def __str__(self):
        return self.name



## SCHEDULER MODELS
# Holds the highest level data for a dog walkers appointment
class Appointment(models.Model):
    walker = models.ForeignKey(Walker, on_delete=models.CASCADE)
    time = models.DateTimeField()

    def __str__(self):
        return self.walker.first_name + ' ' + self.walker.last_name + ' - '  + str(self.time)

# An appoinmentn can consist of up to 5 walks at the same time
class Walk(models.Model):
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE, null = True)

    pickup_location = models.CharField(max_length=150, null=False, blank=False)
    dropoff_location = models.CharField(max_length=150, null=False, blank=False)

    def __str__(self):
        return self.dog.name + ' walk with ' + self.appointment.walker.first_name + ' ' + self.appointment.walker.last_name + ' - '  + str(self.appointment.time)

## Review Models
class ReviewCommonInfo(models.Model):
    rating = models.PositiveSmallIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5),], null=False)
    review_text = models.TextField(max_length=500)
    review_datetime = models.DateTimeField()

    class Meda:
        abstract = True

class WalkerReview(ReviewCommonInfo):
    walker = models.ForeignKey(Walker, on_delete=models.CASCADE)
    author = models.ForeignKey(Owner,  on_delete=models.CASCADE)

class DogReview(ReviewCommonInfo):
    dog = models.ForeignKey(Dog, on_delete=models.CASCADE)
    author = models.ForeignKey(Walker,  on_delete=models.CASCADE)