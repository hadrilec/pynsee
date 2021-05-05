
from unittest import TestCase
from pandas import pandas as pd
import sys

from pynsee.sirene.get_data_from_code import get_data_from_code
from pynsee.sirene.search_from_criteria import search_from_criteria
from pynsee.sirene._get_data_sirene import _get_data_sirene

class TestFunction(TestCase):

    def test_get_data_from_code(self):  
        df1 = get_data_from_code("552081317", "808332670")     
        df2 = get_data_from_code("817899438")
        test = isinstance(df1, pd.DataFrame) & isinstance(df2, pd.DataFrame)
        self.assertTrue(test)

    version_3_7 = (sys.version_info[0]==3) & (sys.version_info[1]==7)
    
    if version_3_7:

        def test_search_from_criteria(self):  
            # df1 = get_data_from_criteria(variable="libelleCommuneEtablissement",
            #                             pattern="montrouge", kind="siren")
            
            df1 = search_from_criteria(variable = ["activitePrincipaleUniteLegale", 
                                                    "codePostalEtablissement"],
                                        pattern = ["86.10Z", "75*"], kind = "siret")

            df2 = search_from_criteria(variable = ["libelleCommuneEtablissement",
                                        'denominationUniteLegale'],
                            pattern = ["igny", 'pizza'], 
                            phonetic_search=True,
                            kind = "siret")

            #mix of variable with and without history on siren
            df3 = search_from_criteria(variable=["denominationUniteLegale",
                                       'categorieJuridiqueUniteLegale', 
                                       'categorieEntreprise'],                                     
                                        pattern=["sncf", '9220', 'PME'], kind="siren")

            #input as string and not list
            df4 = search_from_criteria(variable = 'libelleCommuneEtablissement',
                                         pattern= "montrouge", kind="siret")
                
            test1 = isinstance(df1, pd.DataFrame) & isinstance(df2, pd.DataFrame)
            test2 = isinstance(df3, pd.DataFrame) & isinstance(df4, pd.DataFrame)
            
            self.assertTrue(test1 & test2)



        def test_get_data_sirene(self):  
            
            list_query_siren = ["?q=periode(denominationUniteLegale.phonetisation:sncf)&nombre=20",
                    '?q=sigleUniteLegale:???',
                    '?q=periode(activitePrincipaleUniteLegale:86.10Z)&nombre=1000000']
            
            test = True
            for q in list_query_siren:
                df = _get_data_sirene(q, kind= 'siren')
                test = test & isinstance(df, pd.DataFrame)

            list_query_siret =['?q=denominationUniteLegale.phonetisation:oto&nombre=20&champs=denominationUniteLegale', 
                    '?q=prenom1UniteLegale:hadrien AND nomUniteLegale:leclerc',
                    '?q=prenom1UniteLegale.phonetisation:hadrien AND nomUniteLegale.phonetisation:leclerc',
                    '?q=activitePrincipaleUniteLegale:8*',
                    '?q=activitePrincipaleUniteLegale:86.10Z&nombre=1000000', 
                    '?q=activitePrincipaleUniteLegale:86.10Z AND codePostalEtablissement:75*&nombre=5000', 
                    '?q=denominationUniteLegale.phonetisation:oto&nombre=20']

            for q in list_query_siret:
                df = _get_data_sirene(q, kind= 'siret')
                test = test & isinstance(df, pd.DataFrame)
                    
            self.assertTrue(test)