# ThreatInsightsAI: Cloud Log Analytics & Threat Detection with AI

ThreatInsightsAI is a cloud-native analytics framework for ingesting AWS security logs and detecting threats using a combination of query analytics and AI-based anomaly detection. Ideal for enhancing threat visibility and automating security insights.

## Features
- Log ingestion from CloudTrail, GuardDuty, and VPC Flow Logs
- AWS Athena queries for pattern detection
- Python-based ML model for anomaly detection
- OpenSearch dashboards for visual insights
- Lambda-based alerting and reporting

## Getting Started
1. Deploy ingestion pipeline using Terraform
2. Configure Athena and Glue jobs
3. Train and run anomaly detection script
4. View dashboards and monitor alerts

## Requirements
- AWS CLI
- Python 3.x with Pandas, Scikit-learn
- OpenSearch or Elasticsearch
- AWS Athena, Glue, Lambda

## License
MIT License
