

from django.core import validators
from django.forms import fields,widgets

from django import forms


from ressources.models import Cours, Matiere


from . models import Contact
from django.contrib.auth.forms import UserCreationForm





class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']
        widgets = {
            'Name' : forms.TextInput(attrs={'class':'form-control'}),
            'Email' : forms.EmailInput(attrs={'class':'form-control'}),
            'message' : forms.Textarea( attrs={'class':'form-control'}),
        }

           
        

class EditResultForm(forms.Form):
    def __init__(self, *args, **kwargs):
        self.enseignant_id = kwargs.pop('enseignant_id')
        super(EditResultForm,self).__init__(*args,**kwargs)
        subject_list=[]
        try:
            matiere=Matiere.objects.filter(enseignant_id=self.enseignant_id)
            for matiere in matiere:
                matiere_single=(matiere.id,matiere.titre)
                matiere_list.append(matiere_single)
        except:
            matiere_list=[]
        self.fields['matiere_id'].choices=matiere_list

    

    matiere_id=forms.ChoiceField(label="matiere",widget=forms.Select(attrs={"class":"form-control"}))
    
    matiere_assignment_marks=forms.CharField(label="Assignment Marks",widget=forms.TextInput(attrs={"class":"form-control"}))
    matiere_exam_marks=forms.CharField(label="Exam Marks",widget=forms.TextInput(attrs={"class":"form-control"}))