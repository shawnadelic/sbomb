from django.shortcuts import render
from django.contrib import messages
from django.template import Context
from django.core.mail import EmailMessage
from django.template.loader import get_template

from .forms import ContactForm

# Create your views here.
def contact_us(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            name = request.POST.get('name', '')
            email = request.POST.get('email', '')
            message = request.POST.get('message', '')

            template = get_template('contact/contact_template.txt')
            
            context = Context({
                'name': name,
                'email': email,
                'message': message
            })

            content = template.render(context)

            email = EmailMessage(
                "New contact form message!",
                content,
                "Sugarbomb DIY" + '<editors@sugarbombdiy.com>',
                ['editors@sugarbombdiy.com'],
                headers = {'Reply-To': email}
            )

            email.send()

            form = ContactForm()
            messages.add_message(request, messages.SUCCESS,
                'Congratulations, your message was successfully sent!')
        else:
            form = ContactForm(request.POST)
    else:
        form = ContactForm()
    return render(request, 'contact/contact_us.html', {'form': form})
