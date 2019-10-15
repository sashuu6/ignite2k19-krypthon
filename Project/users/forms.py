from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

class UserUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	
	class Meta:
		model = User
		fields = ['username', 'email']


class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ['image']

#Form for booking new slot for parking
class BookingForm(forms.Form):
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
		('Manipal', 'Manipal'),
		('Chandigarh','Chandigarh')
	]
	#adding values for the FLOOR to provide options for spaces of car parking
	FLOORS = [
		('5', '5'),
		('6', '6'),
		('7', '7'),
		('8', '8'),
		('9', '9'),
	]
	#booking details includes the following extra details: 
	# floors
	# block
	# spaces

	driver_license = forms.CharField(widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Enter the license number',
			}
		))
	vehicle_size = forms.CharField(label = 'Select the vehicle size',widget=forms.Select(
			choices = VEHICLE_SIZE,
			attrs = {
				'text-color': 'white'
			}
		))
	city = forms.CharField(label = 'Select the city',widget=forms.Select(
			choices = CITIES,
			attrs = {
				'text-color': 'white'
			}
		))
	
	floor = forms.CharField(label = 'Select the floor',widget=forms.Select(
			choices = FLOORS,
			attrs = {
				'text-color': 'white'
			}
		))
	block = forms.CharField(label = 'Select the block',widget=forms.Select(
			choices = FLOORS,
			attrs = {
				'text-color': 'white'
			}
		))
	space = forms.CharField(label = 'Select the space',widget=forms.Select(
			choices = FLOORS,
			attrs = {
				'text-color': 'white'
			}
		))
	phone_no = forms.CharField(widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Enter the phone number',
			}
		))
	vehicle_number = forms.CharField(widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Enter the vehicle number',
			}
		))

#form for the feedback details
class FeedbackForm(forms.Form):

	#we are only taking the user feedback data with the post request
	user_feedback = forms.CharField(widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Enter a feedback',
			}
		))
	

class RemoveRow(forms.Form):
	row_id = forms.CharField(widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Enter the booking id to delete that booking history',
			}
		))

#form for the payment details so that thet can be saved in the MODEL
class PayCardRegisterForm(forms.Form):
	#card details includes the following : 
	# card_no
	# card_hold_name
	# card_exp_date
	# card_cvv
	# postal_code
	# save_card

	card_no		=	forms.CharField(widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Enter the 16 digit card number',
			}
		))

	card_hold_name	= forms.CharField(widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Enter the name of card holder',
			}
		))

	card_exp_date	=  forms.CharField(widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Enter the name of card holder',
			}
		))

	card_cvv		= forms.CharField(widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Enter the CVV',
			}
		))

	postal_code		= forms.CharField(widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Enter the postal code',
			}
		))
	save_card = forms.BooleanField(label='Save Card?')
	
	