```bash
$ terraform apply  

Terraform used the selected providers to generate the following execution plan. Resource actions are indicated with the
following symbols:
  + create

Terraform will perform the following actions:

  # google_bigquery_dataset.metar-de-dataset will be created
  + resource "google_bigquery_dataset" "metar-de-dataset" {
      + creation_time              = (known after apply)
      + dataset_id                 = "metas_reports"
      + default_collation          = (known after apply)
      + delete_contents_on_destroy = false
      + effective_labels           = (known after apply)
      + etag                       = (known after apply)
      + id                         = (known after apply)
      + is_case_insensitive        = (known after apply)
      + last_modified_time         = (known after apply)
      + location                   = "US"
      + max_time_travel_hours      = (known after apply)
      + project                    = "de-zoomcamp-418500"
      + self_link                  = (known after apply)
      + storage_billing_model      = (known after apply)
      + terraform_labels           = (known after apply)
    }

  # google_dataproc_cluster.metar-cluster will be created
  + resource "google_dataproc_cluster" "metar-cluster" {
      + effective_labels              = (known after apply)
      + graceful_decommission_timeout = "120s"
      + id                            = (known after apply)
      + name                          = "metar-cluster"
      + project                       = "de-zoomcamp-418500"
      + region                        = "us-central1"
      + terraform_labels              = (known after apply)

      + cluster_config {
          + bucket         = (known after apply)
          + staging_bucket = "dataproc-staging-bucket-de-zoomcamp-418500-yo-bucket"
          + temp_bucket    = (known after apply)

          + master_config {
              + image_uri        = (known after apply)
              + instance_names   = (known after apply)
              + machine_type     = "n1-standard-2"
              + min_cpu_platform = (known after apply)
              + num_instances    = 1

              + disk_config {
                  + boot_disk_size_gb = 30
                  + boot_disk_type    = "pd-ssd"
                  + num_local_ssds    = (known after apply)
                }
            }

          + worker_config {
              + image_uri         = (known after apply)
              + instance_names    = (known after apply)
              + machine_type      = "n1-standard-2"
              + min_cpu_platform  = (known after apply)
              + min_num_instances = (known after apply)
              + num_instances     = 2

              + disk_config {
                  + boot_disk_size_gb = 30
                  + boot_disk_type    = "pd-standard"
                  + num_local_ssds    = 1
                }
            }
        }
    }

  # google_storage_bucket.metar-de-bucket["batch"] will be created
  + resource "google_storage_bucket" "metar-de-bucket" {
      + effective_labels            = (known after apply)
      + force_destroy               = true
      + id                          = (known after apply)
      + location                    = "US"
      + name                        = "batch-de-zoomcamp-418500-yo-bucket"
      + project                     = (known after apply)
      + public_access_prevention    = (known after apply)
      + rpo                         = (known after apply)
      + self_link                   = (known after apply)
      + storage_class               = "STANDARD"
      + terraform_labels            = (known after apply)
      + uniform_bucket_level_access = (known after apply)
      + url                         = (known after apply)

      + lifecycle_rule {
          + action {
              + type = "AbortIncompleteMultipartUpload"
            }
          + condition {
              + age                   = 1
              + matches_prefix        = []
              + matches_storage_class = []
              + matches_suffix        = []
              + with_state            = (known after apply)
            }
        }
    }

  # google_storage_bucket.metar-de-bucket["code"] will be created
  + resource "google_storage_bucket" "metar-de-bucket" {
      + effective_labels            = (known after apply)
      + force_destroy               = true
      + id                          = (known after apply)
      + location                    = "US"
      + name                        = "code-de-zoomcamp-418500-yo-bucket"
      + project                     = (known after apply)
      + public_access_prevention    = (known after apply)
      + rpo                         = (known after apply)
      + self_link                   = (known after apply)
      + storage_class               = "STANDARD"
      + terraform_labels            = (known after apply)
      + uniform_bucket_level_access = (known after apply)
      + url                         = (known after apply)

      + lifecycle_rule {
          + action {
              + type = "AbortIncompleteMultipartUpload"
            }
          + condition {
              + age                   = 1
              + matches_prefix        = []
              + matches_storage_class = []
              + matches_suffix        = []
              + with_state            = (known after apply)
            }
        }
    }

  # google_storage_bucket.metar-de-bucket["dataproc-staging-bucket"] will be created
  + resource "google_storage_bucket" "metar-de-bucket" {
      + effective_labels            = (known after apply)
      + force_destroy               = true
      + id                          = (known after apply)
      + location                    = "US"
      + name                        = "dataproc-staging-bucket-de-zoomcamp-418500-yo-bucket"
      + project                     = (known after apply)
      + public_access_prevention    = (known after apply)
      + rpo                         = (known after apply)
      + self_link                   = (known after apply)
      + storage_class               = "STANDARD"
      + terraform_labels            = (known after apply)
      + uniform_bucket_level_access = (known after apply)
      + url                         = (known after apply)

      + lifecycle_rule {
          + action {
              + type = "AbortIncompleteMultipartUpload"
            }
          + condition {
              + age                   = 1
              + matches_prefix        = []
              + matches_storage_class = []
              + matches_suffix        = []
              + with_state            = (known after apply)
            }
        }
    }

  # google_storage_bucket.metar-de-bucket["streaming"] will be created
  + resource "google_storage_bucket" "metar-de-bucket" {
      + effective_labels            = (known after apply)
      + force_destroy               = true
      + id                          = (known after apply)
      + location                    = "US"
      + name                        = "streaming-de-zoomcamp-418500-yo-bucket"
      + project                     = (known after apply)
      + public_access_prevention    = (known after apply)
      + rpo                         = (known after apply)
      + self_link                   = (known after apply)
      + storage_class               = "STANDARD"
      + terraform_labels            = (known after apply)
      + uniform_bucket_level_access = (known after apply)
      + url                         = (known after apply)

      + lifecycle_rule {
          + action {
              + type = "AbortIncompleteMultipartUpload"
            }
          + condition {
              + age                   = 1
              + matches_prefix        = []
              + matches_storage_class = []
              + matches_suffix        = []
              + with_state            = (known after apply)
            }
        }
    }

  # module.service-account["bigquery"].google_project_iam_member.account_roles will be created
  + resource "google_project_iam_member" "account_roles" {
      + etag    = (known after apply)
      + id      = (known after apply)
      + member  = (known after apply)
      + project = "de-zoomcamp-418500"
      + role    = "roles/bigquery.admin"
    }

  # module.service-account["bigquery"].google_service_account.service_account will be created
  + resource "google_service_account" "service_account" {
      + account_id   = "bigquery-service-acc"
      + description  = "bigquery-service-acc Service Account for de-zoomcamp-418500 project"
      + disabled     = false
      + display_name = "bigquery-service-acc"
      + email        = (known after apply)
      + id           = (known after apply)
      + member       = (known after apply)
      + name         = (known after apply)
      + project      = "de-zoomcamp-418500"
      + unique_id    = (known after apply)
    }

  # module.service-account["dataproc"].google_project_iam_member.account_roles will be created
  + resource "google_project_iam_member" "account_roles" {
      + etag    = (known after apply)
      + id      = (known after apply)
      + member  = (known after apply)
      + project = "de-zoomcamp-418500"
      + role    = "roles/dataproc.admin"
    }

  # module.service-account["dataproc"].google_service_account.service_account will be created
  + resource "google_service_account" "service_account" {
      + account_id   = "dataproc-service-acc"
      + description  = "dataproc-service-acc Service Account for de-zoomcamp-418500 project"
      + disabled     = false
      + display_name = "dataproc-service-acc"
      + email        = (known after apply)
      + id           = (known after apply)
      + member       = (known after apply)
      + name         = (known after apply)
      + project      = "de-zoomcamp-418500"
      + unique_id    = (known after apply)
    }

  # module.service-account["main-viewer"].google_project_iam_member.account_roles will be created
  + resource "google_project_iam_member" "account_roles" {
      + etag    = (known after apply)
      + id      = (known after apply)
      + member  = (known after apply)
      + project = "de-zoomcamp-418500"
      + role    = "roles/viewer"
    }

  # module.service-account["main-viewer"].google_service_account.service_account will be created
  + resource "google_service_account" "service_account" {
      + account_id   = "main-viewer-service-acc"
      + description  = "main-viewer-service-acc Service Account for de-zoomcamp-418500 project"
      + disabled     = false
      + display_name = "main-viewer-service-acc"
      + email        = (known after apply)
      + id           = (known after apply)
      + member       = (known after apply)
      + name         = (known after apply)
      + project      = "de-zoomcamp-418500"
      + unique_id    = (known after apply)
    }

  # module.service-account["storage"].google_project_iam_member.account_roles will be created
  + resource "google_project_iam_member" "account_roles" {
      + etag    = (known after apply)
      + id      = (known after apply)
      + member  = (known after apply)
      + project = "de-zoomcamp-418500"
      + role    = "roles/storage.admin"
    }

  # module.service-account["storage"].google_service_account.service_account will be created
  + resource "google_service_account" "service_account" {
      + account_id   = "storage-service-acc"
      + description  = "storage-service-acc Service Account for de-zoomcamp-418500 project"
      + disabled     = false
      + display_name = "storage-service-acc"
      + email        = (known after apply)
      + id           = (known after apply)
      + member       = (known after apply)
      + name         = (known after apply)
      + project      = "de-zoomcamp-418500"
      + unique_id    = (known after apply)
    }

Plan: 14 to add, 0 to change, 0 to destroy.

Do you want to perform these actions?
  Terraform will perform the actions described above.
  Only 'yes' will be accepted to approve.

  Enter a value: yes

module.service-account["storage"].google_service_account.service_account: Creating...
module.service-account["dataproc"].google_service_account.service_account: Creating...
module.service-account["bigquery"].google_service_account.service_account: Creating...
module.service-account["main-viewer"].google_service_account.service_account: Creating...
google_bigquery_dataset.metar-de-dataset: Creating...
google_storage_bucket.metar-de-bucket["dataproc-staging-bucket"]: Creating...
google_storage_bucket.metar-de-bucket["code"]: Creating...
google_storage_bucket.metar-de-bucket["batch"]: Creating...
google_storage_bucket.metar-de-bucket["streaming"]: Creating...
google_dataproc_cluster.metar-cluster: Creating...
google_storage_bucket.metar-de-bucket["code"]: Creation complete after 1s [id=code-de-zoomcamp-418500-yo-bucket]
google_bigquery_dataset.metar-de-dataset: Creation complete after 1s [id=projects/de-zoomcamp-418500/datasets/metas_reports]
google_storage_bucket.metar-de-bucket["dataproc-staging-bucket"]: Creation complete after 1s [id=dataproc-staging-bucket-de-zoomcamp-418500-yo-bucket]
module.service-account["main-viewer"].google_service_account.service_account: Creation complete after 1s [id=projects/de-zoomcamp-418500/serviceAccounts/main-viewer-service-acc@de-zoomcamp-418500.iam.gserviceaccount.com]
module.service-account["dataproc"].google_service_account.service_account: Creation complete after 1s [id=projects/de-zoomcamp-418500/serviceAccounts/dataproc-service-acc@de-zoomcamp-418500.iam.gserviceaccount.com]
module.service-account["bigquery"].google_service_account.service_account: Creation complete after 1s [id=projects/de-zoomcamp-418500/serviceAccounts/bigquery-service-acc@de-zoomcamp-418500.iam.gserviceaccount.com]
module.service-account["storage"].google_service_account.service_account: Creation complete after 1s [id=projects/de-zoomcamp-418500/serviceAccounts/storage-service-acc@de-zoomcamp-418500.iam.gserviceaccount.com]
google_storage_bucket.metar-de-bucket["batch"]: Creation complete after 1s [id=batch-de-zoomcamp-418500-yo-bucket]
module.service-account["dataproc"].google_project_iam_member.account_roles: Creating...
module.service-account["storage"].google_project_iam_member.account_roles: Creating...
module.service-account["main-viewer"].google_project_iam_member.account_roles: Creating...
module.service-account["bigquery"].google_project_iam_member.account_roles: Creating...
google_storage_bucket.metar-de-bucket["streaming"]: Creation complete after 1s [id=streaming-de-zoomcamp-418500-yo-bucket]
module.service-account["bigquery"].google_project_iam_member.account_roles: Creation complete after 8s [id=de-zoomcamp-418500/roles/bigquery.admin/serviceAccount:bigquery-service-acc@de-zoomcamp-418500.iam.gserviceaccount.com]
module.service-account["dataproc"].google_project_iam_member.account_roles: Creation complete after 8s [id=de-zoomcamp-418500/roles/dataproc.admin/serviceAccount:dataproc-service-acc@de-zoomcamp-418500.iam.gserviceaccount.com]
module.service-account["storage"].google_project_iam_member.account_roles: Creation complete after 9s [id=de-zoomcamp-418500/roles/storage.admin/serviceAccount:storage-service-acc@de-zoomcamp-418500.iam.gserviceaccount.com]
google_dataproc_cluster.metar-cluster: Still creating... [10s elapsed]
module.service-account["main-viewer"].google_project_iam_member.account_roles: Creation complete after 9s [id=de-zoomcamp-418500/roles/viewer/serviceAccount:main-viewer-service-acc@de-zoomcamp-418500.iam.gserviceaccount.com]
google_dataproc_cluster.metar-cluster: Still creating... [20s elapsed]
google_dataproc_cluster.metar-cluster: Still creating... [30s elapsed]
google_dataproc_cluster.metar-cluster: Still creating... [40s elapsed]
google_dataproc_cluster.metar-cluster: Still creating... [50s elapsed]
google_dataproc_cluster.metar-cluster: Still creating... [1m0s elapsed]
google_dataproc_cluster.metar-cluster: Still creating... [1m10s elapsed]
google_dataproc_cluster.metar-cluster: Still creating... [1m20s elapsed]
google_dataproc_cluster.metar-cluster: Still creating... [1m30s elapsed]
google_dataproc_cluster.metar-cluster: Still creating... [1m40s elapsed]
google_dataproc_cluster.metar-cluster: Still creating... [1m50s elapsed]
google_dataproc_cluster.metar-cluster: Still creating... [2m0s elapsed]
google_dataproc_cluster.metar-cluster: Still creating... [2m10s elapsed]
google_dataproc_cluster.metar-cluster: Still creating... [2m20s elapsed]
google_dataproc_cluster.metar-cluster: Still creating... [2m30s elapsed]
google_dataproc_cluster.metar-cluster: Still creating... [2m40s elapsed]
google_dataproc_cluster.metar-cluster: Still creating... [2m50s elapsed]
google_dataproc_cluster.metar-cluster: Creation complete after 2m53s [id=projects/de-zoomcamp-418500/regions/us-central1/clusters/metar-cluster]

Apply complete! Resources: 14 added, 0 changed, 0 destroyed.
```