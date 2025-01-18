# AWS-Cognito-Lambda-login

Example authentication and login implementation using AWS Cognito and Lambda functions.
![image](https://github.com/user-attachments/assets/6a276357-805b-4ab9-90d8-df944e29f25e)

# This repository contains :

- Lambda Function python code for authentification and login with AWS Cognito Service
- JSON sample to add to your lambda function as an inline permission policy (to grant it the permission to authenticate with your Cognito service)
- JSON sample to test your lambda function.

# Getting started

1. You need to have an AWS subscription (can be free tier) alongside a Userpool created in AWS Cognito and an Application client within that Userpool.
2. Create atleast one valid test user in your Userpool (tab "Users management &rarr; Users") and make sure their confirmation status is _confirmed_.
3. In the Application client's settings, make sure the `ALLOW_USER_PASSWORD_AUTH` checkbox, allowing signin with username and password, is checked.
4. In the AWS Lambda service, create a Lambda function using Python 3.8+ (any version past 3.8). Paste the code from LambdaCognitoLogin.py
5. In the Lambda function editor, within the tab "Configuration &rarr; Permissions", click the role name. This leads you to the IAM service at the "Roles" Tab. In the Permission policies section, click "Add permissions &rarr; Create inline Policy". In the policy editor, select the JSON format and paste the JSON sample from LambdaCognitoLogin.json.
6. In the Lambda function editor, within the tab "Configuration &rarr; Environment variables", create the variables `USER_POOL_APP_CLIENT_ID` and `USER_POOL_APP_CLIENT_SECRET` (using the client id and client secret from your Cognito Application client).
7. In the Lambda function editor, within the tab "Test", paste the JSON sample from LambdaCognitoLogin-test.json. Change the username and password values with valid credentials from one of your Cognito Userpool test users.
8. Run the test within the Lambda function code editor. If the previous steps were completed correctly, your output should be a response with `"status": "success"` (and other data), confirming your Lambda function and your Cognito services are now working together.

# Disclaimer

This project is not affiliated with, maintained by, or endorsed by Amazon Web Services (AWS). It is an independent project created to help developers integrate AWS Cognito with Lambda functions. The project code is partially derived from AWS-samples and modified to work with the more recent AWS Cognito versions that use client secrets.
