import calendar
from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from ecommerce.apps.account.models import Incidencia 
from django.http import JsonResponse

from ecommerce.apps.basket.views import basket_add2

from .models import Department, Medic
from ecommerce.apps.catalogue.forms import EventForm

from .utils import Calendar
from django.utils.safestring import mark_safe
from django.http import HttpResponse
from django.views import generic
from .models import *
from django.db.models import Q
from datetime import date, datetime, timedelta

from ..orders.models import Appointment


def product_all(request):
    busqueda = request.GET.get("buscar")
    products = Medic.objects.all()
    # add a temporal email to the session
    if "email" not in request.session:
        request.session["email"] = datetime.now().strftime("%Y%m%d%H%M%S") + "@temporal.com"
    if busqueda:
        medico = Medic.objects.filter(
            Q(name__icontains = busqueda) | 
            Q(surname__icontains = busqueda)
        ).distinct()
        print(medico)
        return render(request, 'catalogue/medics.html', {'products':medico})
    return render(request, "catalogue/index.html", {"products": products, "email": request.session["email"]})

def set_session_email(request):
    request.session["email"] = request.POST["email"]
    return HttpResponseRedirect(reverse('catalogue:calendar'))


def category_list(request, name=None):
    busqueda = request.GET.get("buscar")
    category = get_object_or_404(Department, name=name)
    products = Medic.objects.filter(department=category)
    if busqueda:
        medico = Medic.objects.filter(
            Q(name__icontains = busqueda) | 
            Q(surname__icontains = busqueda)
        ).distinct()
        print(medico)
        return render(request, 'catalogue/medics.html', {'products':medico})
    return render(request, "catalogue/category.html", {"category": category, "products": products, "email": request.session["email"]})


def product_detail(request, slug, appointment_id=None):
    product = get_object_or_404(Medic, slug=slug)
    if appointment_id:
        appointment = get_object_or_404(Appointment, pk=appointment_id)
        return render(request, "catalogue/single.html", {"product": product, "appointment": appointment, "email": request.session["email"]})
    return render(request, "catalogue/single.html", {"product": product, "email": request.session["email"]})

class CalendarView(generic.ListView):
    model = Event
    template_name = 'catalogue/calendar.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.GET.get('month'):
            d = get_date(self.request.GET.get('month'))
            cal = Calendar(d.year, d.month)
        else:
            d = get_date(self.request.GET.get('day', None))
            cal = Calendar(d.year, d.month)

        html_cal = cal.formatmonth(self.request,withyear=True)
        context['calendar'] = mark_safe(html_cal)
        context['prev_month'] = prev_month(d)
        context['next_month'] = next_month(d)
        context['email'] = self.request.session["email"]
        return context

def get_date(req_day):
    if req_day:
        year, month = (int(x) for x in req_day.split('-'))
        return date(year, month, day=1)
    return datetime.today()

def prev_month(d):
    first = d.replace(day=1)
    prev_month = first - timedelta(days=1)
    month = 'month=' + str(prev_month.year) + '-' + str(prev_month.month)
    return month
def next_month(d):
    days_in_month = calendar.monthrange(d.year, d.month)[1]
    last = d.replace(day=days_in_month)
    next_month = last + timedelta(days=1)
    month = 'month=' + str(next_month.year) + '-' + str(next_month.month)
    return month

def event(request, event_id=None):
    
    
    if event_id:
        instance = get_object_or_404(Event, pk=event_id)
    else:
        instance = Event()
    
    instance.client_email=request.session["email"]
    if request.GET.get('medic', False) : 
        medic=Medic.objects.filter(slug= request.GET["medic"] )[0]
        instance.Medico=medic.name
        instance.Departamento= medic.department.name
   
    form = EventForm(request.POST or None, instance=instance)
    if request.POST and form.is_valid():
        form.save()
        fecha=form['start_time'].value()
        departamento=form['Departamento'].value()
        medico= form['Medico'].value()
        id_medico=Medic.objects.filter(name__contains= medico.split(' ')[0]  ,department=departamento)[0].id
        
        basket_add2(request,id_medico,fecha)
        
        return HttpResponseRedirect(reverse('basket:basket_summary'))
    return render(request, 'catalogue/event.html', {'form': form, 'email': request.session["email"]})


def eventos(request, incidencia_id=None):
    eventos= Event.objects.filter(client_email=request.session["email"])
    
    if request.POST.get("action") == "post":

        print(incidencia_id)
        event_id = int(request.POST.get("evento_id"))
        incidencia = get_object_or_404(Incidencia, id=incidencia_id)
        incidencia.evento=get_object_or_404(Event, id=event_id)
        incidencia.id=incidencia_id
        incidencia.save()
    
        return JsonResponse({'incidencia': incidencia_id})
    
    
    return render(request,'catalogue/eventos.html',{'eventos': eventos, 'incidencia_id': incidencia_id} )

    
   