# aws-lambda-read-table
This AWS Lambda function is designed to retrieve all items from a DynamoDB table named 'SalesRecruitmentProgressManagement' and return the retrieved items in the response. 

1. Importing Required Modules:
   - `import json`: Imports the built-in JSON module for JSON processing.
   - `import boto3`: Imports the AWS SDK module for Python.

2. Lambda Handler Function:
   - `def lambda_handler(event, context):`: This is the main function that serves as the entry point for the Lambda execution. It takes two parameters: `event` (the input data provided to the Lambda function) and `context` (information about the execution environment).

3. DynamoDB Initialization:
   - `dynamodb_resource = boto3.resource('dynamodb')`: Initializes the AWS SDK DynamoDB resource.

4. Specifying Table Name:
   - `table_name = 'SalesRecruitmentProgressManagement'`: Specifies the name of the DynamoDB table from which the items will be retrieved.

5. Main Code Block:
   - `try:`: Starts a try block to handle potential exceptions during the execution.
     - `table = dynamodb_resource.Table(table_name)`: Creates a reference to the specified DynamoDB table.
     - `response = table.scan()`: Performs a scan operation on the table to retrieve all items.
     - `items = response.get('Items', [])`: Retrieves the list of items from the scan response. If no items are found, an empty list is used as the default.
     - `print("Retrieved items data:", items)`: Prints the retrieved items for debugging purposes.

6. Return Response:
   - `return { 'statusCode': 200, 'body': items }`: If the try block is executed successfully, the Lambda function returns a response with a status code of 200 (OK) and the retrieved items as the response body.

7. Exception Handling:
   - `except Exception as e:`: Catches any exceptions that occur during the execution.
     - `print("Error:", e)`: Prints the error message for debugging purposes.
     - `return { 'statusCode': 500, 'body': 'An error occurred while retrieving the items.' }`: In case of an exception, the Lambda function returns a response with a status code of 500 (Internal Server Error) and an error message as the response body.

In summary, this Lambda function retrieves all items from a specified DynamoDB table and returns the retrieved items in the response. If successful, it responds with a status code of 200 and the items, and if an error occurs, it responds with a status code of 500 and an error message.