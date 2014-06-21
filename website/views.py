from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect

from website.models import PracticeArea, Disclaimer, ContactRecipient, ContactForm, Content

def globalDisclaimer():
	'''retrieves the global disclaimer to be placed at the bottom of the page'''
	return Disclaimer.objects.filter(name="global").first()

def spanish():
	'''retrieves the spanish text to be placed on the right side of the page'''
	return Content.objects.filter(title="spanish").first()

def contactInfo():
	'''retrieves the contact info to be placed on the right side of the page'''
	return Content.objects.filter(title="contact").first()

# Create your views here.
def index(request):
	content = Content.objects.filter(title="home").first()
	return render_to_response('kenningtonlaw/index.html', {'disclaimer': globalDisclaimer(), 'spanish': spanish(), 'contact':contactInfo(), 'content': content})

def areas(request):
	areas = PracticeArea.objects.filter(display=True)
	return render_to_response('kenningtonlaw/areas.html', {'disclaimer': globalDisclaimer(), 'spanish': spanish(), 'contact':contactInfo(), 'areas': areas})

def profile(request):
	content = Content.objects.filter(title="profile").first()
	return render_to_response('kenningtonlaw/profile.html', {'disclaimer': globalDisclaimer(), 'spanish': spanish(), 'contact':contactInfo(), 'content': content})

def directions(request):
	return render_to_response('kenningtonlaw/directions.html', {'disclaimer': globalDisclaimer(), 'spanish': spanish(), 'contact':contactInfo()})

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

	return render(request, 'kenningtonlaw/contact.html', {'disclaimer': globalDisclaimer(), 'spanish': spanish(), 'contact':contactInfo(), 'form': form})

def thanks(request):
	return render_to_response('kenningtonlaw/thanks.html', {'disclaimer': globalDisclaimer(), 'spanish': spanish(), 'contact':contactInfo()})