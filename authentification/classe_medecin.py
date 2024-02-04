def insertion_medcin(date_Consultation,Type_maladie,Traitement,Diagnostic,patient_consulte):
        import sqlite3
        conn=sqlite3.connect('db.sqlite3')
        cur=conn.cursor()
        req="insert into consultation (date_consultation,type_maladie,traitement,diagnostic,patient_consulte) values (?,?,?,?,?)"
        cur.execute(req,(date_Consultation,Type_maladie,Traitement,Diagnostic,patient_consulte))
        conn.commit()
        conn.close()



def modification_medcin(champ,nvdonnee,id):
        import sqlite3
        conn=sqlite3.connect('db.sqlite3')
        cur=conn.cursor()
        req="UPDATE consultation SET ?=? WHERE id_patient=?"
        cur.execute(req,(champ,nvdonnee,id))
        conn.commit()
        conn.close()



def suppression_medcin(idconsultation):
        import sqlite3
        conn=sqlite3.connect('db.sqlite3')
        cur=conn.cursor()
        req="delete from consultation WHERE id_consultation = ?"
        cur.execute(req,(idconsultation))
        conn.commit()
        conn.close()      