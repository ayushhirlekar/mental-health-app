from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity, get_jwt
from app.models import db, User, Conversation, Message, MoodEntry, VoiceSession
from datetime import datetime

main_bp = Blueprint('main', __name__)

@main_bp.route('/test', methods=['GET'])
def test():
    return jsonify({'message': 'API is working!'}), 200

# Chat endpoints
@main_bp.route('/chat/conversations', methods=['GET'])
@jwt_required()
def get_conversations():
    try:
        user_id = get_jwt_identity()
        conversations = Conversation.query.filter_by(user_id=user_id).order_by(Conversation.updated_at.desc()).all()
        
        return jsonify({
            'conversations': [conv.to_dict() for conv in conversations]
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@main_bp.route('/chat/conversations', methods=['POST'])
@jwt_required()
def create_conversation():
    try:
        user_id = get_jwt_identity()
        data = request.get_json()
        
        conversation = Conversation(
            user_id=user_id,
            title=data.get('title', 'New Chat')
        )
        
        db.session.add(conversation)
        db.session.commit()
        
        return jsonify({
            'message': 'Conversation created',
            'conversation': conversation.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Mood tracking endpoints
@main_bp.route('/mood/entry', methods=['POST'])
@jwt_required()
def add_mood_entry():
    try:
        user_id = get_jwt_identity()
        data = request.get_json()
        
        if not data.get('mood_rating') or not (1 <= int(data['mood_rating']) <= 10):
            return jsonify({'error': 'Mood rating must be between 1 and 10'}), 400
        
        mood_entry = MoodEntry(
            user_id=user_id,
            mood_rating=int(data['mood_rating']),
            notes=data.get('notes', '')
        )
        
        db.session.add(mood_entry)
        db.session.commit()
        
        return jsonify({
            'message': 'Mood entry added',
            'mood_entry': mood_entry.to_dict()
        }), 201
        
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Therapist endpoints
@main_bp.route('/therapist/patients', methods=['GET'])
@jwt_required()
def get_therapist_patients():
    try:
        user_id = get_jwt_identity()
        claims = get_jwt()
        
        if claims.get('role') != 'therapist':
            return jsonify({'error': 'Access denied. Therapist role required.'}), 403
        
        patients = User.query.filter_by(therapist_id=user_id).all()
        
        return jsonify({
            'patients': [patient.to_dict() for patient in patients]
        }), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500