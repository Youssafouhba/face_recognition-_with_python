def recuperation() :
        import sqlite3
        conn = sqlite3.connect('db.sqlite3')
        cur=conn.cursor()
        req="select * from patient"
        result=cur.execute(req)
        resultt=result.fetchall()
        for row in resultt :
            print("les donnees de patient")
            print("id :",row[0])
            print("Nom :",row[1])
            print("prenom :",row[2])
            print("CIN :",row[3])
            print("date de naissance :",row[4])
            print("Tel :",row[5])
            print("Adresse :",row[6])
            print("photo :",row[7])
            print("ses consultations")

            requete="select * from consultation,patient where id_patient=patient_consulte"
            res=cur.execute(requete)
            
            for ligne in res :
                    print("id :",ligne[0])
                    print("date_consultation :",ligne[1])
                    print("type_maladie :",ligne[2])
                    print("traitement :",ligne[3])
                    print("diagnostic :",ligne[4])
                    print("+++++++++++++")
            print("----------------")
