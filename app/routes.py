from flask import Blueprint, request, render_template, jsonify
from app.orange_sms import send_sms

sms_bp = Blueprint('sms', __name__)

@sms_bp.route('/', methods=['GET'])
def home():
    return render_template('form.html')

@sms_bp.route('/send_sms', methods=['POST'])
def send_sms_route():
    to = request.form['to']
    message = request.form['message']
    try:
        response = send_sms(to, message)
        return jsonify({'status': 'succès', 'api_response': response})
    except Exception as e:
        return jsonify({'status': 'échec', 'error': str(e)}), 500
