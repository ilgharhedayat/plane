from django import forms
from .models import ContactUs, WorkWith


class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactUs
        fields = (
            'email',
            'phone_number',
            'title',
            'text',
        )
        labels = {
            'email': 'ایمیل',
            'phone_number': 'شماره تماس',
            'title': 'موضوع',
            'text': 'متن',
        }


class WorkWithForm(forms.ModelForm):
    class Meta:
        model = WorkWith
        fields = (
            'email',
            'phone_number',
            'title',
            'text',
        )
        labels = {
            'email': 'ایمیل',
            'phone_number': 'شماره تماس',
            'title': 'موضوع',
            'text': 'متن',
        }
