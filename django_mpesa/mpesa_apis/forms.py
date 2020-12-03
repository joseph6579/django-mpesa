from django import forms
from django.core.exceptions import ValidationError


class MpesaForm(forms.Form):
    phone_number = forms.CharField(max_length=15, help_text="Enter Your Number in this format: 0701234567")
    amount = forms.IntegerField(max_value=100000, min_value=1)

    def clean_phone_number(self):
        data = self.cleaned_data['phone_number']
        if data[0] == "+":
            raise ValidationError("Enter Your Number in this format: 0701234567")
        elif data[0] != "0":
            raise ValidationError("Enter Your Number in this format: 0701234567")
        elif data[0]+data[1]+data[2] == "254":
            raise ValidationError("Enter Your Number in this format: 0701234567")
        else:
            phone_number = "254"+ data[1:]
        
        return phone_number