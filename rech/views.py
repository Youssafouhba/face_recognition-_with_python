from django.shortcuts import render,redirect

# Create your views here.
def rech(request):

                        
                    def inf(f):

                        import pickle

                        a=[]
                        d=[]
          
                        file = open(f, 'rb')

                        d=pickle.load(file)

                        file.close()
                        
                        for i in range(1,len(d)):
                               
                               a.append(d[i])
                        
                        fil = open(f, 'wb')
                  
                        pickle.dump(a, fil)

                        fil.close()
                                
                    inf("nom")
                    inf("prenom")
                    inf("tel")
                    inf("adresse")

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

                    return redirect('/medecin')