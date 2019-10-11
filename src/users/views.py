from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Booking
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, BookingForm, RemoveRow
from django.http import Http404



def register(request,*args,**kwargs):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created! You are now able to login')
            return redirect('welcome-home')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})
 

@login_required
def profile(request):
	if request.method == 'POST':
		u_form = UserUpdateForm(request.POST, instance=request.user)
		p_form = ProfileUpdateForm(request.POST, request.FILES, instance= request.user.profile)

		if u_form.is_valid() and p_form.is_valid():
			u_form.save()
			p_form.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('profile')

	else:
		u_form = UserUpdateForm(instance=request.user)
		p_form = ProfileUpdateForm(instance=request.user.profile)

	context ={
		'u_form': u_form,
		'p_form': p_form
	}
	return render(request, 'users/profile.html',context)


@login_required
def booking(request):
	if request.method == 'POST':
		form = BookingForm(request.POST)
		if form.is_valid():
			current_user = request.user
			driver_name = current_user.username
			driver_license = request.POST["driver_license"]
			vehicle_number = request.POST["vehicle_number"]
			phone_no = request.POST["phone_no"]
			vehicle_size = request.POST["vehicle_size"]
			city = request.POST["city"]
			saviour = Booking(driver_name = driver_name,driver_license = driver_license, vehicle_number = vehicle_number, phone_no = phone_no, vehicle_size = vehicle_size, city = city)
			saviour.save()
			messages.success(request, f'Payment was successful!')
			return render(request, 'users/payment.html')
	else:
		form = BookingForm()
	return render(request, 'users/booking.html', {'form': form})

@login_required
def view_bookings(request):
	form = RemoveRow(request.POST)
	return render(request, 'users/view_bookings.html', {'Booking' : Booking.objects.all(), 'form': form})

@login_required
def payment(request):
	if request.method == 'POST':
		messages.success(request, f'Payment was successful')
		return redirect('welcome-home')
	return render(request, 'users/payment.html')


def pricing(request):
	return render(request, 'users/pricing.html')


def remove_row(request):
	if request.method == 'POST':
		form = RemoveRow(request.POST)
		if form.is_valid():
			x = form.cleaned_data.get("row_id")
			obj = get_object_or_404(Booking, pk = x)
			obj.delete()
			return redirect('/view_bookings/')
	else:
		form = RemoveRow()
		return render(request, 'users/view_bookings.html', {'form': form})