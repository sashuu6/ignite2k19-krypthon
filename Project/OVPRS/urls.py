from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from users import views as user_views


urlpatterns = [
    path('',include('welcome.urls')),
    path('admin/', admin.site.urls),
    path('register/', user_views.register, name='register'),
    path('profile/', user_views.profile, name='profile'),
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='users/password_reset.html'),name='password_reset'),
    path('password-reset/done',auth_views.PasswordResetDoneView.as_view(template_name='users/password_reset_done.html'),name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='users/password_reset_confirm.html'),name='password_reset_confirm'),
    path('password-reset-complete/', auth_views.PasswordResetCompleteView.as_view(template_name = 'users/password_reset_complete.html'),name = 'password_reset_complete'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='welcome/Boot.html'), name='logout'),
    #to add a new booking to the system
    path('booking/',user_views.booking, name='booking'),
    #view the booking that he/she has made
    path('view_bookings/',user_views.view_bookings, name = 'view_bookings'),
    #this is the end point to view the feedbacks
    path('view_feedbacks/',user_views.view_feedbacks, name = 'view_feedbacks'),
    #to get into the payment forms
    path('payment/',user_views.payment, name = 'payment'),
    path('pricing/',user_views.pricing, name = 'pricing'),
    #end point to provide feedbacks
    path('feedback/',user_views.feedback, name = 'feedback'),
    #when a row is to be removed
    path('remove_row/',user_views.remove_row, name = 'remove_row'),
    #invoked when a card is to be selected
    path('select_card/',user_views.select_card, name = 'select_card')
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)