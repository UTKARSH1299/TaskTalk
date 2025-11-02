# app.py
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_cors import CORS   # to connect React easily

app = Flask(__name__)
CORS(app)  # allow frontend to talk to backend

# Database setup (auto creates SQLite file)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# ---------------- MODELS ----------------
class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(120), nullable=False)

class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    task_id = db.Column(db.Integer, db.ForeignKey('task.id'), nullable=False)
    author = db.Column(db.String(100), nullable=False)
    text = db.Column(db.String(300), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Create DB tables automatically
with app.app_context():
    db.create_all()
    if Task.query.count() == 0:
        db.session.add(Task(title="First Task"))
        db.session.commit()

# ---------------- ROUTES ----------------
@app.route("/tasks", methods=["GET"])
def get_tasks():
    tasks = Task.query.all()
    return jsonify([{"id": t.id, "title": t.title} for t in tasks])

@app.route("/tasks/<int:task_id>/comments", methods=["GET"])
def get_comments(task_id):
    comments = Comment.query.filter_by(task_id=task_id).order_by(Comment.created_at.desc()).all()
    return jsonify([
        {"id": c.id, "author": c.author, "text": c.text, "time": c.created_at.strftime("%H:%M:%S")}
        for c in comments
    ])

@app.route("/tasks/<int:task_id>/comments", methods=["POST"])
def add_comment(task_id):
    data = request.get_json()
    author = data.get("author", "").strip()
    text = data.get("text", "").strip()
    if not author or not text:
        return jsonify({"error": "Author and text required"}), 400
    c = Comment(task_id=task_id, author=author, text=text)
    db.session.add(c)
    db.session.commit()
    return jsonify({"message": "Comment added!"}), 201

@app.route("/comments/<int:cid>", methods=["PUT"])
def update_comment(cid):
    data = request.get_json()
    c = Comment.query.get_or_404(cid)
    new_text = data.get("text", "").strip()
    if not new_text:
        return jsonify({"error": "Text required"}), 400
    c.text = new_text
    db.session.commit()
    return jsonify({"message": "Updated!"})

@app.route("/comments/<int:cid>", methods=["DELETE"])
def delete_comment(cid):
    c = Comment.query.get_or_404(cid)
    db.session.delete(c)
    db.session.commit()
    return jsonify({"message": "Deleted!"})

if __name__ == "__main__":
    app.run(debug=True)
