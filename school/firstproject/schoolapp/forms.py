from django import forms

class NewSchoolForm(forms.Form):
    name=forms.CharField(label='Name',max_length=20)
    roll=forms.FloatField(label='Roll No.')
    standard=forms.CharField(label='Class')
    father=forms.CharField(label='Fathers Name')
