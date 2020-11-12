from django import forms
from .models import Staff

class StaffForm(forms.ModelForm):
    
    class Meta:
        model = Staff
        fields = ('staff_id','fullname','contact_no','address')
        labels = {
            'staff_id':'Staff ID',
            'fullname':'Full Name',
            'contact_no':'Contact No.',
        }

        
