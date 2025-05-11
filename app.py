from flask import Flask
from controllers.dashboard_controller import dashboard_bp
from controllers.drive_controller import drive_bp

app = Flask(__name__)
app.secret_key = 'your_secret_key'


import os
os.environ['OAUTHLIB_INSECURE_TRANSPORT'] = '1'


app.register_blueprint(dashboard_bp)
app.register_blueprint(drive_bp)


os.makedirs('downloads', exist_ok=True)

if __name__ == '__main__':
    app.run(port='7000',host='0.0.0.0',debug=True)
