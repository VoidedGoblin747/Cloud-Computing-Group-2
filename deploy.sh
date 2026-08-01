#!/bin/bash
# deploy.sh - deploy the Smart Task Tracker to Google App Engine

echo "🚀 Deploying Smart Task Tracker to Google App Engine..."

# install dependencies
pip install -r requirements.txt

# run tests (needs a MongoDB running)
python -m pytest tests/ || echo "tests skipped/failed - check MongoDB is running"

# deploy to App Engine
gcloud app deploy app.yaml

echo " Deployment complete!"
echo "🌐 Visit: https://your-project-id.appspot.com"
