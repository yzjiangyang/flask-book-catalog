
from app import create_app, db  # app/__init__ (ROOT PACKAGE)
from app.auth.models import User


flask_app = create_app('prod')
with flask_app.app_context():
    db.create_all()
    if not User.query.filter_by(user_name='harry').first():
        User.create_user(user='harry', email='harry@hogwarts.com', password='secret')
flask_app.run()
