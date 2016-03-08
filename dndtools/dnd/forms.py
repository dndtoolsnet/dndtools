from django import forms
from django.utils.safestring import mark_safe
import dndproject.settings


class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    sender = forms.EmailField(
        required=False,
        label='Your Email',
        help_text='If you want an answer.')


class InaccurateContentForm(forms.Form):
    url = forms.URLField()
    message = forms.CharField(widget=forms.Textarea)
    better_description = forms.CharField(
        widget=forms.Textarea,
        label="Supply better description",
        required=False,
        help_text='Please, supply the text as it SHOULD appear in the description.'
        , )
    sender = forms.EmailField(
        required=False,
        label='Your Email',
        help_text='If you want an answer.')
    