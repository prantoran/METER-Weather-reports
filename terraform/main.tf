terraform {
  backend "local" {}
  required_version = ">= 1.7"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "5.22.0"
    }
  }
}

provider "google" {
  project     = var.project
  region      = var.region
  credentials = file(var.credentials)
}

# Google Cloud Storage Bucket
resource "google_storage_bucket" "metar-de-bucket" {
  for_each      = toset(var.buckets)
  name          = "${each.key}-${var.gcs_bucket_suffix}"
  location      = var.location
  force_destroy = true

  lifecycle_rule {
    condition {
      age = 1
    }
    action {
      type = "AbortIncompleteMultipartUpload"
    }
  }
}

# BigQuery dataset
resource "google_bigquery_dataset" "metar-de-dataset" {
  dataset_id = var.bq_dataset_name
  location   = var.location
}


# Dataproc cluster
resource "google_dataproc_cluster" "metar-cluster" {
  name                          = var.dataproc_cluster_name
  region                        = var.region
  graceful_decommission_timeout = "120s"

  cluster_config {
    staging_bucket = "${var.dataproc_staging_bucket_prefix}-${var.gcs_bucket_suffix}"

    master_config {
      num_instances = 1
      machine_type  = var.dataproc_machine_type
      disk_config {
        boot_disk_type    = "pd-ssd"
        boot_disk_size_gb = 30
      }
    }

    worker_config {
      num_instances = 2
      machine_type  = var.dataproc_machine_type
      disk_config {
        boot_disk_size_gb = 30
        num_local_ssds    = 1
      }
    }
  }
}