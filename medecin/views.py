from django.shortcuts import redirect, render
from django.http import HttpResponse

def medecin(request):
    
    import sqlite3

    conn = sqlite3.connect('db.sqlite3')

    cur=conn.cursor()

    requete="select * from patient,consultation where diagnostic is NULL  AND id_patient=patient_consulte "

    res=cur.execute(requete)

    result = cur.fetchone()

    if result is not None:

        request.session['id']=result[8]

        return render(request, 'med.html', {'nom': result[1], 'prenom': result[2] , 'cin': result[3], 'consultation':result[9],'maladie': result[10],'taritement': result[11],'description': result[12]})
    
    else:

        return render(request, 'med.html',{'err': "aucun patient dans la salle d'attente"})
    


def suivant(request):
    
    import sqlite3

    conn = sqlite3.connect('db.sqlite3')

    cur=conn.cursor()

    request.session['id']=request.session['id']+1

    requete="select * from patient,consultation where id_consultation={}  AND id_patient=patient_consulte ".format(request.session['id'])

    res=cur.execute(requete)

    result = cur.fetchone()
    
    if result is not None:

        return render(request, 'med.html', {'nom': result[1], 'prenom': result[2] , 'cin': result[3], 'consultation':result[9],'maladie': result[10],'taritement': result[11],'description': result[12]})
    
    else:
        return redirect('/medecin')
    
def deconnect(request):

    return redirect("../")

    import sqlite3

    conn = sqlite3.connect('db.sqlite3')

    cur=conn.cursor()
        
    requete="delete from consultation where diagnostic is NULL"

    res=cur.execute(requete)

    conn.commit()
    
    def inf(f):

        import pickle

        a=[]
          
        fil = open(f, 'wb')
                  
        pickle.dump(a, fil)

        fil.close()
    inf("nom")
    inf("prenom")
    inf("tel")
    inf("adresse")

    request.session['prenom']=[]
    
    request.session['nom']=[]

    request.session['tel']=[]

    request.session['adresse']=[]


