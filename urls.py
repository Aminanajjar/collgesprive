from django import views
from django.urls import include, path
from.views import *
from application import views
from.views import ResultListView

urlpatterns = [


 #ETUDIANT
    path('Commentaires_des_enseignants/<int:cours_id>',Commentaires_des_enseignants,name="Commentaires_des_enseignants"),
    path('teacher_feedback_save/<int:cours_id>',teacher_feedback_save, name='teacher_feedback_save'),
    path('student_feedback_save/<int:cours_id>',student_feedback_save, name='student_feedback_save'),
    path('liste_matière',liste_matière, name='liste_matière'),
    path('liste_note/<int:classe_id>',liste_note, name='liste_note'),
    


  
   
    #Etudiants
    
      path('notes',notes,name="notes"),
      
      path('absenceEleve',absenceEleve,name="absenceEleve"),
      path('calendar/',calendar,name="calendar"),
      path('Commentaires_des_etudiants/<int:cours_id>',Commentaires_des_etudiants,name="Commentaires_des_etudiants"),
      
      path('liste_etudiants/', liste_etudiants, name='liste_etudiants'),
      path('edit_profile/', edit_profile, name='edit_profile'),
      path('homepageeleve',homepageeleve,name="homepageeleve"),
      path('cours_etudiant/<int:matiere_id>/<int:id>/',cours_etudiant,name="cours_etudiant"),

      
      
  
  
  #Enseignant 
  path('ajouter_presence/',ajouter_presence,name="ajouter_presence"),
  #path('notification/',notification,name="notification"),

  path('edit_student_result/<int:etudiant_id>/<int:classe_id>/',edit_student_result, name='edit_student_result'),
  path('edit_action/<int:etudiant_id>/<int:classe_id>/',edit_action, name='edit_action'),
  path('edit_action_2/<int:etudiant_id>/<int:classe_id>/',edit_action_2, name='edit_action_2'),
  path('get_etudiant_list/', get_etudiant, name='get_etudiant_list'),
  path('noteEtudiant/',noteEtudiant,name="noteEtudiant"),
  path('ajouter_note/',ajouter_note,name="ajouter_note"),
 path('liste_matieres/',liste_matieres,name="liste_matieres"),
  path('presence_classe/', presence_classe, name='presence_classe'),
  path('presence/<int:classe_id>/', presence, name='presence'),
  path('presence_action/<int:seance_id>/<int:etudiant_id>/', presence_action, name='presence_action'),
  path('absent_action/<int:seance_id>/<int:etudiant_id>/', absent_action, name='absent_action'),
  path('extraclasse/<int:seance_id>/',extraclasse, name='extraclasse'),
  #path('exist_present/<int:seance_id>/<int:etudiant_id>',exist_present, name='exist_present'),
  path('liste_seance/<int:classe_id>/', liste_seance, name='liste_seance'),


  path('calenda',calenda,name="calenda"),
 
  path('ajouter_matiere',ajouter_matiere,name="ajouter_matiere"),
 
  path('enseignant_ajout_resultat',enseignant_ajout_resultat,name="enseignant_ajout_resultat"),
  path('view/save',ResultListView.as_view(),name="view-resultat"),
  path('result_list/<int:classe_id>/', result_list, name='result_list'),
  path('homepage',homepage,name="homepage"),
  path('edit_profile_enseignant',edit_profile_enseignant,name="edit_profile_enseignant"),

  path('<int:asst_id>/calenda_enseignant/', calenda_enseignant, name="calenda_enseignant"),
  path('uplode_cours',uplode_cours,name="uplode_cours"),
  path('delete_cours/<int:pk>/',delete_cours,name="delete_cours"),
 

# base.html
    path('',home,name="home"),
    path('classe',views.classe,name="classe"),
    path('paiement',views.paiement,name="paiement"), 
    path('paysuccess',views.paysuccess,name="paysuccess"), 
    path('formule',views.formule,name="formule"),
 
    
    path('info_enseignant1',views.info_enseignant1,name="info_enseignant1"),
    path('info_enseignant2',views.info_enseignant2,name="info_enseignant2"), 
    path('info_enseignant3',views.info_enseignant3,name="info_enseignant3"),   
    path('info_enseignant4',views.info_enseignant4,name="info_enseignant4"),         
    path('stv',views.stv,name="stv"), 
   
  
    path('physique',views.physique,name="physique"),
    path('info',views.info,name="info"),
    path('contact',views.contact,name="contact"),    
    path('mois',views.mois,name="mois"),   
    path('users',views.users,name="users"),  
    
    path('francais',views.francais,name="francais"),
 
    path('mathématique',views.mathématique,name="mathématique"), 
    path('cours',views.cours,name="cours"),
    path('histoire',views.histoire,name="histoire"), 
   

    
   
 

    #path('deconnection',views.deconnection,name="deconnection"),

   

    #path('login',views.logIn,name="login"),
    path('users_admin',users_admin,name="users_admin"),
   
    path('register',register,name="register"),
 
   
 
  
]