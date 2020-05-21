
from flask import Flask

def create_app(config_filename):
    app = Flask(__name__)
    app.config.from_object(config_filename)
    return app


if __name__ == "__main__":
    app = create_app("app")
    app.run(debug=True, host='127.0.0.1', port=5000)