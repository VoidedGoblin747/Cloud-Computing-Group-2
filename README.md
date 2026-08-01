# Smart Task Tracker

Cloud Computing final project - Group 2
Alexander L Hernandez-Carney, Gloriya Leejo, Oziel Flores

A task tracker we built for the class project. Flask backend, MongoDB for storage, deployed on Google App Engine. You can add tasks, edit them, mark them done, delete them, and filter by priority. There's also a JSON API if you want to hit it programmatically instead of using the dashboard.

## Stack
Flask (Python 3), MongoDB, HTML/CSS/JS, Google App Engine

## Who did what
- **Alexander** - frontend: templates, CSS, mobile layout, the priority filter JS
- **Gloriya** - backend: Flask routes, CRUD logic, the JSON API, status history
- **Oziel** - MongoDB VM setup, App Engine deployment, tests

We each worked on our own branch and merged through PRs.

## Running it locally

Need Python 3.9+ and MongoDB running somewhere (local install or Docker).

```bash
git clone https://github.com/VoidedGoblin747/Cloud-Computing-Group-2.git
cd Cloud-Computing-Group-2
python -m venv venv
source venv/bin/activate     # Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Start Mongo if it's not already running:
```bash
mongod --dbpath /path/to/data
# or: docker run -d -p 27017:27017 --name mongo mongo:7
```

Optional - throw in some sample tasks so the dashboard isn't empty:
```bash
python seed_data.py
```

Run it:
```bash
python -m app.main
```
Open `localhost:8080`.

Tests (Mongo needs to be running):
```bash
python -m pytest tests/
```

## Deploying

```bash
gcloud init
gcloud config set project YOUR_PROJECT_ID
```

Put the real MongoDB connection string in `app.yaml` first - don't commit the actual password. Then:
```bash
./deploy.sh
# or just: gcloud app deploy
```

Check it's live:
```bash
gcloud app browse
gcloud app logs tail -s default
```

## MongoDB VM setup

We're running Mongo on an Ubuntu VM:
```bash
wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
sudo apt-get update && sudo apt-get install -y mongodb-org
sudo systemctl enable --now mongod
```

Then make a DB user:
```bash
mongosh
use task_tracker
db.createUser({ user: "task_user", pwd: "your_password_here", roles: [{ role: "readWrite", db: "task_tracker" }] })
```

## API

| Route | Method | What it does |
|---|---|---|
| `/` | GET | dashboard |
| `/add` | GET/POST | add task |
| `/edit/<id>` | GET/POST | edit task |
| `/complete/<id>` | GET | mark done |
| `/delete/<id>` | GET | delete |
| `/api/tasks` | GET/POST | list / create (JSON) |
| `/api/tasks/<id>` | GET/PUT/DELETE | read / update / delete one (JSON) |
| `/health` | GET | returns "ok" |

## Notes
- Tasks sort by priority first, then deadline
- Status changes get logged to a history array on each task
- Priority filter on the dashboard is plain JS
