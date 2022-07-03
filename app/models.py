from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
STATE_CHOICES = (
('Andaman & Nicobar ISlands' , 'Andaman & Nicobar Isalnds'),
('Andhra Pradesh' , 'Andhra Pradesh'),
('Arunachal Pradesh' , 'Arunachal Pradesh'),
('Assam' , 'Assam'),
('Bihar' , 'Bihar'),
('Chandigarh' , 'Chandigarh'),
('Chhattisgarh' , 'Chhattisgarh'),
('Dadra & Nagar Haveli' , 'Dadra & Nagar Haveli'),
('Daman and Diu' , 'Daman and Diu'),
('Delhi' , 'Delhi'),
('Goa' , 'Goa'),
('Gujarat' , 'Gujarat'),
('Haryana' , 'Haryana'),
('Himachal Pradesh' , 'Himachal Pradesh'),
('Jammu & Kashmir' , 'Jammu & Kashmir'),
('Jharkhand' , 'Jharkhand'),
( 'Karnataka','Karnataka'),
( 'Kerala','Kerala'),
('Lakshadweep','Lakshadweep'),
('Madhya Pradesh', 'Madhya Pradesh'),
( 'Maharashtra', 'Maharashtra'),
( 'Manipur','Manipur'),
( 'Meghalaya', 'Meghalaya'),
('Mizoram','Mizoram'),
('Nagaland','Nagaland'), 
('Odisha','Odisha'),
('Puducherry','Puducherry'),
('Punjab','Punjab'),
('Rajasthan', 'Rajasthan'),
('Sikkim','Sikkim'),
('Tamil Nadu','Tamil Nadu'),
('Telangana', 'Telangana'),
('Tripura','Tripura'),
('Uttarakhand','Uttarakhand'),
('Uttar Pradesh', 'Uttar Pradesh'),
('West Bengal','West Bengal'),
)

class Customer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    zipcode = models.IntegerField()
    state = models.CharField(choices=STATE_CHOICES, max_length=50)

    def __str__(self):
        return str(self.id)


class Tour(models.Model):
    
    city = models.CharField(max_length=100)
    original_price = models.FloatField()
    discounted_price = models.FloatField()
    description = models.TextField()
    product_image = models.ImageField(upload_to='packageimg')

    def __str__(self):
        return str(self.id)

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)
    
    @property
    def total_cost(self):
        return self.quantity* self.tour.discounted_price
    
    
class Booked(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    tour = models.ForeignKey(Tour, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50,default='Booked')

    @property
    def total_cost(self):
        return self.quantity* self.tour.discounted_price

class Train(models.Model):
    train_no=models.CharField(max_length=100)
    train_name=models.CharField(max_length=100)
    train_from=models.CharField(max_length=100)
    train_to=models.CharField(max_length=100)
    train_time=models.DateTimeField(auto_now_add=True)
    train_price=models.FloatField()

    def __str__(self):
        return str(self.id)



