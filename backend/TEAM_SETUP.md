# Team Setup Instructions

## Prerequisites
1. Install PostgreSQL
2. Install Python 3.9+
3. Clone this repository

## Setup Steps
everythin in terminal
1. \`cd backend\`
2. \`python -m venv venv\`
3. \`venv\\Scripts\\activate\` (Windows) or \`source venv/bin/activate\` (Mac/Linux)
4. \`pip install -r requirements.txt\`
5. Copy \`.env.example\` to \`.env\`
6. Update \`.env\` with your PostgreSQL password
7. In PostgreSQL: \`CREATE DATABASE mental_health_app;\`
8. \`python run.py\`

## Your .env should have:
- Your PostgreSQL password
- Same JWT/SECRET keys as team
- Local model paths" > TEAM_SETUP.md