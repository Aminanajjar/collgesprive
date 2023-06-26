from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.views import View
from accounts.models import Etudiant
from django.contrib import messages
from application.forms import EditResultForm
#from ressources.models import Matiere, StudentResult
class EditResultViewClass(View):
    def get(self,request,*args,**kwargs):
        enseignant_id=request.user.id
        edit_result_form = EditResultForm(enseignant_id=request.user.id)
        return render(request,"Enseignants/edit_student_result.html",{"form":edit_result_form})

    def post(self,request,*args,**kwargs):
        form = EditResultForm(request.POST, enseignant_id=request.user.id)
        if form.is_valid():
            etudiant = form.cleaned_data['etudiant']
            matiere_assignment_marks = form.cleaned_data['matiere_assignment_marks']
            matiere_exam_marks = form.cleaned_data['matiere_exam_marks']
            matiere_id = form.cleaned_data['matiere_id']

           # etudiant_obj = Etudiant.objects.get()
           # matiere_obj = Matiere.objects.all()
           # result=StudentResult.objects.get(matiere_id=matiere_obj,etudiant_id=etudiant_obj)
            #result.matiere_assignment_marks=matiere_assignment_marks
            #result.matiere_exam_marks=matiere_exam_marks
           # result.save()
            messages.success(request, "Successfully Updated Result")
            return HttpResponseRedirect(reverse("edit_student_result"))
        else:
            messages.error(request, "Failed to Update Result")
            form=EditResultForm(request.POST,staff_id=request.user.id)
            return render(request,"Enseignants/edit_student_result.html",{"form":form})
