from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect

from website.models import PracticeArea, Disclaimer, ContactRecipient, ContactForm

# Create your views here.
def index(request):
	return render_to_response('kenningtonlaw/index.html', {'disclaimer': Disclaimer.objects.filter(name="global").first()})

def areas(request):
	areas = PracticeArea.objects.filter(display=True)
	return render_to_response('kenningtonlaw/areas.html', {'disclaimer': Disclaimer.objects.filter(name="global").first(), 'areas': areas})

def profile(request):
	return render_to_response('kenningtonlaw/profile.html', {'disclaimer': Disclaimer.objects.filter(name="global").first()})

def directions(request):
	return render_to_response('kenningtonlaw/directions.html', {'disclaimer': Disclaimer.objects.filter(name="global").first()})

def contact(request):
	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			subject = form.cleaned_data['subject']
			message = form.cleaned_data['message']
			sender = form.cleaned_data['sender']

			recipients = ContactRecipient.objects.filter(active=True).values_list('recipient', flat=True)

			from django.core.mail import EmailMessage
			email = EmailMessage(subject, message, 'website-contact@rkenningtonlaw.com', recipients, headers = {'Reply-To': sender})
			email.send()

			return HttpResponseRedirect('/thanks')
	else:
		form = ContactForm()

	return render(request, 'kenningtonlaw/contact.html', {'disclaimer': Disclaimer.objects.filter(name="global").first(), 'form': form})

def thanks(request):
	return render_to_response('kenningtonlaw/thanks.html', {'disclaimer': Disclaimer.objects.filter(name="global").first()})