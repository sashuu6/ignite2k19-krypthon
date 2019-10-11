from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image

class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	image = models.ImageField(default='default.jpg', upload_to='media')


	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):
		super(Profile, self).save(*args,**kwargs)
		img = Image.open(self.image.path)

		if img.height > 300 or img.width > 300:
			output_size = (300,300)
			img.thumbnail(output_size)
			img.save(self.image.path)

class Booking(models.Model):
	VEHICLE_SIZE = [
		('Personal vehicle','Personal vehicle'),
		('Commercial vehicle','Commercial vehicle'),
		('Sport utility vehicle','Sport utility vehicle'),
		('Special purpose vehicle','Special purpose vehicle')
	]
	CITIES = [
		('Mangalore', 'Mangalore'),
		('Surathkal', 'Surathkal'),
		('Udupi', 'Udupi'),
		('Manipal', 'Manipal')
	]
	driver_name = models.CharField(max_length = 30)
	driver_license = models.CharField(max_length = 30)
	vehicle_number = models.CharField(max_length = 10)
	vehicle_size = models.CharField(max_length = 30, choices = VEHICLE_SIZE, default='Personal vehicle')  
	city = models.CharField(max_length = 30, choices = CITIES, default='Surathkal')
	phone_no = models.CharField(max_length = 14, default = '+91 ')
	checkin_time = models.DateTimeField(default = timezone.now)
	def __str__(self):
		return self.driver_name

			