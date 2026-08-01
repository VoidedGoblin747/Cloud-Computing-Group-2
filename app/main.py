# Entry point so we can run the app locally with: python -m app.main
from app import app

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
