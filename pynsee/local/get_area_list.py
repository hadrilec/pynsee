# -*- coding: utf-8 -*-

from functools import lru_cache

@lru_cache(maxsize=None)
def get_area_list(area=None):    
    
    import pandas as pd
    from pynsee.utils._request_insee import _request_insee
    from pynsee.utils._paste import _paste
    
    list_available_area = ['zonesDEmploi2020', 'airesDAttractionDesVilles2020', 'unitesUrbaines2020']
    area_string = _paste(list_available_area, collapse = " ")
    
    if area is not None:
        list_available_area = [area]
        if not area in list_available_area:
            msg = "!!! {} is not available\nPlease choose area among:\n{}".format(area, area_string)
            raise ValueError(msg)        
    
    list_data = []
    
    for a in list_available_area:
        api_url = 'https://api.insee.fr/metadonnees/V1/geo/' + a + '?date=*'
        
        request = _request_insee(api_url = api_url,  file_format = 'application/json')
        
        data = request.json() 
        
        for i in range(len(data)):
            df = pd.DataFrame(data[i], index=[0])
            list_data.append(df)
    
    data_all = pd.concat(list_data).reset_index(drop=True)
    
    return(data_all)
    
