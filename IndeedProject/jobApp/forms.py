from django import forms

class jobForm(forms.Form):
    id=forms.IntegerField()
    company=forms.CharField(max_length=30)
    address=forms.CharField(max_length=50)
    email=forms.EmailField()
    phone=forms.IntegerField()
    date=forms.DateField()
