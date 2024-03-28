credentials       = "../keys/service-acc-cred.json"
project           = "de-zoomcamp-418500"
region            = "us-central1"
location          = "US"
bq_dataset_name   = "metas_reports"
gcs_bucket_suffix = "de-zoomcamp-418500-yo-bucket"
gcs_storage_class = "STANDARD"
buckets           = ["batch", "streaming", "code", "dataproc-staging-bucket"]
accounts = {
  bigquery    = "roles/bigquery.admin"
  storage     = "roles/storage.admin"
  main-viewer = "roles/viewer"
  dataproc    = "roles/dataproc.admin"
}

# dataproc variables
dataproc_cluster_name          = "metar-cluster"
dataproc_staging_bucket_prefix = "dataproc-staging-bucket"
dataproc_machine_type          = "n1-standard-2"