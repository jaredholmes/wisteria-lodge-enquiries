from datetime import timedelta, date

from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import ValidationError

from . import validators

class EnquiryForm(forms.Form):
    choices_adult = ((1, '1'), (2, '2'))
    choices_children = ((0, '0'), (1, '1'), (2, '2'))

    name = forms.CharField(
        label='Name',
        max_length=50,
        validators=[validators.validate_alpha],
    )
    email = forms.EmailField(
        label='Email address',
        max_length=80,
        validators=[validators.validate_email],
    )
    enq_date_start = forms.DateField(
        label='Check-in date',
        widget=forms.DateInput(attrs={'class': 'datepicker'}),
        validators=[validators.validate_future],
    )
    enq_date_end = forms.DateField(
        label='Check-out date',
        widget=forms.DateInput(attrs={'class': 'datepicker'}),
    )
    adults = forms.ChoiceField(
        choices=choices_adult,
        validators=[validators.validate_integer],
    )
    children = forms.ChoiceField(
        choices=choices_children,
        validators=[validators.validate_integer],
    )

    def clean(self):
        cleaned_data = super().clean()
        enq_date_start = cleaned_data.get('enq_date_start')
        enq_date_end = cleaned_data.get('enq_date_end')

        """Check that check-out is at least 2 days after check-in"""
        if enq_date_start and enq_date_end:
            error_text = "Check-out date must be at least 2 days after check-in date"
            if enq_date_start - enq_date_end >= timedelta(days=-1):
                self.add_error('enq_date_end', error_text)
