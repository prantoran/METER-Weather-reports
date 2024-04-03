import pandas as pd
import requests
from typing import Dict, List
import io
import random

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


NETWORKS_SERVICE="https://mesonet.agron.iastate.edu/sites/networks.php?"


@data_loader
def load_data_from_api(data: Dict, *args, **kwargs) -> List[List[Dict]]:
    '''
    Augments data with a list of weather stations from a specified network.

    Args:
        
    Returns:
        
    Raises:
        HTTPError: If there is an error accessing the URL.

    '''

    network_name = data['network']
    url = f'{NETWORKS_SERVICE}network={network_name}&format=csv&nohtml=on'
    response = requests.get(url)

    df = pd.read_csv(io.StringIO(response.text), sep=',')

    stations = list(df.stid)

    tasks = []
    metadata = []
    
    random.shuffle(stations)
    
    stations_subset = ["CYVR", "CYXX", "CYLW", "CYWH"]

    cnt = 2

    for i, u in enumerate(stations):
        if cnt == 2:
            break
        cnt += 1
        stations_subset.append(u)

    for i, u in enumerate(stations_subset):    
        v = data.copy()
        v['station'] = u
        tasks.append(v)
        metadata.append(dict(block_uuid=f"{network_name}_{u}"))

    return [
        tasks,
        metadata
    ]

@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'
