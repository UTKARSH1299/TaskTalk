# 🧩 TaskTalk — Full Stack Flask + React Comment System  

TaskTalk is a **full-stack comment management web app** built with **Flask (Python)** for the backend and **React.js** for the frontend.  
It allows users to add and view comments in real time, demonstrating seamless communication between frontend and backend — developed as part of the **Better Internship (Associate Software Engineer – Python/React)** assessment.  

---

## 🧠 Overview  

The goal of TaskTalk is to demonstrate:  
- 🔹 Backend API creation using **Flask + SQLAlchemy**  
- 🔹 Frontend integration with **React + Axios**  
- 🔹 Real-time communication between client and server  
- 🔹 Clean folder structure and professional development workflow  

This project showcases a complete **full-stack understanding** of REST APIs, frontend integration, and environment setup.  

---

## ⚙️ Tech Stack  

| Layer | Technology |
|:------|:------------|
| 💻 Frontend | React.js (Axios for API calls) |
| 🔙 Backend | Flask (Python) |
| 🗄️ Database | SQLite (via SQLAlchemy ORM) |
| 🌐 Communication | REST API |
| 🧰 Tools | VS Code, Git, Node.js, Python Virtual Environment |

---

## 📁 Project Structure  

better-assessment/
│
├── backend/
│ ├── app.py # Flask API routes (backend logic)
│ ├── models.py # Database models
│ └── venv/ # Python virtual environment
│
├── frontend-react/
│ ├── src/
│ │ ├── App.js # React UI logic (Axios integration)
│ │ ├── App.css # Styling
│ │ └── index.js # Root entry point
│ ├── package.json # React dependencies
│
├── .gitignore # Ignored folders (node_modules, venv, etc.)
├── README.md # Project documentation

yaml
Copy code

---

## 🚀 How to Run Locally  

### 🧩 Backend Setup (Flask)  
1. Open a terminal and move to the backend folder:  
   ```bash
   cd backend
   python -m venv venv
   venv\Scripts\activate
   pip install flask flask-cors flask-sqlalchemy
Start the Flask server:

bash
Copy code
python app.py
✅ Server runs at: http://127.0.0.1:5000

💻 Frontend Setup (React)
Open another terminal in the frontend-react folder:

bash
Copy code
cd frontend-react
npm install
npm start
✅ Frontend runs at: http://localhost:3000

💬 Usage
Enter your name and comment in the text fields.

Click “Add” to post your comment.

Comments instantly appear in the list with your name and timestamp.

Data is fetched and posted using Axios calls to Flask API endpoints (/api/comments).

🌟 Key Features
✅ Simple REST API built with Flask
✅ CORS-enabled communication between backend and frontend
✅ Real-time UI updates with React state
✅ Optional SQLite database support
✅ Clean, beginner-friendly structure

![alt text](<Screenshot (436).png>)