import os
import ssl
import sendgrid
from sendgrid.helpers.mail import *

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.mail import send_mail
from django.utils import timezone

from .forms import EnquiryForm
from .models import Enquiry

# ssl._create_default_https_context = ssl._create_unverified_context

# Create your views here.
def index(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            e = Enquiry(
                name = data['name'],
                email = data['email'],
                adults = data['adults'],
                children = data['children'],
                enq_date_start = data['enq_date_start'],
                enq_date_end = data['enq_date_end'],
            )
            e.save()
            # Compile the email
            subject = 'New Enquiry from your Website'
            message = ('You have received a new enquiry on your website. '
            + 'Here are the details:\n\n'
            + 'From: ' + e.name + '\n'
            + 'Email: ' + e.email + '\n'
            + str(e.adults) + ' adults' + '\n'
            + str(e.children) + ' children' + '\n'
            + 'Check-in: ' + e.enq_date_start.strftime('%d %B, %Y') + '\n'
            + 'Check-out: ' + e.enq_date_end.strftime('%d %B, %Y') + '\n'
            )
            # send_mail(
            #     subject,
            #     message,
            #     'jar3dh0lm3s@gmail.com',
            #     ['wisterialodge11@gmail.com'],
            #     fail_silently=True,
            # )
            # return render(request, 'enquiries/dist/enquiry-success.html', {'form': form})
            sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
            from_email = Email('wisterialodge11@gmail.com')
            to_email = Email('wisterialodge11@gmail.com')
            email_subject = subject
            email_content = Content('text/plain', message)
            mail = Mail(from_email, email_subject, to_email, email_content)
            response = sg.client.mail.send.post(request_body=mail.get())

            if response.status_code == 202:
                return render(request, 'enquiries/dist/enquiry-success.html', context = { 'form' : form })

    else:
        form = EnquiryForm()

    context = {
        'form': form
    }

    return render(request, 'enquiries/dist/enquiry.html', context,)
