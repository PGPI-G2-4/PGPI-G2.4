from django.forms import ModelForm, DateInput , EmailInput, TextInput
from ecommerce.apps.catalogue.models import Event

class EventForm(ModelForm):
  class Meta:
    model = Event
    # datetime-local is a HTML5 input type, format to make date time show on fields
    widgets = {
      'start_time': DateInput(attrs={'type': 'datetime-local' , 'id': 'fecha_cita'}, format='%Y-%m-%dT%H:%M'),
      'client_email': EmailInput(attrs={'type' : 'hidden' ,'id': 'email', }),
      'Medico' : TextInput(attrs={'readonly' : 'readonly' ,'id': 'id_Medico', }),
      'Departamento': TextInput(attrs={'readonly' : 'readonly' ,'id': 'id_Departamento', }),
    }
    fields = ['Medico', 'Departamento', 'start_time' , 'client_email']

  def __init__(self ,*args, **kwargs ):
    super(EventForm, self).__init__(*args, **kwargs)
    # input_formats to parse HTML5 datetime-local input to datetime field
    self.fields['start_time'].input_formats = ('%Y-%m-%dT%H:%M',)
    

    
    
