from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm


# Create your views here.
def contact(request):
    """
    Render the contact form
    """
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Your inquiry was sent successfully!')
            return redirect('contact_success')
        else:
            messages.error(request, 'Sending the inquiry failed. Please try again.')
    else:
        form = ContactForm()

    return render(request, 'contact/contact.html', {'form': form})


def contact_success(request):
    """
    Render the contact success page
    """
    return render(request, 'contact/contact_success.html')
