from django import forms

from drive.models import Post    


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()

class RegisterForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class UploadForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['file']

