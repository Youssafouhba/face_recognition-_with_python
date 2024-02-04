import sqlite3
conn = sqlite3.connect('db.sqlite3')
cur=conn.cursor()

def insertion_assistante(nom,prenom,cin,naissance,tel,adresse):
        conn = sqlite3.connect('db.sqlite3')
        cur=conn.cursor()
        req="insert into patient(nom,prenom,cin,naissance,tel,adresse) values (?,?,?,?,?,?) "
        cur.execute(req,(nom,prenom,cin,naissance,tel,adresse,))
        conn.commit()
        conn.close()

def modification_assistante(champ,nvdonnee,idPatient):
        conn = sqlite3.connect('db.sqlite3')
        cur=conn.cursor()
        req="UPDATE patient SET "+champ+" = ? WHERE id_patient= ? "
        cur.execute(req,(nvdonnee,idPatient))
        conn.commit()
        conn.close()

def suppression_assistante(idPatient):
        conn = sqlite3.connect('db.sqlite3')
        cur=conn.cursor()
        req="delete from patient WHERE id_patient=?"
        cur.execute(req,(idPatient,)) 
        conn.commit()
        conn.close()
suppression_assistante(2)