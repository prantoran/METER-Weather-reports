import json
from typing import Dict, List

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data(*args, **kwargs) -> Dict:
    with open ('config.json', 'r') as f:
        config = json.load(f)
    return config


@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'
