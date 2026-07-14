# Automated Cloud Infrastructure Provisioning & Reporting Pipeline

## Project Overview

This project automates cloud infrastructure provisioning, API data collection, validation, reporting, and notification workflows using Python, Terraform, and Azure.

The solution demonstrates:

- Infrastructure as Code (Terraform)
- Azure Cloud Automation
- REST API Integration
- Data Validation
- CSV & HTML Report Generation
- Logging
- Notification Framework
- Task Scheduling

---

## Architecture

```text
Scheduler
    |
    v
Python Pipeline
    |
    +--> Terraform
    |       |
    |       +--> Azure Storage Account
    |
    +--> REST API
    |
    +--> Data Validation
    |
    +--> JSON Export
    |
    +--> CSV Report
    |
    +--> HTML Report
    |
    +--> Logging
    |
    +--> Email Notification


Project Structure
cloud-reporting-pipeline/

├── api/
├── config/
├── data/
│   ├── raw/
│   └── processed/
├── infra/
├── logs/
├── notifications/
├── reports/
├── scheduler/
├── terraform/
├── tests/
├── validation/
│
├── main.py
├── requirements.txt
├── README.md
└── .env

Technologies Used

Python
Terraform
Azure
REST APIs
Pandas
PyTest
Jinja2
Git
GitHub

Installation

Clone repository:git clone <repository-url>
Move into project:cd cloud-reporting-pipeline
Create virtual environment:python -m venv venv
Activate environment:source venv/bin/activate
Install dependencies:pip install -r requirements.txt

Configuration
Update .env file:
AZURE_SUBSCRIPTION_ID=
AZURE_RESOURCE_GROUP=
AZURE_LOCATION=

API_BASE_URL=
API_TOKEN=

SMTP_SERVER=
SMTP_USER=
SMTP_PASSWORD=
EMAIL_TO=


Terraform Commands

Initialize:
cd terraform
terraform init
terraform plan
terraform apply
terraform output

Run Application

From project root:
python main.py

Reports Generated

JSON:data/raw/users.json
CSV:data/processed/users.csv
HTML:data/processed/users.html
Logs
logs/pipeline.log

Automated Scheduling
Manual execution:./scheduler/run.sh
Cron execution:0 8 * * * scheduler/run.sh

Running Tests
pytest -v


Features Implemented

API Integration
Data Validation
JSON Export
CSV Reporting
HTML Reporting
Terraform Automation
Logging
Email Framework
Scheduling
Unit Testing

Future Enhancements

Azure VM Provisioning
Azure Key Vault Integration
Teams Notifications
Slack Notifications
CI/CD Pipeline
Multi-Environment Deployment


Author

C R AJJAIAH
