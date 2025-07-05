import pandas as pd
from datetime import datetime
import re

def valider_email(col_email):

   chaine =r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'

   validites_mail= col_email.apply(lambda x: 1 if re.match(chaine, str(x)) else 0)
   taux_validite_email = validites_mail.sum() / len(col_email) * 100
   return taux_validite_email

def coherence_age(date_naissance) :
    
   date_ref=datetime.today().date()
  # date_naissance = pd.to_datetime(date_naissance, errors='coerce')
   date_naissance = pd.to_datetime(date_naissance, dayfirst=True, errors='coerce')


   age = (date_ref - date_naissance.dt.date).apply(lambda x: x.days // 365)
   age_coherence = age.apply(lambda age: 1 if ( age > 5 and age <100 )   else 0)
   taux_coherence_age = age_coherence.sum() / len(date_naissance) * 100
   return taux_coherence_age

def valider_phone(phone) :

   pattern_telephone = r'^\+\d{6,15}$'  
   phone_valide= phone.apply(lambda phone: 1 if re.match(pattern_telephone, str(phone)) else 0)
   taux_validite_phone = phone_valide.sum() / len(phone) * 100
   return taux_validite_phone

#phones = pd.Series(['+33612345678', '+33612345679', '+33612345678', '+33612345638'])
#valider_phone(phones)

def coherence_pays(pays) :

  pays_coherence= pays.apply(lambda pays: 1 if str(pays).upper()=='FRANCE' or str(pays).upper()=='USA'  else 0)
  taux_coherence_pays = pays_coherence.sum() / len(pays) * 100
  return taux_coherence_pays

pays = pd.Series(['USA', 'FRANCE', 'FRANCE', 'US'])

def unique(col) :
  lig=col.nunique()
  taux_unicite = (lig / len(col)) * 100
  return taux_unicite

def add( a ,b) :
    return a+b

def completude(col): 
    col_clean = col.replace('', pd.NA)
    null_counts = col_clean.isnull().sum()
    Taux_de_Completude= (1 - (null_counts / len(col))) * 100
    return Taux_de_Completude 

def analyser_dataframe(df):
    resultat = []
    for col in df.columns:
        if col == 'pays':
            Taux_Cohrence = coherence_pays(df[col])
        elif col == 'date_naissance':
            Taux_Cohrence = coherence_age(df[col])
        else:
            Taux_Cohrence = 0

        if col == 'email':
            Taux_validaty = valider_email(df[col])
        elif col == 'telephone':
            Taux_validaty = valider_phone(df[col])
        else:
            Taux_validaty = 0

        taux_comp = completude(df[col])
        taux_uni = unique(df[col])

        resultat.append({
            'colonne': col,
            'taux_completude (%)': round(taux_comp, 2),
            'taux_unicite (%)': round(taux_uni, 2),
            'Taux_validaty(%)': round(Taux_validaty, 2),
            'Taux_Cohrence(%)': round(Taux_Cohrence, 2)
        })

    return pd.DataFrame(resultat) 

df=pd.read_csv(r"C:\Users\user\Projets_data\Pipeline_data_quality\Client_Data_Sample.csv" ,sep=';', dtype={'telephone': str})


if __name__ == "__main__":
    df = pd.read_csv("Client_Data_Sample.csv", sep=';', dtype={'telephone': str})
    print(analyser_dataframe(df))




