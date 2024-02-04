def insertion_medcin(date_Consultation,Type_maladie,Traitement,Diagnostic,s):
        import sqlite3
        conn=sqlite3.connect('db.sqlite3')
        cur=conn.cursor()
        req="update consultation set date_consultation = ? , type_maladie = ? , traitement = ? , diagnostic = ? where id_consultation = ?"
        cur.execute(req,(date_Consultation,Type_maladie,Traitement,Diagnostic,s))
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