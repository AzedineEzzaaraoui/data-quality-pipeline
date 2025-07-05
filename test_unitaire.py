import pandas as pd
from pipeline import valider_email ,valider_phone ,coherence_age , coherence_pays , add , completude
from datetime import datetime

def test_valider_email():
    emails = pd.Series(['test@gmail.com', 'a', 'user@yahoo.fr'])
    result = valider_email(emails)
    assert round(result, 2) == round((2 / 3) * 100, 2)
def test_valider_phone() :
    phone = pd.Series(['+33612345678', '+33612345679', '+33612345678', '+33612345638'])
    result = valider_phone(phone)
    assert round(result, 2) == round((4/ 4) * 100, 2)

def test_coherence_age() :
   date_naissance = pd.Series(['15/05/1990', '15/05/1990', '15/05/1990', '15/05/1990'])
   
   result = coherence_age(date_naissance)
   assert round(result, 2) == round((4/ 4) * 100, 2)

def test_coherence_pays() :
  pays = pd.Series(['USA', 'FRANCE', 'FRANCE', 'USA'])
  result = coherence_pays(pays)
  assert round(result, 2) == round((4/ 4) * 100, 2)

def  test_unique() :

    col = pd.Series(['USA', 'FRANCE', 'FRANCE', 'US'])
    result = coherence_pays(col)
    assert round(result, 2) == round((3/ 4) * 100, 2)
def test_add() :
    a=3 
    b=4 
    result=add(a,b)
   # assert result == 7
    return result

def test_completude() :
 col = pd.Series(['USA', 'FRANCE', 'FRANCE', 'FRANCE'])
 sortie=completude(col)
 assert sortie == 100



if __name__ == "__main__":
    test_valider_email()
    print("Test passed email!")
    test_valider_phone()
    print("Test passed phone!")
    test_coherence_age()
    print("Test passed age!")
    test_coherence_pays()
    print("Test passed pays!")
    test_unique()
    print("Test passed unqiue!")
    print(test_add() )
    test_completude() 
    print("Test passed completude!")
