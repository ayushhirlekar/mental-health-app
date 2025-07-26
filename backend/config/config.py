import os
from datetime import timedelta
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Database configuration
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # JWT configuration
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=24)
    
    # Flask configuration
    SECRET_KEY = os.environ.get('SECRET_KEY')
    
    # AI Model configuration (for your local LLM)
    AI_MODEL_PATH = os.environ.get('AI_MODEL_PATH', './models/local_llm')
    VOICE_MODEL_PATH = os.environ.get('VOICE_MODEL_PATH', './models/voice_model')