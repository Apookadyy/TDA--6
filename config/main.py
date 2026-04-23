from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# Initialize app
app = Flask(__name__)

# Configuration
app.config['SECRET_KEY'] = 'your_secret_key_here'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobportal.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize database
db = SQLAlchemy(app)

# Login manager setup
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# Import routes (make sure these files exist)
from src.routes.auth_routes import auth_bp
from src.routes.job_routes import job_bp
from src.routes.admin_routes import admin_bp

# Register Blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(job_bp)
app.register_blueprint(admin_bp)

# Default route
@app.route('/')
def home():
    return "Welcome to Job Portal Application 🚀"

# Run server
if __name__ == '__main__':
    app.run(debug=True)