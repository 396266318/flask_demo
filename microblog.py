from app import app, db, cli
from app.models import User, Post
app.run(debug=True, port=8000)