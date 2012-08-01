from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

class BaseCustomForm(forms.ModelForm):
    """Add ability to check an email is unique"""
    email = forms.EmailField(required=True)

    def clean(self, commit=True):
        cleaned_data = super(BaseCustomForm, self).clean()
        email_value = cleaned_data.get('email')
        if email_value is None:
            return cleaned_data
        exists_email = User.objects.filter(email__iexact=email_value)
        if self.instance:
            user_email =User.objects.filter(pk=self.instance.id, email__iexact =email_value)
            if user_email is None:
                if exists_email:
                    raise forms.ValidationError("A user with this email already exists.")
            else:
                if self.instance.email != email_value:
                    if exists_email:
                        raise forms.ValidationError("A user with this email already exists.")
        else:
            if exists_email:
                raise forms.ValidationError("A user with this email already exists.")
        return cleaned_data

class UserCreateForm(BaseCustomForm, UserCreationForm):
    """Class for create User"""
    class Meta:
        model = User


class CustomUserChangeForm(BaseCustomForm, UserChangeForm):
    """Class for update User"""
    class Meta:
        model = User

