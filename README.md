# METER-Weather-reports


## Setup Python Environment

### Install Conda

### Create virtual env

```bash
conda create -n metas python=3.11 --file requirements.txt
conda activate metas
```

### Create package list
```bash
conda list -e > requirements.txt
```

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

### Access Mage UI
```bash
localhost:6789
```
