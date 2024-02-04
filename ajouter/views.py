from django.shortcuts import render,redirect
from django.http import HttpResponse
from .classe_assistant import insertion_assistante ,modification_assistante,suppression_assistante
from .classe_medecin import insertion_medcin ,modification_medcin,suppression_medcin


# Create your views here.


def ajouter(request):

    if  request.session['stat'] == 'assistant' :

        return render(request, 'ajouter.html') #formulair d4ajout de l'assistante
    
    else: return render(request, 'consult.html') #formulair d4ajout de medcin sinon

def ajout(request):

    if request.session['stat'] == 'assistant':

        nom = request.POST['nom']

        prenom = request.POST['prenom']

        cin = request.POST['cin']

        naissance = request.POST['naissance']

        tel = request.POST['tel']
    
        adresse = request.POST['adresse']

        request.session['cin'] = cin
    
        #photo = request.POST['photo']
    
        if nom != '' and prenom != '' and cin != '' and naissance != '' and tel != '' and adresse != '':

            insertion_assistante(nom,prenom,cin,naissance,tel,adresse)

            return redirect('/face')

            #return render(request, 'ajouter.html', {'a':  "Ajouté avec succés ."})
        
        else: return redirect('/ajouter')

    else:

            date_Consultation = request.POST['date_Consultation']
            
            Type_maladie = request.POST['Type_maladie']
     
            Traitement = request.POST['Traitement']
            
            Diagnostic = request.POST['Diagnostic']
        
            s = request.session['id'] 

            if date_Consultation  != '' and Type_maladie != '' and Traitement != '' and  Diagnostic != '' :
            
                if(insertion_medcin(date_Consultation,Type_maladie,Traitement,Diagnostic,s)):
            
                    return redirect('medcin')
                
                else: return redirect('rech')
                
            else: return redirect('/ajouter')