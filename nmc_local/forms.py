from django import forms
from captcha.fields import ReCaptchaField

# our new form
class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True)
    contact_email = forms.EmailField(required=True)
    content = forms.CharField(
        required=True,
        widget=forms.Textarea
    )
    captcha = ReCaptchaField()

    def __init__(self, *args, **kwargs):
        super(ContactForm, self).__init__(*args, **kwargs)
        self.fields['contact_name'].label = "Your name"
        self.fields['contact_email'].label = "Your email"
        self.fields['content'].label = "Your message"
        self.fields['captcha'].label = "Are you a robot?"
