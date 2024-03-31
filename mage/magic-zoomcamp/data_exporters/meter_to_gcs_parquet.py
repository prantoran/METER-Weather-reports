from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from pandas import DataFrame
from os import path
from typing import Dict, List


if 'data_exporter' not in globals():
    from mage_ai.data_preparation.decorators import data_exporter



@data_exporter
def export_data_to_google_cloud_storage(df: DataFrame, data: Dict, **kwargs) -> None:

    config_path = path.join(get_repo_path(), 'io_config.yaml')
    config_profile = 'dev'

    if df.size > 0:
        station = df.iloc[0]['station']
    else:
        station = 'unknown_station'

    network = data['network']
    
    bucket_name = data['gcs_bucket']
    object_key = f"{network}/{station}/{station}.parquet"

    GoogleCloudStorage.with_config(ConfigFileLoader(config_path, config_profile)).export(
        df,
        bucket_name,
        object_key,
    )
