from django import forms
from.models import User

class DateInput(forms.DateInput):
    input_type = "date"

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = "__all__"
        widgets = {"password":forms.PasswordInput()}
