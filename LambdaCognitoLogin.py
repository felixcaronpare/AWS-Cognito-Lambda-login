# Copyright (C) 2025 felixcaronpare
# SPDX-License-Identifier: MIT-0

import boto3
import os
import sys
import hmac
import hashlib
import base64

def get_secret_hash(username, client_id, client_secret):
    message = username + client_id
    dig = hmac.new(
        str(client_secret).encode('utf-8'),
        msg=message.encode('utf-8'),
        digestmod=hashlib.sha256
    ).digest()
    return base64.b64encode(dig).decode()

client = boto3.client('cognito-idp')

def lambda_handler(event, context):
    if 'username' not in event or 'password' not in event:
        return {
            'status': 'fail',
            'msg': 'Username and password are required'
        }
    resp, msg = initiate_auth(event["username"], event["password"])
    if msg != None:
        return {
            'status': 'fail', 
            'msg': msg,
        }
    return {
        'status': 'success',
        'tokens': resp['AuthenticationResult']
    }

def initiate_auth(username, password):
    # (See https://docs.aws.amazon.com/lambda/latest/dg/configuration-envvars.html for info on programmatically defining environment variables in Lambda.)
    App_client_id = os.environ.get('USER_POOL_APP_CLIENT_ID')
    client_secret = os.environ.get('USER_POOL_APP_CLIENT_SECRET')
    
    if not client_secret or not App_client_id:
        raise ValueError("fMissing atleast one environment variable")

    try:
        secret_hash = get_secret_hash(username, App_client_id, client_secret)
        resp = client.initiate_auth(
            ClientId=App_client_id,
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters={
                'USERNAME': username,
                'PASSWORD': password,
                'SECRET_HASH': secret_hash
            }
        )
    except client.exceptions.InvalidParameterException as e:
        return None, "Username and password must not be empty"
    except client.exceptions.NotAuthorizedException as e:
        return None, "Username or password is incorrect"
    except client.exceptions.UserNotFoundException as e:
        return None, "User does not exist"
    except Exception as e:
        return None, "Unknown error"
    return resp, None