variable "credentials" {
  description = "My Credentials"
  default     = "../keys/service-acc-cred.json"
}

variable "project" {
  description = "Project"
  default     = "de-zoomcamp-418500"
}

variable "region" {
  description = "Project Region"
  default     = "us-central1"
}

variable "location" {
  description = "Project Location"
  default     = "US"
}

# BigQuery
variable "bq_dataset_name" {
  description = "My Metas BigQuery Dataset name"
  default     = "metas_dataset"
}

# GCS Buckets
variable "buckets" {
  description = "Provide buckets names for creating resources example: batch, realt-time"
  type        = list(string)
}
variable "gcs_bucket_suffix" {
  description = "My Metas Storage Bucket suffix"
  default     = "de-zoomcamp-418500-metas-bucket"
}
variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}



# Dataproc variables
variable "dataproc_cluster_name" {
  description = "Dataproc Cluster name"
  default     = ""
  type        = string
}
variable "dataproc_staging_bucket_prefix" {
  description = "Dataproc Staging Bucket Prefix"
  default     = ""
  type        = string
}
variable "dataproc_machine_type" {
  description = "Dataproc machine type"
  default     = ""
  type        = string
}


# service account(s)
variable "accounts" {
  description = "Provide set of resources strings for creating roles, for example: 'bigquery'"
  type        = map(string)
}
