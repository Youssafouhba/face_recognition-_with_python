from django.shortcuts import render,redirect

from django.http import HttpResponse

from authentification.views import login

from .classe_user import recuperation


# Create your views here.

def recherche(request):

      import sqlite3

      recherche=request.POST['search']

      conn = sqlite3.connect('db.sqlite3')

      cur=conn.cursor()

      search=recherche.split()

      req="SELECT * FROM patient,consultation where nom='{}' AND prenom='{}' AND id_patient=patient_consulte ".format(search[0],search[1])

      resultat=cur.execute(req)

      result = cur.fetchone()

      nom=result[0]
      
      return render(request, 'resultat_recherche.html', {'nom': result[1], 'prenom': result[2] , 'cin': result[3], 'naissance':result[4], 'tel': result[5] })


def recherche_detect(request):
    
    import sqlite3

    conn = sqlite3.connect('db.sqlite3')

    cur=conn.cursor()

    rb=cur.execute("select id_patient from patient where cin=?",(request.session['cinid'],))

    request.session['id']= rb.fetchone()
                    
    requezte="insert into consultation(patient_consulte) values (?)"

    ress=cur.execute(requezte,request.session['id'])

    conn.commit()

    return redirect('./liste_attente')


def liste_attente(request):

      def inf(data,f):

        import pickle

        a=[]

        requete="select * from patient,consultation where diagnostic is NULL AND id_patient=patient_consulte "

        res=cur.execute(requete)

        result = cur.fetchone()

        if result is not None:
          
            file = open(f, 'rb')

            a = pickle.load(file)

            file.close()
        else:

            pickle.load(file)

            file.close()

        a.append(data)
          
        fil = open(f, 'wb')
                  
        pickle.dump(a, fil)

        fil.close()

      def get(f):
          
          import pickle

          file = open(f, 'rb')

          data=pickle.load(file)

          file.close()

          return data

      
      request.session['prenom']=[]
    
      request.session['nom']=[]

      request.session['cin']=[]

      request.session['tel']=[]

      request.session['adresse']=[]
      
      import sqlite3

      conn = sqlite3.connect('db.sqlite3')

      cur=conn.cursor()

      requete="select nom,prenom,tel,adresse from patient,consultation where diagnostic is NULL AND patient_consulte = ? AND id_patient=patient_consulte "

      res=cur.execute(requete,request.session['id'])

      result = cur.fetchall()

      if result is not None:
        
        for j in result:
            nom = j[0]
            prenom = j[1]
            tel = j[2]
            adresse = j[3]

        inf(nom,"nom")
        inf(prenom,"prenom")
        inf(tel,"tel")
        inf(adresse,"adresse")
           
        request.session['nom']=get("nom")

        request.session['prenom']=get("prenom")

            #request.session['cin'].append(j[3])

        request.session['tel']=get("tel")

        request.session['adresse']=get("adresse")
           
        return render(request, 'python.html', {'nom': request.session['nom'], 'prenom': request.session['prenom'],'tel': request.session['tel'],'adresse': request.session['adresse'],})
    
      else:

        return render(request, 'python.html',{'nom': [], 'prenom': [], 'cin': [], 'tel': [],'adresse': [],})
    
    
