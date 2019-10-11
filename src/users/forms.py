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

class RemoveRow(forms.Form):
	row_id = forms.CharField(widget=forms.TextInput(
			attrs={
				'class': 'form-control',
				'placeholder': 'Enter the booking id to delete that booking history',
			}
		))