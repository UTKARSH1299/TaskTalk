import json
from app import app, db, Task, Comment

client = app.test_client()

def test_get_tasks():
    res = client.get('/tasks')
    assert res.status_code == 200

def test_add_comment():
    res = client.post('/tasks/1/comments', json={"author": "Tester", "text": "Hello Flask"})
    assert res.status_code == 201

def test_update_comment():
    # Add one comment first
    res = client.post('/tasks/1/comments', json={"author": "EditUser", "text": "To Edit"})
    assert res.status_code == 201

    # Get comment id inside app context
    with app.app_context():
        cid = Comment.query.order_by(Comment.id.desc()).first().id

    # Update the comment
    res = client.put(f'/comments/{cid}', json={"text": "Edited"})
    assert res.status_code == 200

def test_delete_comment():
    # Add one comment
    res = client.post('/tasks/1/comments', json={"author": "DeleteUser", "text": "Delete Me"})
    assert res.status_code == 201

    # Get comment id inside app context
    with app.app_context():
        cid = Comment.query.order_by(Comment.id.desc()).first().id

    # Delete the comment
    res = client.delete(f'/comments/{cid}')
    assert res.status_code == 200
