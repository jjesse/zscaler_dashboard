#!/bin/bash

# Zscaler Mission Control Dashboard - Setup Script
# This script sets up the development environment

set -e

echo "🚀 Setting up Zscaler Mission Control Dashboard..."

# Check if Docker is installed
if ! command -v docker &> /dev/null; then
    echo "❌ Docker is not installed. Please install Docker first."
    exit 1
fi

# Check if Docker Compose is installed
if ! command -v docker-compose &> /dev/null; then
    echo "❌ Docker Compose is not installed. Please install Docker Compose first."
    exit 1
fi

# Create .env file from template if it doesn't exist
if [ ! -f .env ]; then
    echo "📝 Creating .env file from template..."
    cp .env.example .env
    echo "⚠️  Please edit .env file with your Zscaler API credentials before running the application."
fi

# Create necessary directories
echo "📁 Creating necessary directories..."
mkdir -p logs
mkdir -p mission_control_data
mkdir -p backups

# Set up Python virtual environment for backend development
echo "🐍 Setting up Python virtual environment..."
cd backend
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
cd ..

# Initialize frontend (if you want to set it up immediately)
read -p "Do you want to set up the frontend now? (y/n): " setup_frontend
if [ "$setup_frontend" = "y" ]; then
    echo "⚛️  Setting up React frontend..."
    cd frontend
    # This will be created in the next phase
    echo "Frontend setup will be completed in Phase 1 of the project."
    cd ..
fi

echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Edit the .env file with your Zscaler API credentials"
echo "2. Run 'docker-compose up -d' to start the services"
echo "3. Visit http://localhost:8000/docs to see the API documentation"
echo "4. Check the logs with 'docker-compose logs -f'"
echo ""
echo "For development:"
echo "- Backend: cd backend && source venv/bin/activate && uvicorn app.main:app --reload"
echo "- Check health: curl http://localhost:8000/health"
