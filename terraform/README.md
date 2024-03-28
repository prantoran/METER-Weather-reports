# Terraform

## Setting up service account in GCP
- Create project
- Enable APIs
    - BigQuery
    - Cloud Storage
    - DataProc
    - For creating service accounts
        - Identity and Access Management (IAM)
        - Cloud Resource Manager
- IAM Admin -> Service Accounts -> Create Service Account
- Set service account name (i.e. terraform-runner)
- Set the roles. We will need:
    - Storage Admin
    - BigQuery Admin
    - Viewer (of all resources)
    - Dataproc Administrator
    - Service Account User (required for creating Dataproc cluser using Terraform)
    - Additional permissions required for creating service accounts with this service account:
        - Create Service Accounts
        - Delete Service Accounts
        - Prooject IAM Admin
- Download keys
    - IAM -> Service Accounts -> Manage keys -> Add key -> JSON
    - Rename the json to `service-acc-cred.json`
    - Move the json to keys folder

## Setup Terraform Google Provider
- https://registry.terraform.io/providers/hashicorp/google/latest/docs
    - Click `Use Provider` and copy the config. i.e:
        ```
        terraform {
            required_providers {
                google = {
                source = "hashicorp/google"
                version = "5.22.0"
                }
            }
        }

        provider "google" {
            # Configuration options
        }
        ```
- Paste the config in `terraform/main.tf`.
- Setup configuration options, i.e.
    ```bash
    provider "google" {
        project     = "my-project-id"
        region      = "us-central1"
    }
    ```
    - Copy project-id from GCP console's Dashboard.
- Setup credentials, i.e.
    - Option 1: Hard-code path:
    ```bash
    provider "google" {
        project     = "my-project-id"
        region      = "us-central1"
    }
    ```
    - Option 2: Using gcloud auth (uses main account instead of service acccount):
    ```bash
    gcloud default auth-login
    ```
    - Option 3: Set `GOOGLE_CREDENTIALS`:
    ```bash
    export GOOGLE_CREDENTIALS="`pwd`/keys/service-acc-cred.json"
    ```
- (Optional) Format:
    ```bash
    terraform fmt
    ```

## Init Terraform
```bash
terraform init
```

Sample output:

    ```bash
    Initializing the backend...

    Initializing provider plugins...
    - Finding hashicorp/google versions matching "5.22.0"...
    - Installing hashicorp/google v5.22.0...
    - Installed hashicorp/google v5.22.0 (signed by HashiCorp)

    Terraform has created a lock file .terraform.lock.hcl to record the provider
    selections it made above. Include this file in your version control repository
    so that Terraform can guarantee to make the same selections by default when
    you run "terraform init" in the future.

    Terraform has been successfully initialized!

    You may now begin working with Terraform. Try running "terraform plan" to see
    any changes that are required for your infrastructure. All Terraform commands
    should now work.

    If you ever set or change modules or backend configuration for Terraform,
    rerun this command to reinitialize your working directory. If you forget, other
    commands will detect it and remind you to do so if necessary.
    ```

## Setting up resources

### GCP Storage Bucket
- https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/storage_bucket

### GCP BigQuery Dataset
- https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/bigquery_dataset

### GCP Dataproc Cluster
- https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/dataproc_cluster

## Check config 
```bash
terraform plan
```

## Create resources
```bash
terraform apply
```

## Deallocate resources
```bash
terraform destroy
```