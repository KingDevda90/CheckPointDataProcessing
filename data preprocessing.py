#!/usr/bin/env python
# coding: utf-8

# In[36]:


import pandas as pd
#1.Importer les donnees et afficher les dix premiers lignes
client_0_bills = pd.read_csv("/Users/mac/Desktop/GoMyCode/STEG_BILLING_HISTORY.csv")


# In[37]:


print(client_0_bills.head(10))


# In[38]:


#2.Les types de variable:
client_0_bills.info()


# In[39]:


#.3 Afficher les informations generales du jeu de donnees.
#Nombre de lignes : 4476749 lignes
#Nombre de colonnes : 16 colonnes.
#Nombre de caracteristique categoricielle : 4
#Il consomme 546.5+ MB espace memoire.


# In[40]:


#4.Inspectez l’ensemble de données pour détecter d’éventuelles valeurs manquantes.
client_0_bills.isnull().sum()
# Le nombre total est 4579.


# In[41]:


#5.Sélectionnez votre stratégie pour gérer les valeurs manquantes et dites-nous pourquoi vous avez fait ce choix.
#On a affaire a des types de donnes numeriuqes et les donnes manquantes assez importante, dont le mode me convient le mieux.
client_0_bills['reading_remarque'].fillna(client_0_bills['reading_remarque'].mode()[0],inplace = True)
client_0_bills['counter_number'].fillna(client_0_bills['counter_number'].mode()[0],inplace = True)
client_0_bills.isnull().sum()


# In[42]:


#6.Exécutez une analyse descriptive sur les caractéristiques numériques (colonnes).
column_num = client_0_bills.select_dtypes(include=['int64','float64'])
column_num.describe()


# In[43]:


#7.Sélectionnez les enregistrements de factures du client avec un identifiant ='train_Client_0', en utilisant 2 méthodes.
#Premiere methode:
client_0_bills[client_0_bills['client_id']=='train_Client_0']


# In[44]:


#Deuxieme methode:
client_0_bills.loc[client_0_bills['client_id']=='train_Client_0']


# In[45]:


#8.Transformez la fonctionnalité 'counter_type' en variable numérique à l'aide de l'encodeur de votre choix.
client_0_bills['counter_type'].values


# In[46]:


counter_type = {'counter_type' : {
    'ELEC': 1
}
    
}


# In[47]:


#9. Supprimez la fonctionnalité 'counter_statue' du Dataframe
client_0_bills = client_0_bills.drop('counter_statue', axis = 1)


# In[48]:


client_0_bills.head()


# In[ ]:




