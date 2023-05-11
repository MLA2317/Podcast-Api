from django import forms
from .models import Contact, Subscribe


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control',
            'id': 'name',
            'placeholder': 'name'
        })
        self.fields['message'].widget.attrs.update({
            'class': 'form-control',
            'id': 'message',
            'placeholder': 'message'
        })


class SubscribeForm(forms.ModelForm):
    class Meta:
        model = Subscribe
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({
            'class': 'newsletter_input',
            'id': 'email',
            'placeholder': 'email'
        })
