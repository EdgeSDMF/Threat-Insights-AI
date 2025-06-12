import json
import boto3

def lambda_handler(event, context):
    sns = boto3.client("sns")
    message = "ThreatInsightsAI Alert: Suspicious activity detected in logs."
    sns.publish(
        TopicArn="arn:aws:sns:us-east-1:123456789012:ThreatAlerts",
        Message=message,
        Subject="Threat Alert"
    )
    return {"statusCode": 200, "body": json.dumps("Alert dispatched.")}
