from django import forms
from .models import Meetups
import extras

class createMeetup(forms.ModelForm): 
    def __init__(self, *args, **kwargs): 
        super(createMeetup, self).__init__(*args, **kwargs)
        self.fields['subjType'].label = 'Subject Type'
        self.fields['meetupType'].label = 'Meetup Type'
        self.fields['buildingNames'].label = 'Building'
    class Meta:
        model = Meetups 
        fields = [
            'subjType', 
            'subjCode', 
            'meetupType',
            'description',
            'buildingNames', 
            'meetupRoom', 
            'meetupStart', 
            'meetupEnd'
        ]
        widgets = {
            'subjType': forms.Select(attrs={'class' : 'form-control'}),    
            'subjCode': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Subject Code'}),
            'meetupType': forms.Select(attrs={'class' : 'form-control'}),
            'description': forms.Textarea(attrs={'class' : 'form-control', 'placeholder' : 'Meetup description'}),
            'buildingNames': forms.Select(attrs={'class' : 'form-control'}),
            'meetupRoom': forms.TextInput(attrs={'class' : 'form-control', 'placeholder' : 'Meetup Room'}),
            'meetupStart': forms.DateInput(attrs={'class' : 'form-control'}),
            'meetupEnd': forms.DateTimeInput(attrs={'class' : 'form-control'}),
        }

       
        