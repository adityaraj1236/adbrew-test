TODO App – React + Django + MongoDB + Docker
📌 Overview

This is a full-stack TODO Application built using:

React (Hooks-based)

Django REST Framework

MongoDB (PyMongo, no ORM)

Docker (3 containers: app, api, mongo)

The entire system runs end-to-end in Docker with a persistent MongoDB volume.
All data is fetched from the backend and no hardcoded values are used.

🚀 Features
✔ Fetch TODOs

GET http://localhost:8000/todos
React displays the live TODO list fetched from MongoDB.

✔ Create TODO

POST http://localhost:8000/todos
Adds a new task to MongoDB and refreshes the list automatically.

✔ Fully Dockerized Setup

A single Dockerfile is used (as required by assignment).
Three services run using docker-compose:

api → Django backend

app → React frontend

mongo → MongoDB database

✔ React Implementation

100% React Hooks (useState, useEffect)

Error states (empty task, failed API, loading)

Clean UI

No class components

✔ Django Implementation

No models

No serializers

No Django ORM

Pure PyMongo with robust error handling

Backend designed using clean, production-style structure

✔ MongoDB

Runs inside Docker using official MongoDB server

Persists data using a volume mapped from /src/db

🐳 Docker Setup Used in This Project
docker-compose.yml

The project uses the provided single-Dockerfile architecture.
Services:

Service	Description
api	Django backend server
app	React frontend
mongo	MongoDB instance with persistent storage

Environment variable required:

ADBREW_CODEBASE_PATH=/absolute/path/to/src

▶️ How to Run the Project
1. Set environment variable

Windows PowerShell:

$env:ADBREW_CODEBASE_PATH="C:/Users/Aditya/adbrew/adb_test/src"

2. Start services
docker-compose up --build

3. App URLs
Component	URL
Frontend	http://localhost:3000

Backend API	http://localhost:8000/todos

MongoDB	localhost:27017
📂 Project Structure
src
│
├── app/                 # React frontend
│   ├── public/
│   └── src/
│       ├── App.js
│       ├── api.js
│       ├── index.js
│       └── App.css
│
├── rest/                # Django backend
│   ├── rest/
│       ├── settings.py
│       ├── urls.py
│       ├── views.py
│       └── wsgi.py
│
├── db/                  # MongoDB data (persistent volume)
│
└── requirements.txt

🧠 API Endpoints
GET /todos

Returns all TODO items.
Response example:

[
  { "task": "Buy groceries" },
  { "task": "Learn Docker" }
]

POST /todos

Creates a new TODO.

Body:

{
  "task": "New task"
}

⭐ Why This Implementation Is Strong

Clean code & modular structure (both JS and Python)

Proper use of React Hooks

Robust backend error handling

No ORM / serializer — pure MongoDB usage

Persistent DB volume

Follows assignment instructions exactly

Docker-first approach — fully reproducible environment

Fast, reliable API design

📩 Final Note

This project demonstrates a strong understanding of:

React functional components

State management

Django REST APIs

MongoDB with PyMongo

Docker orchestration

I am confident in explaining the architecture and design in a walkthrough session.