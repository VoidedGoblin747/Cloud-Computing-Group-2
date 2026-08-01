# Smart Task Tracker (Google App Engine + MongoDB)

Cloud Computing Final Project &mdash; **Group 2**
Alexander L Hernandez-Carney, Gloria Leejo, Oziel Flores

A task management web app built on **Google App Engine** with a **MongoDB** backend.
Users can create, update, delete and track tasks with **priorities**, **deadlines**
and a **status history**. Built with Flask (Python 3).

---

## Project structure

```
cloud-computing-group-2/
├── app/
│   ├── __init__.py        # Flask app + MongoDB (PyMongo) setup
│   ├── main.py            # local entry point (python -m app.main)
│   ├── models.py          # Task model / MongoDB queries
│   ├── routes.py          # web pages + JSON API routes
│   └── templates/
│       ├── base.html
│       ├── index.html     # dashboard
│       ├── add_task.html
│       └── edit_task.html
├── static/
│   ├── css/style.css
│   └── js/script.js
├── tests/
│   └── test_api.py
├── config.py
├── requirements.txt
├── app.yaml               # Google App Engine config
├── deploy.sh
├── seed_data.py           # sample tasks for the demo
└── README.md
```

---

## Who does what (3-person split)

Each person owns one area, works on their **own branch**, and opens a **pull request**
for the others to review before merging into `main`.

### Alexander L Hernandez-Carney &mdash; Frontend & UI/UX
- HTML/CSS design: `app/templates/*.html`, `static/css/style.css`
- Dashboard layout, stat cards, priority color-coding
- Responsive (mobile/desktop) design and `static/js/script.js` interactions
- Branch: `feature/frontend-ui`

### Gloria Leejo &mdash; Backend & API
- Flask app setup (`app/__init__.py`) and routes (`app/routes.py`)
- CRUD + JSON API endpoints and MongoDB queries (`app/models.py`)
- Status history tracking and deadline handling
- Branch: `feature/backend-api`

### Oziel Flores &mdash; Database & Deployment
- MongoDB VM setup and configuration, `config.py`
- Google App Engine deployment (`app.yaml`, `deploy.sh`)
- Testing (`tests/`) and documentation (this README)
- Branch: `feature/db-deploy`

---

## How to run it locally (step by step)

You need Python 3.9+ and a MongoDB you can reach.

1. **Clone and enter the repo**
   ```bash
   git clone https://github.com/VoidedGoblin747/Cloud-Computing-Group-2.git
   cd Cloud-Computing-Group-2
   ```

2. **Virtual environment + dependencies**
   ```bash
   python -m venv venv
   source venv/bin/activate        # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

3. **Start MongoDB** (either works)
   - Local install: `mongod --dbpath /path/to/data`
   - Or Docker: `docker run -d -p 27017:27017 --name mongo mongo:7`

4. **(Optional) add sample tasks for the demo**
   ```bash
   python seed_data.py
   ```

5. **Run the app**
   ```bash
   python -m app.main
   ```
   Open <http://localhost:8080>.

Run the tests (MongoDB must be running):
```bash
python -m pytest tests/
```

---

## Deploy to Google App Engine (step by step)

1. Install the Google Cloud SDK and initialize:
   ```bash
   gcloud init
   gcloud config set project YOUR_PROJECT_ID
   ```
2. Put your real MongoDB connection string into `app.yaml` (`MONGO_URI`).
   **Do not commit the real password.**
3. Deploy:
   ```bash
   ./deploy.sh        # or: gcloud app deploy
   ```
4. Open the live site and watch logs:
   ```bash
   gcloud app browse
   gcloud app logs tail -s default
   ```

---

## MongoDB VM setup (Oziel's task)

On an Ubuntu VM:
```bash
wget -qO - https://www.mongodb.org/static/pgp/server-6.0.asc | sudo apt-key add -
echo "deb [ arch=amd64,arm64 ] https://repo.mongodb.org/apt/ubuntu focal/mongodb-org/6.0 multiverse" \
  | sudo tee /etc/apt/sources.list.d/mongodb-org-6.0.list
sudo apt-get update
sudo apt-get install -y mongodb-org
sudo systemctl start mongod
sudo systemctl enable mongod
```
Then create a database user:
```bash
mongosh
use task_tracker
db.createUser({
  user: "task_user",
  pwd: "secure_password_here",
  roles: [{ role: "readWrite", db: "task_tracker" }]
})
```

---

## GitHub collaboration workflow

```bash
# everyone clones the repo
git clone https://github.com/VoidedGoblin747/Cloud-Computing-Group-2.git

# work on your own branch
git checkout -b feature/your-feature-name

# commit and push your changes
git add .
git commit -m "Description of changes"
git push origin feature/your-feature-name

# open a Pull Request on GitHub, get a teammate to review, then merge
```

---

## JSON API

- `GET /` &mdash; dashboard (HTML)
- `GET/POST /add`, `GET/POST /edit/<id>` &mdash; add / edit forms
- `GET /complete/<id>`, `GET /delete/<id>` &mdash; complete / delete
- `GET /api/tasks`, `GET /api/tasks/<id>` &mdash; read tasks as JSON
- `POST /api/tasks`, `PUT /api/tasks/<id>`, `DELETE /api/tasks/<id>` &mdash; JSON CRUD
- `GET /health` &mdash; returns `ok` (App Engine health check)
