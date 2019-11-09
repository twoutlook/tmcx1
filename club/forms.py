from django.forms import ModelForm
from .models import Data2

class MeetingForm(ModelForm):
    class Meta:
        model= Data2
        fields =['date1','name','member','role']
