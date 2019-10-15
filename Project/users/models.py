from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
import datetime

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
	#adding values for the FLOOR to provide options for spaces
	FLOORS = [
		('5', '5'),
		('6', '6'),
		('7', '7'),
		('8', '8'),
		('9', '9'),
	]
	driver_name = models.CharField(max_length = 30)
	driver_license = models.CharField(max_length = 30)
	vehicle_number = models.CharField(max_length = 10)
	vehicle_size = models.CharField(max_length = 30, choices = VEHICLE_SIZE, default='Personal vehicle')  
	city = models.CharField(max_length = 30, choices = CITIES, default='Surathkal')
	#adding extra floor item,block space etc
	floor = models.CharField(max_length = 1, choices = FLOORS, default='5')
	block = models.CharField(max_length = 1, choices = FLOORS, default='5')
	space = models.CharField(max_length = 1, choices = FLOORS, default='5')
	phone_no = models.CharField(max_length = 14, default = '+91 ')
	checkin_time = models.DateTimeField(default = datetime.datetime.now())
	checkout_time = models.DateTimeField(default = datetime.datetime.now())
	# to store the active status
	active_status = models.IntegerField(default = 1)
	def __str__(self):
		return self.driver_name
	#adding extra information to the class
	class Meta:
		#making each record unique
		unique_together = ('driver_license','active_status')

#model for the storing feedback datas
class Feedback(models.Model):
	user_name = models.CharField(max_length = 30)
	user_feedback = models.CharField(max_length = 30)
	
	def __str__(self):
		return self.user_name

#Model to save card details
class PayCards(models.Model):
	#making the field as primary key so that a card cannot be acced twice
	card_no  = models.CharField( max_length=16,primary_key=True)
	card_hold_name = models.CharField(max_length = 30,default = 'TestUser')
	#card_type = models.CharField(max_length = 30)
	card_exp_date = models.CharField(max_length = 5,default = '01/01')
	card_cvv  = models.CharField( max_length=3,default = '002')
	postal_code  = models.CharField( max_length=6,default = '673604')
	user_name = models.CharField(max_length = 30)

	def __str__(self):
 		return self.user_name