from flask import Blueprint, Flask, request, jsonify
import hmac
import base64
import requests
from hashlib import sha1
from datetime import datetime
from flask_cors import CORS 
from Comm.LenderXComm import execute_lx_api_call

app = Blueprint('GetLoanType', __name__) 
CORS(app)

class XCredentials:
    def __init__(self, lx_user, APIKey, APISecret, BaseURL):
        self.LXUser = lx_user
        self.APISecret = APISecret
        self.APIKey = APIKey
        self.BaseURL = BaseURL

def get_loan_types(credentials):
    return execute_lx_api_call(credentials, None, "/lookup", "type=loan_type", "GET","text/x-json")

@app.route('/api/get_loan_types', methods=['GET'])
def api_get_loan_types():
    # Get query parameters
    lx_user = request.args.get('lx_user')
    APIKey = request.args.get('APIKey')
    APISecret = request.args.get('APISecret')
    BaseURL = request.args.get('BaseURL')

    # Create a credentials object
    cred = XCredentials(lx_user, APIKey, APISecret, BaseURL)

    # Get loan types
    resp = get_loan_types(cred)
   

    return jsonify(resp)
