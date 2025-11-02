import React, { useState, useEffect } from "react";
import axios from "axios";

export default function App() {
  const [task, setTask] = useState(null);
  const [comments, setComments] = useState([]);
  const [author, setAuthor] = useState("");
  const [text, setText] = useState("");

  // Load tasks from Flask backend
  useEffect(() => {
    axios.get("http://127.0.0.1:5000/tasks").then((res) => {
      if (res.data.length > 0) {
        setTask(res.data[0]);
        loadComments(res.data[0].id);
      }
    });
  }, []);

  // Load comments for this task
  const loadComments = async (taskId) => {
    const res = await axios.get(`http://127.0.0.1:5000/tasks/${taskId}/comments`);
    setComments(res.data);
  };

  // Add a new comment
  const addComment = async () => {
    if (!author.trim() || !text.trim()) {
      alert("Please enter your name and comment.");
      return;
    }
    await axios.post(`http://127.0.0.1:5000/tasks/${task.id}/comments`, {
      author,
      text,
    });
    setAuthor("");
    setText("");
    loadComments(task.id);
  };

  return (
    <div style={{ margin: 40, fontFamily: "Arial" }}>
      <h2>🧩 TaskTalk</h2>
      {task && <h3>Task: {task.title}</h3>}

      <div style={{ marginBottom: 15 }}>
        <input
          placeholder="Your name"
          value={author}
          onChange={(e) => setAuthor(e.target.value)}
        />
        <input
          placeholder="Write a comment"
          value={text}
          onChange={(e) => setText(e.target.value)}
          style={{ marginLeft: 5 }}
        />
        <button onClick={addComment} style={{ marginLeft: 5 }}>
          Add
        </button>
      </div>

      <div>
        {comments.length === 0 ? (
          <p>No comments yet.</p>
        ) : (
          comments.map((c) => (
            <div
              key={c.id}
              style={{
                background: "#f3f3f3",
                padding: 10,
                marginBottom: 6,
                borderRadius: 6,
              }}
            >
              <b>{c.author}</b>: {c.text}
              <small style={{ color: "#777" }}> ({c.time})</small>
            </div>
          ))
        )}
      </div>
    </div>
  );
}
