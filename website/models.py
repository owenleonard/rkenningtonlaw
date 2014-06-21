from django.db import models
from django import forms

# Create your models here.

class PracticeArea(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()
	display = models.BooleanField(default=True)

	def __str__(self):
		return self.title

class Disclaimer(models.Model):
	name = models.CharField(max_length=100)
	content = models.TextField()

	def __str__(self):
		return self.name

class ContactRecipient(models.Model):
	recipient = models.EmailField()
	active = models.BooleanField(default=True)

	def __str__(self):
		return self.recipient

class ContactForm(forms.Form):
	sender = forms.EmailField()
	subject = forms.CharField(max_length=100)
	message = forms.CharField(widget=forms.Textarea)

class Content(models.Model):
	title = models.CharField(max_length=100)
	description = models.TextField()

	def __str__(self):
		return self.title
