# Imports
from django.shortcuts import render, reverse, redirect
from django.views import generic, View
from django.contrib.auth.models import User
import datetime
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView
from django.core.paginator import Paginator

from .models import Booking
from .forms import BookingForm


# This shows if user is logged in

def get_user_instance(request):
    # Display autofil features
    user_email = request.user.email
    user = User.objects.filter(email=user_email).first()
    return user


# Dispalyes booking form with autofil features
class Reservations(View):

    template_name = 'bookings/reservations.html'
    success_message = 'Booking has been made.'

    def get(self, request, *args, **kwargs):
        # Collects users email
        if request.user.is_authenticated:
            email = request.user.email
            booking_form = BookingForm(initial={'email': email})
        else:
            booking_form = BookingForm()
        return render(request, 'bookings/reservations.html',
                      {'booking_form': booking_form})

    def post(self, request):
        # COnfirms correct formatting
        booking_form = BookingForm(data=request.POST)

        if booking_form.is_valid():
            booking = booking_form.save(commit=False)
            booking.user = request.user
            booking.save()
            messages.success(
                request, "Booking succesful, awaiting confirmation")
            return render(request, 'bookings/confirmed.html')

        return render(request, 'bookings/reservations.html',
                      {'booking_form': booking_form})


# Dispays the confirmation page upon a succesful booking


# This view will display confirmation on a successful booking
class Confirmed(generic.DetailView):

    template_name = 'bookings/confirmed.html'

    def get(self, request):
        return render(request, 'bookings/confirmed.html')


# Display all the bookings the user has active,

# This view will display all the users bookings
class BookingList(generic.ListView):
    model = Booking
    queryset = Booking.objects.filter().order_by('-created_date')
    template_name = 'booking_list.html'
    paginated_by = 6

    def get(self, request, *args, **kwargs):

        booking = Booking.objects.all()
        paginator = Paginator(Booking.objects.filter(user=request.user), 6)
        page = request.GET.get('page')
        booking_page = paginator.get_page(page)
        today = datetime.datetime.now().date()
        '''
        Shows booking as expired if current date
        beyond date requested
        '''
        for date in booking:
            if date.requested_date < today:
                date.status = 'Booking Expired'

        if request.user.is_authenticated:
            bookings = Booking.objects.filter(user=request.user)
            return render(
                request,
                'bookings/booking_list.html',
                {
                    'booking': booking,
                    'bookings': bookings,
                    'booking_page': booking_page})
        else:
            return redirect('accounts/login.html')


'''
Displays the edit booking page for 
users to edit their reservation
'''


# This view will display the booking by it's primary key 
class EditBooking(SuccessMessageMixin, UpdateView):

    model = Booking
    form_class = BookingForm
    template_name = 'bookings/edit_booking.html'
    success_message = 'Booking has been updated.'

    def get_success_url(self, **kwargs):
        return reverse('booking_list')


# User can delte their booking

def cancel_booking(request, pk):

    booking = Booking.objects.get(pk=pk)

    if request.method == 'POST':
        booking.delete()
        messages.success(request, "Booking cancelled")
        return redirect('booking_list')

    return render(
        request, 'bookings/cancel_booking.html', {'booking': booking})