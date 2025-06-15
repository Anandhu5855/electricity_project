from django.shortcuts import render, redirect
from .forms import ElectricityForm

def submit_status(request):
    if request.method == 'POST':
        form = ElectricityForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'home/thankyou.html')
    else:
        form = ElectricityForm()
    return render(request, 'home/form.html', {'form': form})