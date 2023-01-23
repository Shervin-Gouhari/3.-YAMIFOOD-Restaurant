from django import forms
from .models import Reservation


# required is True by default
# class ReservationForm(forms.forms):
#     name = forms.CharField(max_length=30)
#     email = forms.EmailField(max_length=100)
#     phone = forms.IntegerField()
#     number = forms.IntegerField(default=0)
#     date = forms.DateField(auto_now=False, auto_now_add=False)
#     time = forms.TimeField(auto_now=False, auto_now_add=False)
     
class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = "__all__"