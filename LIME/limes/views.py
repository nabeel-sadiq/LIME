from django.shortcuts import render, redirect
from .models import Limes
from .forms import LimeForm

# Display all limes (tweets)
def limes(request):
    limes = Limes.objects.all()
    return render(request, "limes.html", {"limes": limes})

# Create a new lime (tweet)
def lime_create(request):
    if request.method == 'POST':
        form = LimeForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new lime to the database
            return redirect('limes')  # Redirect to the limes page after submission
    else:
        form = LimeForm()
    return render(request, "lime_create.html", {"form": form})
