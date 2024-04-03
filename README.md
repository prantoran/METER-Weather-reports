# METER-Weather-reports

## Technologies

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white)
![Google Cloud](https://img.shields.io/badge/GoogleCloud-%234285F4.svg?style=for-the-badge&logo=google-cloud&logoColor=white)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Jupyter Notebook](https://img.shields.io/badge/jupyter-%23FA0F00.svg?style=for-the-badge&logo=jupyter&logoColor=white)

- [Dataproc](https://cloud.google.com/dataproc)
- [Apache Spark](https://spark.apache.org/)
- [PySpark](https://spark.apache.org/docs/latest/api/python/)
- [BigQuery](https://cloud.google.com/bigquery)
- [GCS Buckets](https://cloud.google.com/storage)

---

## About the project

An educational project to build an end-to-end pipline for near real-time and batch processing of data further used for visualisation 👀 and a machine learning model 🧠.

The project is designed to enable the preparation of an analytical summary of the variability of METAR weather reports over the years for airports of European countries. 

Read more about METAR here ➡️ [METAR](https://www.dronepilotgroundschool.com/reading-aviation-routine-weather-metar-report/)
- An ordinary METAR report is issued hourly unless significant weather changes have occurred.
- For terminology, METAR refers to the type of report issued hourly and a SPECI refers to the type issued during special circumstances.


Here is the Looker Studio demo of the analysis using few stations: [CA_BC_ASOS](https://lookerstudio.google.com/reporting/cc8b1182-bd9e-49c1-9e38-d0feffd0cd0d)


## Setting up Terraform
Checkout [terraform/README.md](terraform/README.md).

## Setting up Mage

Checkout [mage/README.md](mage/README.md).

The contents of Mage was copied from [github.com/mage-ai/maze-zoomcamp](https://github.com/mage-ai/mage-zoomcamp).

#### If there are existing docker instances (i.e. Postgres) that is stopping the prev command
- Stopping docker instances
```bash
docker stop $(docker ps -aq)
docker rm $(docker ps -aq)
```
- Stopping Postgresql running in Ubuntu
```bash
sudo systemctl stop postgresql
```

## Mage features
- Dynamic blocks: https://docs.mage.ai/guides/blocks/dynamic-blocks

### Access Mage UI
```bash
localhost:6789
```


## Process from GCS Bucket to BigQuery using Dataproc/Spark

### Upload Pyspark script and sql commands:
```bash
./scripts/upload_pyspark_script_sql_to_gcs.sh
```
### Submit jobs to Dataproc
```bash
./script/submit_dataproc_job.sh
```
Note: We need to change the station (i.e. `CA_BC_ASOS`) in the script mentioned above.

## Analyze the generated BigQuery tables using Looker Studio
Here is a sample Looker dashboard: [CA_BC_ASOS](https://lookerstudio.google.com/reporting/cc8b1182-bd9e-49c1-9e38-d0feffd0cd0d)
