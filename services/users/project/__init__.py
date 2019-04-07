import os
from flask import Flask, jsonify
import sys

# instantiate app
app = Flask(__name__)

app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)

#print(app.config, file=sys.stderr)
# docker-compose -f docker-compose-dev.yaml logs

@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'message': 'pong'
    })
    
