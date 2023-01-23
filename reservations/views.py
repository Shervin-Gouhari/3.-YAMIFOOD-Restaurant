from django.shortcuts import render
from .forms import ReservationForm

def reservation_view(request):
    if request.method == "POST":
        form = ReservationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ReservationForm()
    return render(request, "reservations/reservation.html", {"form": form})