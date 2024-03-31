
import json
import datetime
from typing import Dict, List

if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test

@data_loader
def load_data(config: Dict, *args, **kwargs) -> List[List[Dict]]:

    stations_list = []

    start_date = datetime.datetime(
        config["start_year"],
        config["start_month"],
        config["start_day"]
    )

    end_date = datetime.datetime.now() + datetime.timedelta(days=1)
    
    networks_list: list[str]=config["network"]

    gcs_bucket = config["batch_bucket_name"]

    tasks = []
    metadata = []

    for i, name in enumerate(networks_list):
        tasks.append(
            dict(
                id=i,
                network=name,
                start_date=start_date.strftime("year1=%Y&month1=%m&day1=%d"),
                end_date=end_date.strftime("year2=%Y&month2=%m&day2=%d"),
                gcs_bucket=gcs_bucket
            )
        )
        metadata.append(dict(block_uuid=f'for_network_{name}'))

    return [
        tasks,
        metadata
    ]


@test
def test_output(output, *args) -> None:
    assert output is not None, 'The output is undefined'
