from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from config.config import Config

# Create Flask app
app = Flask(__name__)
app.config.from_object(Config)

# Initialize extensions
db = SQLAlchemy()
db.init_app(app)
jwt = JWTManager(app)
CORS(app)

# Import models
from app.models import User, Conversation, Message, MoodEntry, VoiceSession

# Basic test route
@app.route('/api/test')
def test():
    return {'message': 'Mental Health App API is working!'}

# Simple registration endpoint
@app.route('/auth/register', methods=['POST'])
def register():
    return {'message': 'Registration endpoint ready'}

if __name__ == '__main__':
    with app.app_context():
        # Create database tables
        db.create_all()
        print("✅ Database tables created successfully!")
        
        # Print available routes
        print("\n🚀 Available endpoints:")
        for rule in app.url_map.iter_rules():
            print(f"  {list(rule.methods)} {rule.rule}")
    
    print(f"\n🌐 Flask server running on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)