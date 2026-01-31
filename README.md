# 🎮 Secure Web-Based Rock-Paper-Scissors Game Using Flask

This project implements a **secure, session-based web application** for the classic **Rock-Paper-Scissors** game using **Python Flask**, **SQLite**, **HTML/CSS**, and **JavaScript**.  
The system supports **user registration, authentication, gameplay against a computer opponent, persistent score tracking**, and a **responsive user interface with dark/light theme support**.

---

## Features

- Secure **user registration and login** with hashed passwords  
- **Session-based authentication** to restrict unauthorized access  
- Rock-Paper-Scissors gameplay against a **randomized computer opponent**  
- Automatic tracking of:
  - Wins
  - Losses
  - Score
- Persistent data storage using **SQLite**
- Responsive, modern UI design
- **Dark / Light mode toggle**
- Theme preference stored using browser `localStorage`
- Clear separation of backend, frontend, and client-side logic

---

## Project Structure

```
Rock Paper Scissors Flask App/
├── .venv/                     # Virtual environment (local)
├── app.py                     # Main Flask application
├── create_db.py               # Database creation script
├── database.db                # SQLite database
├── requirements.txt           # Python dependencies
│
├── static/
│   ├── style.css              # Application styling
│   ├── game.js                # Game interaction logic
│   └── theme.js               # Dark / Light mode toggle
│
└── templates/
    ├── login.html             # Login page
    ├── register.html          # Registration page
    └── game.html              # Game dashboard
```

---

## Installation

### 1. Create and Activate Virtual Environment (Optional but Recommended)

```
python -m venv .venv
# Windows PowerShell
.venv\Scripts\Activate.ps1
```

---

### 2. Install Dependencies

```
pip install -r requirements.txt
```

The `requirements.txt` file includes Flask, Werkzeug, Jinja2, and related dependencies required to run the application.

---

### 3. Database Setup

The database is automatically initialized when the application starts.  
You may also manually create the database using:

```
python create_db.py
```

This creates a `users` table containing fields for authentication credentials and game statistics.

---

## How It Works

### 1. Application Configuration

- `app.py` initializes the Flask application.
- A secret key is configured for secure session handling.
- SQLite database connections are managed through helper functions.
- Database tables are automatically created if they do not exist.

---

### 2. User Authentication

#### Registration
- Users create an account using a unique user ID and password.
- Passwords are securely hashed using `werkzeug.security`.

#### Login
- Credentials are validated against stored hashed passwords.
- On successful authentication, a session is created.
- Unauthorized users are redirected to the login page.

---

### 3. Game Logic

- Users select **Rock**, **Paper**, or **Scissors**.
- The computer randomly selects its move.
- Game rules determine the result:
  - **Win** → +10 score and win count increment
  - **Loss** → loss count increment
  - **Draw** → no score change
- Updated statistics are stored in the database after each round.

---

### 4. Frontend Interaction

- `game.js` handles client-side game interactions and dynamic updates.
- `style.css` provides a clean, responsive UI.
- `theme.js` manages dark/light theme switching using `localStorage`.

---

### 5. Theme Management

- Users can toggle between **Dark Mode** and **Light Mode**.
- Theme preferences persist across sessions.
- UI updates occur instantly without page reload.

---

## Usage

### Run the Application

From the project root directory:

```
python app.py
```

Then open your browser and navigate to:

```
http://127.0.0.1:5000
```

---

### Application Flow

1. User registers or logs in.
2. Redirected to the game dashboard.
3. Plays Rock-Paper-Scissors against the computer.
4. Views real-time updates of wins, losses, and score.
5. Logs out securely when finished.

---

## Results and Observations

- Fast response times due to lightweight backend logic.
- SQLite ensures reliable persistence for small-to-medium-scale usage.
- Fully responsive UI across devices.
- Secure password hashing prevents plain-text credential storage.

---

## Future Enhancements

- Global leaderboard
- Match history and analytics dashboard
- AI-based opponent strategy
- REST API version
- Cloud deployment (Render / Railway / AWS)
- Progressive Web App (PWA)

---

## 📜 License

This project is intended for **educational and learning purposes**.  
Free to modify and extend.

---

## 👤 Author

**Sathwika Rudroju**  
Python Full Stack Developer (Fresher)

_Last updated: Jan 2026_
