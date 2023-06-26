
from asyncio.windows_events import NULL
from django.db import IntegrityError
from django.db.models import Sum
from django .utils import timezone 

import datetime
import json
from telnetlib import LOGOUT
from django.forms import modelformset_factory
from django.urls import reverse
from  django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils. encoding import force_bytes, force_text 
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from accounts.models import Enseignant, Etudiant

from django.core import serializers
from contact.forms import CommentaireForm
from contact.models import CommentaireEtudiant

from projet import settings
import email
from email import message
from math import fmod
from operator import itemgetter       
import MySQLdb

from django.contrib import messages
from django.http import  HttpResponseForbidden, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from django.contrib.auth.decorators import login_required
from ressources.forms import CoursForm



from ressources.models import DAYS_OF_WEEK,  Classe, Cours, Emplois,  Matiere, Presence, Seance,time_slots
from resultat.models import Results



from .forms import ContactForm, EditResultForm

from django.contrib.auth.models import User , auth
from django.contrib.auth import authenticate,login
import os
from django.contrib.auth.forms import UserCreationForm

from django.core.mail import send_mail,EmailMessage
import socket
socket.getaddrinfo('localhost', 3306)


from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import View


from django.http import HttpResponse
# Create your views here.











def info_enseignant1(request):
    return render(request,'liste_enseignants/info_enseignant1.html')
def info_enseignant2(request):
    return render(request,'liste_enseignants/info_enseignant2.html')
def info_enseignant3(request):
    return render(request,'liste_enseignants/info_enseignant3.html')
def info_enseignant4(request):
    return render(request,'liste_enseignants/info_enseignant4.html')
def home(request):
    return render(request,'home.html')



    






def users_admin(request):
   
    return render(request,'administration/users_admin.html')






  

     

   



def mois(request):
    return render(request,'administration/mois.html')
def users(request):
    return render(request,'administration/users.html')    





def contact(request):
    if request.method=="POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/application')
    form=ContactForm
    context= {'form' : form}       
    return render(request,'contact.html', context)





import stripe
stripe.api_key = "sk_test_51NCM1eB4DSPortDLYAR5TP0aMniltF2GPoNLzaE16wip7yTH2rZbU5La7MLT4ayW603fOtVxbA4XY8ZEnsqiGaBh00yyeHhSsC"

def paiement(request):
   if request.method == "POST":
                amount = int(request.POST["amount"]) 
                #Create customer
                try:
                        customer = stripe.Customer.create(
                                       email=request.POST.get("email"),
                                       name=request.POST.get("full_name"),
                                       description="Test donation",
                                    source=request.POST['stripeToken']
                                       )

                except stripe.error.CardError as e:
                  return HttpResponse("<h1>There was an error charging your card:</h1>"+str(e))     

                except stripe.error.RateLimitError as e:
                     # handle this e, which could be stripe related, or more generic
                     return HttpResponse("<h1>Rate error!</h1>")

                except stripe.error.InvalidRequestError as e:
                  return HttpResponse("<h1>Invalid requestor!</h1>")

                except stripe.error.AuthenticationError as e:  
                  return HttpResponse("<h1>Invalid API auth!</h1>")

                except stripe.error.StripeError as e:  
                  return HttpResponse("<h1>Stripe error!</h1>")

                except Exception as e:  
                  pass  



                #Stripe charge 
                charge = stripe.Charge.create(
                       customer=customer,
                          amount=int(amount)*100,
                          currency='usd',
                          description="Test donation"
                     ) 
                transRetrive = stripe.Charge.retrieve(
                           charge["id"],
                           api_key="sk_test_51NCM1eB4DSPortDLYAR5TP0aMniltF2GPoNLzaE16wip7yTH2rZbU5La7MLT4ayW603fOtVxbA4XY8ZEnsqiGaBh00yyeHhSsC"

                        )
                charge.save() # Uses the same API Key.
                return redirect("paysuccess")

                   


   return render(request,'administration/paiement.html')


def paysuccess(request):
    return render(request, "administration/paysuccess.html")



def info(request):
    return render(request,'administration/info.html')

def physique(request):
    return render(request,'administration/physique.html')

def stv(request):
    return render(request,'administration/stv.html')        

def histoire(request):
    return render(request,'administration/histoire.html')

def mathématique(request):
    return render(request,'administration/mathématique.html')



def francais(request):
    return render(request,'administration/francais.html')

def formule(request):
    return render(request,'Etudiants/formule.html')


def cours(request):
    return render(request,'administration/courses.html')    

def classe(request):
    return render(request,'administration/classe.html')    



def register(request):

         
    return render(request,'administration/register.html')   













    

# Enseignants pages

def homepage(request):
    return render(request,'Enseignants/homepage.html')


@login_required
def edit_profile_enseignant(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        telephone = request.POST.get('telephone')
        password = request.POST.get('password')

        enseignant = get_object_or_404(Enseignant, user=request.user)

        enseignant.first_name = first_name
        enseignant.last_name = last_name
        enseignant.telephone = telephone

        if password:
            request.user.set_password(password)
            request.user.save()

        enseignant.save()

        messages.success(request, "Modification réussie")
        return redirect('enseignant')

    messages.error(request, "Erreur") 
    return redirect('enseignant')

def noteEtudiant(request):
    classes = Seance.objects.filter(enseignant_id=request.user.id).values('classe__id', 'classe__nom', 'classe__niveau').distinct()

    context = {'classes': classes}

    # Récupère le résultats_id de la requête GET
    results_id = request.GET.get('results_id')
 
    # Vérifie si le résultats_id est valide et ajoute le lien d'ajout de notes dans le contexte
   

    return render(request, 'Enseignants/noteEtudiant.html', context)
def ajouter_note(request):
     
    
       
     return render(request, 'Enseignants/ajouter_note.html')


def liste_seance(request,classe_id):
    
    seances = Seance.objects.filter(enseignant_id=request.user.id, classe_id=classe_id)
    
    context = {
        
        'seances':seances,
    }
    return render(request, 'Enseignants/liste_seance.html',context)






def absence(request):
    return render(request,'Enseignants/absence.html')



#resultat

@login_required
def liste_etudiants(request):
    enseignant = request.user.enseignant
    matieres = enseignant.matiere.all()
    context = {'matieres': matieres}
    return render(request, 'Enseignants/liste_etudiants.html', context)





def presence_classe(request):
   


    classes = Seance.objects.filter(enseignant_id=request.user.id).values('classe__id','classe__nom','classe__niveau').distinct()
    
   

    return render(request, 'Enseignants/presence_classe.html',{'classes':classes})



def uplode_cours (request):
        cours= Cours.objects.filter(enseignant_id=request.user.id)
        return render(request,'Enseignants/uplode_cours.html',{'cours':cours})



def liste_matieres (request):
        matieres= Matiere.objects.all()
        etudiant=  request.user.etudiant
        if etudiant.niveau=='7ème':
         i=7
        elif etudiant.niveau=='8ème':
         i=8
        elif etudiant.niveau=='9ème':
         i=9
        return render(request,'Etudiants/liste_matieres.html',{'matieres':matieres,'i':i,'etudiant':etudiant})       



def notification (request):
        
      
        return render(request,'Enseignants/notification.html')        





def delete_cours(request, pk):
    if request.method =='POST':
        cours=get_object_or_404(Cours , pk=pk)
        cours.delete()
        messages.success(request,"cours est supprimée")
        return redirect('uplode_cours')
    else:
        return redirect('uplode_cours')


def calenda(request):
    try:
        enseignant = Enseignant.objects.get(user=request.user)
    except Enseignant.DoesNotExist:
        enseignant = Enseignant.objects.create(user=request.user)

    matiere = enseignant.matiere
    asst = Emplois.objects.filter(seance__matiere=matiere)
    matrix = [['' for i in range(10)] for j in range(6)]  

    for i, d in enumerate(DAYS_OF_WEEK):
        t = 0
        for j in range(10):  
            if j == 0:
                matrix[i][0] = d[0]
                continue
            if j == 4 or j == 8:
                continue
            try:
                a = asst.get(periode=time_slots[t][0], jour=d[0])
                matrix[i][j] = {
                    'matiere': a.seance.matiere.titre,
                    'salle': a.seance.salle,
                    'classe': a.seance.classe
                }
            except Emplois.DoesNotExist:
                pass
            t += 1
            if t >= len(time_slots):
                break

    context = {'matrix': matrix}
    return render(request, 'Enseignants/calenda.html', context)


def calenda_enseignant(request,asst_id):
    asst=get_object_or_404(Emplois,id=asst_id)
    lt_list=[]
    t_list= Enseignant.objects.filter(seance__classe_titre=asst.seance.classe_titre)
    for t in t_list:
        at_list=Emplois.objects.filter(seance__enseignant=t)
        if not any([True if at.periode == asst.periode and at.jour == asst.jour else False for at in at_list]):
            lt_list.append(t)
    return render(request,'Enseignants/calenda_enseignant.html',{'lt_list':lt_list})


def ajouter_matiere (request):
   
    cours = Cours.objects.all()
 

    return render(request,'Enseignants/ajouter_matiere.html',{'cours': cours})



def presence(request, classe_id):
   
   
    return render(request, 'Enseignants/presence.html')
from django.utils.html import strip_tags

def presence_action(request, seance_id, etudiant_id):
    presence, created = Presence.objects.get_or_create(etudiant_id=etudiant_id, seance_id=seance_id)
    presence.etat = 'present'
    presence.save()
    return redirect('/extraclasse/' + str(seance_id))

def absent_action(request, seance_id, etudiant_id):
    presence, created = Presence.objects.get_or_create(etudiant_id=etudiant_id, seance_id=seance_id)
    presence.etat = 'absent'
    presence.save()
    return redirect('/extraclasse/' + str(seance_id))
from django.db.models import Prefetch

def extraclasse(request, seance_id):
    classe = Seance.objects.filter(id=seance_id).get()

    # Récupérer les étudiants distincts de la classe avec leurs présences
    etudiants = Etudiant.objects.filter(classe_id=classe.classe_id).distinct().prefetch_related(
        Prefetch('presence_set', queryset=Presence.objects.filter(seance_id=seance_id), to_attr='presences')
    )

    context = {
        'etudiants': etudiants,
        'seance_id': seance_id
    }

    return render(request, 'Enseignants/extraclasse.html', context)
def enseignant_ajout_resultat(request):
    matieres = Matiere.objects.all()
   
    return render(request,'Enseignants/enseignant_ajout_resultat.html',{"matieres":matieres})



def liste_note(request, classe_id):

    etudiants=Etudiant.objects.filter(classe_id=classe_id).all()
    
   
    return render(request,'Enseignants/liste_note.html',{'etudiants': etudiants})











from django.db.models import F, Value, IntegerField
from django.db.models.functions import Coalesce

class ResultListView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        etudiant_id = request.POST.get('etudiant_id')
        classe_id = request.POST.get('classe_id')
        matiere_id = request.POST.get('matiere_id')
        test = request.POST.get('test')
        examen = request.POST.get('examen')

        if not etudiant_id:
            messages.error(request, 'L\'étudiant doit être spécifié')
            return redirect('view-resultat')

        try:
            etudiant_id = int(etudiant_id)
        except ValueError:
            messages.error(request, 'ID d\'étudiant non valide')
            return redirect('view-resultat')

        try:
            etudiant = Etudiant.objects.get(id=etudiant_id)
        except Etudiant.DoesNotExist:
            messages.error(request, 'L\'étudiant spécifié n\'existe pas')
            return redirect('view-resultat')

        classe = Classe.objects.get(id=classe_id)
        matiere = Matiere.objects.get(id=matiere_id)

       

        messages.success(request, 'Résultat enregistré avec succès.')
        return redirect('view-resultat')

   
    def get(self, request, *args, **kwargs):
        # Get the student object using the id from the URL
        etudiant = Etudiant.objects.get(id=kwargs['id'])
        
        # Get all the results for the student and annotate them with the total score
      

        return render(request, 'Enseignants/result_list.html', )





def result_list(request, classe_id):
   results=Results.objects.filter(etudiant__classe_id=classe_id)
   enseignant=request.user.enseignant
   matiere=enseignant.matiere.titre
   context={
       'results':results,
       'matiere':matiere
   }
   return render(request, 'Enseignants/result_list.html',context)





   
   

def get_etudiant(request, id):
    etudiants = Etudiant.objects.all()
    enseignant = Enseignant.objects.get(user=request.user)
    context = {
        'etudiants': etudiants,
        'enseignant': enseignant
    }
    return render(request, 'enseignant_ajout_resultat.html',context)




from django.forms import modelformset_factory

def edit_action(request,etudiant_id,classe_id):
    etudiant = Etudiant.objects.get(user_id=etudiant_id)
    enseignant=request.user.enseignant.user_id
    if request.method == 'POST':
        orale = request.POST.get('orale')
        note_de_controle = request.POST.get('note_de_controle')
        note_de_examen = request.POST.get('note_de_examen')
        evaluation = request.POST.get('evaluation')
        total = (float(note_de_examen)*2+float(note_de_controle)+float(orale))/4

      
      
        
        
        r=Results.objects.create(orale=orale,note_de_controle=note_de_controle,note_de_examen=note_de_examen,total=total,evaluation=evaluation,enseignant_id=enseignant,etudiant_id=etudiant.user_id)

            
        messages.success(request, "Notes enregistrées avec succès")
    return redirect('result_list', classe_id=classe_id)
   


def edit_action_2(request,etudiant_id,classe_id):
    etudiant = Etudiant.objects.get(user_id=etudiant_id)  
    enseignant=request.user.enseignant.user_id
    
    orale = request.get('orale')
    note_de_controle = request.get('note_de_controle')
    note_de_examen = request.get('note_de_examen')
    evaluation = request.get('evaluation')
    total = (float(note_de_examen)*2+float(note_de_controle)+float(orale))/4

 
    r=Results.objects.get(enseignant_id=enseignant,etudiant_id=etudiant.user_id)
    r1=Results(id=r.id,orale=orale,note_de_controle=note_de_controle,note_de_examen=note_de_examen,total=total,evaluation=evaluation,enseignant_id=r.enseignant_id,etudiant_id=r.etudiant_id)
         
           
    r1.save_base()


      
         
    messages.success(request, "Notes enregistrées avec succès")
    return redirect('result_list', classe_id=classe_id)
  

def edit_student_result(request,etudiant_id,classe_id):
    enseignant=request.user.enseignant.user_id
   
    result=Results.objects.get_or_create(etudiant_id=etudiant_id,enseignant_id=enseignant)
    etudiant = Etudiant.objects.get(user_id=etudiant_id)
    
    if request.method == "POST":
        orale = request.POST.get('orale')
        note_de_controle = request.POST.get('note_de_controle')
        note_de_examen = request.POST.get('note_de_examen')
        evaluation = request.POST.get('evaluation')
        total = (float(note_de_examen)*2+float(note_de_controle)+float(orale))/4

 
        r=Results.objects.get(enseignant_id=enseignant,etudiant_id=etudiant.user_id)
        r1=Results(id=r.id,orale=orale,note_de_controle=note_de_controle,note_de_examen=note_de_examen,total=total,evaluation=evaluation,enseignant_id=r.enseignant_id,etudiant_id=r.etudiant_id)
         
           
        r1.save_base()


      
         
        messages.success(request, "Notes enregistrées avec succès")
        return redirect('result_list', classe_id=classe_id)
    return render(request, 'Enseignants/edit_student_result.html',{'result':result,'etudiant_id':etudiant_id,'classe_id':classe_id})



def save_student_result(request, etudiant_id):
   
    return redirect('edit_student_result')

def delete_student_result(request, etudiant_id):
    
    
    return redirect('edit_student_result')



#Etudiants page

def homepageeleve(request):
    
    return render(request,'Etudiants/homepageeleve.html')

def liste_matière(request):
    matieres = Matiere.objects.all()
    etudiant=request.user.etudiant
    return render(request,'Etudiants/liste_matière.html', {'matieres': matieres,'etudiant': etudiant})




def Commentaires_des_etudiants(request,cours_id):
    etudiant = Etudiant.objects.all()
    comments = CommentaireEtudiant.objects.filter(cours_id=cours_id).order_by('date')
    form = CommentaireForm()
    context = {'commentaires': comments, 'etudiant_obj': etudiant, 'form': form, 'cours_id':cours_id}
    return render(request, 'Etudiants/Commentaires_des_etudiants.html', context)


def student_feedback_save(request, cours_id):
    if request.method == "POST":
        form = CommentaireForm(request.POST)
        if form.is_valid():
            etudiant = request.user.etudiant
            cours = Cours.objects.get(id=cours_id)
            if etudiant and cours:
                form.instance.etudiant = etudiant
                form.instance.enseignant=None
                form.instance.cours = cours
                form.instance.commentaire = form.cleaned_data['commentaire'] 
                
                form.save()
                messages.success(request, "Commentaire envoyé.")
            else:
                messages.error(request, "Erreur lors de l'enregistrement du commentaire.")
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
    return redirect('Commentaires_des_etudiants', cours_id=cours_id)



def Commentaires_des_enseignants(request,cours_id):
    etudiant = Etudiant.objects.all()
    comments = CommentaireEtudiant.objects.filter(cours_id=cours_id).order_by('date')
    form = CommentaireForm()
    context = {'commentaires': comments, 'etudiant_obj': etudiant, 'form': form, 'cours_id':cours_id}
    return render(request, 'Enseignants/Commentaires_des_enseignants.html', context)


def teacher_feedback_save(request, cours_id):
    if request.method == "POST":
        form = CommentaireForm(request.POST)
        if form.is_valid():
            enseignant = request.user.enseignant
            cours = Cours.objects.get(id=cours_id)
            if enseignant and cours:
                form.instance.enseignant = enseignant
                form.instance.etudiant=None
                form.instance.cours = cours
                form.instance.commentaire = form.cleaned_data['commentaire'] 
                
                form.save()
                messages.success(request, "Commentaire envoyé.")
            else:
                messages.error(request, "Erreur lors de l'enregistrement du commentaire.")
        else:
            messages.error(request, "Veuillez corriger les erreurs ci-dessous.")
    return redirect('Commentaires_des_enseignants', cours_id=cours_id)



   
def calendar(request):
    try:
        etudiant = Etudiant.objects.get(user=request.user)
    except Etudiant.DoesNotExist:
        
        etudiant = Etudiant.objects.create(user=request.user)
    classe = etudiant.classe
    asst = Emplois.objects.filter(seance__classe=classe)
    matrix = [['' for i in range(10)] for j in range(6)]
    for i, d in enumerate(DAYS_OF_WEEK):
        t = 0
        for j in range(10):  
            if j == 0:
                matrix[i][0] = d[0]
                continue
            if j == 4 or j == 8:
                continue
            try:
                a = asst.get(periode=time_slots[t][0], jour=d[0])
                matrix[i][j] = {
                    'matiere': a.seance.matiere.titre,
                    'salle': a.seance.salle,
                    'classe': a.seance.classe
                }
            except Emplois.DoesNotExist:
                pass
            t += 1
            if t >= len(time_slots):
                break

    context = {'matrix': matrix}
    return render(request, 'Etudiants/calendar.html', context)



def cours_etudiant(request,matiere_id,id):
    etudiant=request.user.etudiant
    if id == 7 :
        niveau='7ème'
    elif id== 8 :
        niveau='8ème'
    elif id== 9:
        niveau='9ème'
   
    cours= Cours.objects.filter(enseignant__matiere_id=matiere_id, niveau=niveau)

    return render(request,'Etudiants/cours_etudiant.html', {'cours': cours})

def notes(request):
   etudiant=request.user.etudiant.user_id
   results=Results.objects.filter(etudiant_id=etudiant)

   context={
       'results':results
   }
   return render(request,'Etudiants/notes.html',context)

def absenceEleve(request): 
        etud=Etudiant.objects.get(user_id=request.user.id)
    
        presences=Presence.objects.filter(etudiant_id=etud)
       
        context={
            'presences':presences,
          
        }
        return render(request,'Etudiants/absenceEleve.html',context)





@login_required
def edit_profile(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        Adresse = request.POST.get('Adresse')
        password = request.POST.get('password')

        etudiant = get_object_or_404(Etudiant, user=request.user)

        etudiant.first_name = first_name
        etudiant.last_name = last_name
        etudiant.Adresse = Adresse

        if password:
            request.user.set_password(password)
            request.user.save()

        etudiant.save()

        messages.success(request, "Modification réussie")
        return redirect('etudiant')

    messages.error(request, "Erreur") 
    return redirect('etudiant')










    



def ajouter_presence(request): 
        
    return render(request,'Enseignants/ajouter_presence.html')