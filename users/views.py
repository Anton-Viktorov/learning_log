from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Registrations new user"""
    if request.method != 'POST':
        # Show empty registration form
        form = UserCreationForm()
    else:
        # Processing a completed form
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            new_user = form.save()
            # Log in and redirect on home page
            login(request, new_user)
            return redirect('learning_logs:index')

    # Show empty or invalid page
    context = {'form': form}
    return render(request, 'registration/register.html', context)
