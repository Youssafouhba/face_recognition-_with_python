from django.shortcuts import render,redirect
from django.http import HttpResponse
from .classe_assistant import insertion_assistante ,modification_assistante,suppression_assistante
from .classe_medecin import insertion_medcin ,modification_medcin,suppression_medcin


# Create your views here.

def home(request):
     
     return render(request,'login.html')


def login(request):
          
          request.session['s']=False

          Email=request.POST['Email']

          password=request.POST['password']
          
          if Email=="docteur@gmail.com" and password=='123':
               
               request.session['stat']= 'doctor'

               return redirect('/medecin')
               

          elif Email=="assistant@gmail.com" and password=='123':
               
                    request.session['stat']= 'assistant'

                    request.session['s']=True
               
                    return redirect('/sec')
                    
          else:

               return redirect('/')
     
def modification(request):
     champ = request.POST['champ']
     nvdonnee = request.POST['nvdonnee']
     idPatient = request.POST['idPatient']

     if request.session['stat'] == 'assistant':
          modification_assistante(champ,nvdonnee,idPatient)
     if request.session['stat'] == 'doctor':
          modification_medcin(champ,nvdonnee,idPatient)
     


def suppression(request):
     idPatient = request.POST['idPatient']
     idconsultation = request.POST['idconsultation']
     if request.session['stat'] == 'assistant': 
          suppression_assistante(idPatient)
     if request.session['stat'] == 'doctor':
          suppression_medcin(idconsultation)