from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Booking,Feedback,PayCards
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm, BookingForm,FeedbackForm, RemoveRow,PayCardRegisterForm
from django.http import Http404
import datetime
import logging
from django.utils import timezone

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
			#getting datas from the form fields
			driver_license = request.POST["driver_license"]
			vehicle_number = request.POST["vehicle_number"]
			phone_no = request.POST["phone_no"]
			vehicle_size = request.POST["vehicle_size"]
			city = request.POST["city"]
			floor = request.POST["floor"]
			block = request.POST["block"]
			space = request.POST["space"]
			#adding new record to the Booking model
			saviour = Booking(floor=floor,block=block,space=space,driver_name = driver_name,driver_license = driver_license, vehicle_number = vehicle_number, phone_no = phone_no, vehicle_size = vehicle_size, city = city)
			saviour.save()
			messages.success(request, f'Payment was successful!')
			form = PayCardRegisterForm(request.POST)
			return render(request, 'users/payment.html',{'Cards' : PayCards.objects.all(), 'form': form})
	else:
		form = BookingForm()
	return render(request, 'users/booking.html', {'form': form})



@login_required
def feedback(request):
	#handling feedback form request
	if request.method == 'POST':
		form = FeedbackForm(request.POST)
		if form.is_valid():
			current_user = request.user
			driver_name = current_user.username
			driver_license = request.POST["user_feedback"]
			#adding new record to the Feedback model
			saviour = Feedback(user_name = driver_name,user_feedback = driver_license)
			saviour.save()
			messages.success(request, f'Feedback was successful!')
			return render(request, 'users/profile.html')
	else:
		form = FeedbackForm()
	return render(request, 'users/feedback.html', {'form': form})


@login_required
def view_bookings(request):
	form = RemoveRow(request.POST)
	return render(request, 'users/view_bookings.html', {'Booking' : Booking.objects.all(), 'form': form})

@login_required
def view_feedbacks(request):
	#Rendering the users/view_feedbacks.html
	return render(request, 'users/view_feedbacks.html', {'Feedback' : Feedback.objects.all()})


@login_required
def payment(request):
	
	#Handling the payment POST request
	if request.method == 'POST':
		form = PayCardRegisterForm(request.POST)
		if form.is_valid():
			current_user = request.user
			user_name = current_user.username
			#getting details from the submitted form
			save_card = request.POST.get("save_card")
			card_no = request.POST["card_no"]
			card_hold_name = request.POST["card_hold_name"]
			card_exp_date = request.POST["card_exp_date"]
			card_cvv = request.POST["card_cvv"]
			postal_code = request.POST["postal_code"]
			#checking if card size is less than or equal to 5
			if save_card and PayCards.objects.all().filter(user_name=request.user.username).count() < 5:
				saviour = PayCards(user_name = user_name,card_no = card_no,card_hold_name=card_hold_name,card_exp_date=card_exp_date,postal_code=postal_code)
				saviour.save()
				messages.success(request, f'Payment was successful')
			elif PayCards.objects.all().filter(user_name=request.user.username).count() >= 5:
				messages.success(request, f'Payment was successful, but no more cards can be saved')
			
				
			
			return redirect('welcome-home')
		
	else:
		#getting the form object
		form = PayCardRegisterForm()
		#Rendering the users/payment.html
		return render(request, 'users/payment.html',{'Cards' : PayCards.objects.all().filter(user_name=request.user.username), 'form': form})



def pricing(request):
	return render(request, 'users/pricing.html')


#function that is used to remove a single row and return back
def remove_row(request):
	if request.method == 'POST':
		form = RemoveRow(request.POST)
		if form.is_valid():
			x = form.cleaned_data.get("row_id")
			obj = get_object_or_404(Booking, pk = x)
			#updating the checkout time of the record
			obj.checkout_time =  datetime.datetime.now()
			obj.active_status=0;
			obj.save()
			return redirect('/view_bookings/')
	else:
		form = RemoveRow()
		return render(request, 'users/view_bookings.html', {'form': form})

#function that is used to select a single card from the cards list
def select_card(request):
	#handling post request if available
	if request.method == 'POST':
		card_no1 = request.POST.get("card_no")
		form = PayCardRegisterForm()
		return render(request, 'users/payment.html',{'Cards' : PayCards.objects.all().filter(user_name=request.user.username),
			'form': form,
			'selectedCard': PayCards.objects.all().filter(user_name=request.user.username).filter(card_no=card_no1)[0:1],
			})
	else:
		#if post request is not available
		form = PayCardRegisterForm()
		return render(request, 'users/payment.html',{'Cards' : PayCards.objects.all().filter(user_name=request.user.username), 'form': form})

		