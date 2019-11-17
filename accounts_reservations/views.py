from django.shortcuts import render, redirect
from .models import account_reservation
from django.contrib.auth.models import User
from datetime import datetime
from django.core.mail import send_mail
from django.conf import settings
from django.http import HttpResponse


def five_limit():
    if 'number' not in five_limit.__dict__:
        five_limit.number = 0
    if 'compared_time' not in five_limit.__dict__:
        five_limit.compared_time = datetime.now()
    now_time = datetime.now()
    if five_limit.number == 0 or five_limit.number < 5:
        difference = (now_time - five_limit.compared_time).total_seconds()
        print(five_limit.compared_time, five_limit.number)
        if difference < 86400:
            if five_limit.number > 4:
                five_limit.number = 0
                return "error"
            else:
                five_limit.number += 1
                return "success"
        else:
            five_limit.compared_time = now_time
            five_limit.number = 1
            return "success"
    else:
        return "error"


def reservation(request):
    if request.method == 'POST':
        message_type = request.POST['message_type']
        therapist_type = request.POST['therapist_type']
        reservation_date_time = request.POST['reservation_date_time']
        mobile_number = request.POST['mobile_number']
        special_instruction = request.POST['special_instruction']
        date_time_obj = datetime.strptime(
            reservation_date_time, '%Y/%m/%d %H:%M')
        date = date_time_obj.date()
        time = date_time_obj.time()
        reference_id = User.objects.get(username=request.user.username)
        reservation_create = account_reservation(reference_id=reference_id, massagetype=message_type, therapist=therapist_type,
                                                 date=date, time=time, mobile_number=mobile_number, specialinstruction=special_instruction)
        aaa = five_limit()
        if aaa == "success":
            reservation_create.save()
            subject = 'Your Reservation'
            message = 'Username:' + request.user.username + '\n' + 'Phone Number' + \
                mobile_number + '\n' + 'Date and Time:' + str(date) + str(time)
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [reference_id.email, settings.EMAIL_HOST_USER]
            send_mail(subject, message, email_from, recipient_list)
            return render(request, 'accounts_reservations/reservationsuccess.html')
            # return HttpResponse("Email has just sent successfully")
        else:
            # return HttpResponse("Email Sending Failed Because reservation was exceeded")
            return render(request, 'accounts_reservations/reservationexceeded.html')

    else:
        return render(request, 'accounts_reservations/reservation.html')






