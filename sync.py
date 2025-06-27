import datetime
from external_apis import fetch_api_placeholder
from models import APIPlaceholderModel
from db import db

def fetch_and_sync_placeholder(app):
    with app.app_context():
        print(f"[{datetime.datetime.now()}] Starting synchronization with external API...")

        try:
            data = fetch_api_placeholder()
            
            for post in data:
                payload = APIPlaceholderModel(content=post)
                db.session.add(payload)
            
            db.session.commit()
            
            print("Synchronization completed.")
        except Exception as e:
            print(f"[ERROR] Synchronization error: {e}")