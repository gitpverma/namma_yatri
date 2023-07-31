from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_restful import Api

from handler.register_user_handler import Registration, Update

debug = True
app = Flask(__name__)
app.debug = debug
api = Api(app)

cors_whiteliested_domains = ["*"]
CORS(app, origins=cors_whiteliested_domains, allow_headers=["Authorization", "x-source-id", "Content-Type"],
     supports_credentials=True, intercept_exceptions=True, max_age="600")

app.config['APP_SETTINGS'] = 'development'
app.config['APP_NAME'] = "DEV"

app.secret_key = '7a80a071-6999-4e6b-ab53-7eeaf1a52ed7'

# define endpoint here
api.add_resource(Registration, '/v1/user_register')
api.add_resource(Update, '/v1/user_update')
#api.add_resource(ForgetPwd, '/v1/resetPwd')
#api.add_resource(Topic, '/v1/get_topic')
#api.add_resource(Preference, '/v1/SetPreference')
#api.add_resource(Preference_details, '/v1/get_preference_details')


@app.route('/health')
def health():
    return "I'm healthy!"


if __name__ == '__main__':
    app.run(debug=True, port=5000)



