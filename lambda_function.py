import json
import boto3

def lambda_handler(event, context):
    # Initialize the DynamoDB resource
    dynamodb_resource = boto3.resource('dynamodb')
    
    # Specify the table name
    table_name = 'SalesRecruitmentProgressManagement'
    
    try:
        # Get a reference to the DynamoDB table
        table = dynamodb_resource.Table(table_name)
        
        # Perform a scan operation to retrieve all items
        response = table.scan()
        
        # Extract the items' data
        items = response.get('Items', [])
        print("Retrieved items data:", items)
        
        return {
            'statusCode': 200,
            'body': items
        }
    except Exception as e:
        print("Error:", e)
        return {
            'statusCode': 500,
            'body': 'An error occurred while retrieving the items.'
        }