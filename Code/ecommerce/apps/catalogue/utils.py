from datetime import datetime, timedelta
from calendar import HTMLCalendar

from django.urls import reverse
from django.utils.text import slugify

from .models import Event
from ..orders.models import Appointment


def get_medic_absolute_url(event):
	# Slugify the medic name
	medic_slug = slugify(event.Medico)
	# Get the appointment searching by email and date
	appointment = Appointment.objects.get(client_email=event.client_email, date_time=event.start_time)
	# Pass the appointment id to the url
	return reverse("catalogue:product_detail", args=[medic_slug, appointment.id])


class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	# formats a day as a td
	# filter events by day
	def formatday(self, day, events):
		events_per_day = events.filter(start_time__day=day)
		d = ''
		for event in events_per_day:
			d += f"<a href={get_medic_absolute_url(event)}><li class='medico'> {event.Medico} </li></a>"

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul class='dia'> {d} </ul></td>"
		return '<td></td>'

	# formats a week as a tr
	def formatweek(self, theweek, events):
		week = ''
		for d, weekday in theweek:
			week += self.formatday(d, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self,request, withyear=True):
		events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month , client_email=request.session["email"])

		cal = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		cal += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		cal += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			cal += f'{self.formatweek(week, events)}\n'
		return cal