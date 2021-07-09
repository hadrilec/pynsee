# -*- coding: utf-8 -*-
# Copyright : INSEE, 2021

import pandas as pd


def _street_metadata():

    df = pd.DataFrame({
        'typeVoieEtablissement':
        ['AIRE', 'ALL', 'AV', 'BASE', 'BD',
                 'CAMI', 'CAR', 'CHE',
                 'CHEM', 'CHS', 'CITE', 'CLOS',
                 'COIN', 'COR', 'COTE', 'COUR', 'CRS',
                 'DOM', 'DSC', 'ECA', 'ESP',
                 'FG', 'GARE', 'GR', 'HAM', 'HLE',
                 'ILOT', 'IMP', 'LD', 'LOT',
                 'MAR', 'MTE', 'PARC', 'PAS', 'PL',
                 'PLAN', 'PLN', 'PLT', 'PONT', 'PORT',
                 'PRO', 'PRV', 'QUA', 'QUAI', 'RES', 'RLE',
                 'ROC', 'RPT', 'RTE', 'RUE', 'SENTE',
                 'SQ', 'TOUR', 'TPL', 'TRA', 'VLA',
                 'VLGE', 'VOIE', 'ZA', 'ZAC',
                 'ZAD', 'ZI', 'ZONE', ' '],
            'typeVoieEtablissementLibelle':
                ['Aire', 'Allée', 'Avenue', 'Base', 'Boulevard',
                 'Cami', 'Carrefour', 'Chemin',
                 'Cheminement', 'Chaussée', 'Cité', 'Clos',
                 'Coin', 'Corniche', 'Cote', 'Cour', 'Cours',
                 'Domaine', 'Descente', 'Ecart', 'Esplanade',
                 'Faubourg', 'Gare', 'Grande Rue', 'Hameau', 'Halle',
                 'Ilot', 'Impasse', 'Lieu dit', 'Lotissement',
                 'Marché', 'Montée', 'Parc', 'Passage', 'Place',
                 'Plan', 'Plaine', 'Plateau', 'Pont', 'Port',
                 'Promenade', 'Parvis', 'Quartier', 'Quai', 'Résidence', 'Ruelle',
                 'Rocade', 'Rond Point', 'Route', 'Rue', 'Sentier',
                 'Square', 'Tour', 'Terre-Plein', 'Traverse', 'Villa',
                 'Village', 'Voie', 'Zone artisanale', "Zone d'aménagement concerté",
                 "Zone d'aménagement différé", 'Zone industrielle', 'Zone', ' '
                 ]
    })

    return(df)
