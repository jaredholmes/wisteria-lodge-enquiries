from datetime import timedelta, date

from django.test import TestCase

from .forms import EnquiryForm
from .models import Enquiry

# Create your tests here.
def test_form_is_valid(self):
    """Valid form form.is_valid() returns True"""
    data = {
        'name': 'Jared',
        'email': 'j@gmail.com',
        'adults': '2',
        'children': '1',
        'enq_date_start': date.today() + timedelta(days=5),
        'enq_date_end': date.today() + timedelta(days=10),
    }
    form = EnquiryForm(data)
    self.assertTrue(form.is_valid())

def test_blank_data(self):
    """Blank form form.is_valid() returns False and
    errors = ['This field is required']"""
    data = {
        'name': '',
        'email': '',
        'adults': '',
        'children': '',
        'enq_date_start': '',
        'enq_date_end': '',
    }
    form = EnquiryForm(data)
    error_required = ['This field is required.']
    self.assertFalse(form.is_valid)
    self.assertEqual(form.errors, {
        'name': error_required,
        'email': error_required,
        'adults': error_required,
        'children': error_required,
        'enq_date_start': error_required,
        'enq_date_end': error_required,
    })

def test_non_alpha_name(self):
    data = {
        'name': 'Jar3d',
        'email': 'j@gmail.com',
        'adults': '2',
        'children': '1',
        'enq_date_start': date.today() + timedelta(days=5),
        'enq_date_end': date.today() + timedelta(days=10),
    }
    form = EnquiryForm(data)
    error = ['\'Jar3d\' contains non-alphabetical characters']
    self.assertFalse(form.is_valid)
    self.assertEqual(form.errors, {
        'name': error,
    })

def test_past_starting_date(self):
    data = {
        'name': 'Jared',
        'email': 'j@gmail.com',
        'adults': '2',
        'children': '1',
        'enq_date_start': date.today() + timedelta(days=-5),
        'enq_date_end': date.today() + timedelta(days=10),
    }
    form = EnquiryForm(data)
    error = ['%s is earlier than tomorrow' % data['enq_date_start']]
    self.assertFalse(form.is_valid)
    self.assertEqual(form.errors, {
        'name': error,
    })

def test_stay_under_2_days(self):
    data = {
        'name': 'Jared',
        'email': 'j@gmail.com',
        'adults': '2',
        'children': '1',
        'enq_date_start': date.today() + timedelta(days=5),
        'enq_date_end': date.today() + timedelta(days=6),
    }
    form = EnquiryForm(data)
    error = ['Check-out date must be at least 2 days after check-in date']
    self.assertFalse(form.is_valid)
    self.assertEqual(form.errors, {
        'name': error,
    })
