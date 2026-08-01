#!/usr/bin/env python3
# Adds a few sample tasks so the dashboard isn't empty for the demo.
# Run once (with MongoDB running):  python seed_data.py

import os
from datetime import datetime, timedelta

from pymongo import MongoClient

MONGO_URI = os.environ.get('MONGO_URI', 'mongodb://localhost:27017/task_tracker')

client = MongoClient(MONGO_URI)
db = client.get_default_database()
if db is None:
    db = client['task_tracker']
tasks = db['tasks']

# clear old sample data so we don't pile up duplicates
tasks.delete_many({})

today = datetime.utcnow()


def days(n):
    return (today + timedelta(days=n)).strftime('%Y-%m-%d')


sample = [
    {'title': 'Finish project proposal', 'description': 'Write the overview and goals.',
     'priority': 'high', 'deadline': days(-2), 'status': 'completed'},
    {'title': 'Set up MongoDB VM', 'description': 'Create the free-tier VM, open port 27017.',
     'priority': 'high', 'deadline': days(1), 'status': 'pending'},
    {'title': 'Build the dashboard page', 'description': 'HTML + CSS for the task cards.',
     'priority': 'medium', 'deadline': days(3), 'status': 'pending'},
    {'title': 'Deploy to App Engine', 'description': 'Run gcloud app deploy and test the URL.',
     'priority': 'medium', 'deadline': days(5), 'status': 'pending'},
    {'title': 'Record demo video', 'description': 'Show add / edit / complete / delete.',
     'priority': 'low', 'deadline': days(6), 'status': 'pending'},
]

for t in sample:
    t['created_at'] = today
    t['updated_at'] = today
    t['history'] = []

tasks.insert_many(sample)
print('Added %d sample tasks.' % len(sample))
