# -*- coding: utf-8 -*-
# Copyright : INSEE, 2021

import pandas as pd


def get_map_list():
    """Get a list of all available maps

    Notes:
        All data come from https://france-geojson.gregoiredavid.fr/, made from INSEE and IGN data.

        Only arrondissements municipaux data come from https://public.opendatasoft.com/explore/dataset/arrondissements-millesimes0/information/

    Examples:
        >>> from pynsee.localdata import get_map_list
        >>> map_list = get_map_list()
    """

    maps_list = {
        'name_fr': ['arrondissements',
                    'arrondissements-avec-outre-mer',
                    'arrondissements-version-simplifiee',
                    'arrondissements-municipaux',
                    'cantons',
                    'cantons-avec-outre-mer',
                    'cantons-version-simplifiee',
                    'communes',
                    'communes-avec-outre-mer',
                    'communes-version-simplifiee',
                    'departements',
                    'departements-avec-outre-mer',
                    'departements-version-simplifiee',
                    'metropole',
                    'metropole-et-outre-mer',
                    'metropole-version-simplifiee',
                    'regions',
                    'regions-avant-redecoupage-2015',
                    'regions-avec-outre-mer',
                    'regions-version-simplifiee'],
        'name_en': ['arrondissements',
                    'arrondissements-with-overseas',
                    'arrondissements-version-simplified',
                    'arrondissements-municipaux',
                    'cantons',
                    'cantons-with-overseas',
                    'cantons-version-simplified',
                    'communes',
                    'communes-with-overseas',
                    'communes-version-simplified',
                    'departements',
                    'departements-with-overseas',
                    'departements-version-simplified',
                    'metropole',
                    'metropole-with-overseas',
                    'metropole-version-simplified',
                    'regions',
                    'regions-before-modification-2015',
                    'regions-with-overseas',
                    'regions-version-simplified']
    }
    maps_list = pd.DataFrame(maps_list)
    return(maps_list)
