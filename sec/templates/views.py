from django.shortcuts import render,redirect

from django.http import HttpResponse


def recherche(request):

      import sqlite3

      recherche=request.POST['search']

      if recherche!='':

            conn = sqlite3.connect('db.sqlite3')

            cur=conn.cursor()

            search=recherche.split()

            if len(search) == 1:

                  return redirect('/sec')
            
            req="SELECT * FROM patient,consultation where nom='{}' AND prenom='{}' AND id_patient=patient_consulte ".format(search[0],search[1])

            resultat =cur.execute(req)

            result = cur.fetchone()

            if result is not None:

                  return render(request, 'affichage.html', {'nom': result[1], 'prenom': result[2] , 'tel': result[3], 'naissance':result[4], 'tel': result[5] ,'adresse': result[6] ,'date_consultation': result[8], 'maladie': result[9], 'traitement': result[10], 'diagnostic': result[11]  })

            else: return redirect('/sec')
      
      else: return redirect('/sec')

def sec(request):
     
     if request.session['s']== True :
            
            request.session['prenom']=[]
    
            request.session['nom']=[]

            request.session['cin']=[]

            request.session['tel']=[]

            request.session['adresse']=[]

            
            def get(f):
          
                  import pickle

                  file = open(f, 'rb')

                  data=pickle.load(file)

                  file.close()

                  return data
                
            request.session['nom']=get("nom")

            request.session['prenom']=get("prenom")

            #request.session['cin'].append(j[3])

            request.session['tel']=get("tel")

            request.session['adresse']=get("adresse")

            return render(request, 'python.html', {'nom': request.session['nom'], 'prenom': request.session['prenom'],'tel': request.session['tel'],'adresse': request.session['adresse'],})
            
     else: return redirect('/authentification')
