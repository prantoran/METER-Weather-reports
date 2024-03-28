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

variable "bq_dataset_name" {
  description = "My Metas BigQuery Dataset name"
  default     = "metas_dataset"
}

variable "gcs_bucket_name" {
  description = "My Metas Storage Bucket name"
  default     = "de-zoomcamp-418500-metas-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}