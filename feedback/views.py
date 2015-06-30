from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.utils import timezone

from .forms import FeedbackForm

def submit(request):
    if request.method == "POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            submission = form.save(commit=False)
            submission.timestamp = timezone.now()
            submission.save()
            form = FeedbackForm(request.POST)
            messages.add_message(request, messages.SUCCESS,
                'Congratulations, your feedback has been submitted!')
            form = FeedbackForm()
        else:
            form = FeedbackForm(request.POST)
    else:
        form = FeedbackForm()

    return render(request, 'feedback/submit.html', {'form': form })

class SuccessView(TemplateView):
    template_name = 'feedback/success.html'

    def get_context_data(self, **kwargs):
        context = super(SuccessView, self).get_context_data(**kwargs)
        context['email'] = kwargs['email']
        return context
    
