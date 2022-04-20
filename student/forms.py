from dataclasses import field
from django import forms
from .models import Student

class StudentForm(forms.Form):
    class Meta:
        model = Student
        fields = '__all__'
    
    name = forms.CharField(max_length=100)
    nrc = forms.CharField(max_length=100)
    dob = forms.DateField()
    phone = forms.CharField(max_length=20)
    contact = forms.ChoiceField(choices=(('Yangon', 'Yangon'), ('Mandalay', 'Mandalay')))
    
class ScoreForm(forms.Form):
    student = forms.ModelChoiceField(queryset=Student.objects.all())
    year = forms.CharField(max_length=4)
    mark = forms.IntegerField()
    remark = forms.Textarea()