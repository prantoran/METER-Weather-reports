import io
import pandas as pd
import requests
from typing import Dict, List

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


STATION_SERVICE="https://mesonet.agron.iastate.edu/cgi-bin/request/asos.py?"


@data_loader
def load_data_from_api(data: Dict, *args, **kwargs) -> pd.DataFrame:
    '''
    Fetches weather data for a specified weather station.
    Args:

    Returns:
        pd.DataFrame: A Pandas DataFrame containing the weather data.

    Raises:
        HTTPError: If there is an error accessing the URL.
    '''
    station = data['station']
    start_date = data['start_date']
    end_date = data['end_date']

    url = STATION_SERVICE + f"station={station}&data=all&"
    url += start_date + "&"
    url += end_date + "&"
    url += "tz=Etc%2FUTC&format=onlycomma&latlon=yes&elev=yes&missing=null&trace=T&direct=no&report_type=3&report_type=4"
    
    return pd.read_csv(url, sep=',')
        

@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'
