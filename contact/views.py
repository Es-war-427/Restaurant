from django.shortcuts import render, redirect, get_object_or_404
from .models import Contact
from django.contrib import messages  # For user feedback


def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        review = request.POST.get('review')

        if name and email and review:
            contact = Contact(name=name, email=email, review=review)
            contact.save()
            messages.success(request, "Your review has been submitted!")
        else:
            messages.error(request, "Please fill in all fields.")

        # Refresh the page with new data
        return redirect('/contact/')  # Ensures form reloading, avoids resubmission

    # GET method
    service = Contact.objects.all()
    data = {'service': service}
    return render(request, 'contact.html', data)


def delete(request, id):
    dele = get_object_or_404(Contact, id=id)
    dele.delete()
    messages.success(request, "Review deleted successfully.")
    return redirect('/contact/')
