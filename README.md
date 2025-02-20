# Character CRUD API

## 📚 Overview

This project is a **REST API** designed using the **Hexagonal Architecture**. It allows you to perform CRUD operations for character management. The project includes:

- 🌐 **Web Interface** (Flask-based API)
- 💻 **Console Client** (using [Typer](https://typer.tiangolo.com/))
- 📝 **API Documentation** with Swagger UI at the `/docs` endpoint

---

## 🚀 Installation

### 🔧 Option 1: Using `virtualenv` and `pip`

1. **Clone the repository**:

```bash
git clone <repository_url>
cd <repository_folder>
```

2. **Create and activate a virtual environment**:

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\\Scripts\\activate
```

3. **Install dependencies**:

```bash
pip install -r requirements.txt
```

---

### 🐳 Option 2: Using Docker Compose

Ensure you have **Docker** and **Docker Compose** installed. Then, simply run:

```bash
docker-compose up -d
```

This will spin up the entire application environment.

---

## 💻 Running the Console Client

The console client provides a CLI for interacting with the API.

### 🔥 **Usage:**

```bash
python3 cli.py --help
```

### ⚡ **Available Commands:**
- `list-characters`: Lists all characters.
- `get-character <id>`: Retrieves a character by ID.
- `add-character`: Adds a new character (provide required fields).
- `delete-character <id>`: Deletes a character by ID.

Example:

```bash
python3 cli.py add-character --name "Luke" --height 172 --mass 77 --hair-color "blond" --skin-color "fair" --eye-color "blue" --birth-year 19
```

---

## 🌐 Accessing the Web Interface

Once the application is running (via Docker or locally), you can access the **API documentation**:

- 🚀 Swagger UI: [http://localhost:5000/docs](http://localhost:5000/docs)

---

## 🏗️ Project Structure

```
├── application              # Use cases (business logic)
├── domain                   # Domain models and schemas
├── infra                    # Infrastructure layer (e.g., Flask views, SQL repositories)
│   ├── web
│   │   └── flask            # Flask API endpoints and configurations
│   └── repositories         # SQLAlchemy repositories
├── cli.py                   # Console client (Typer-based)
├── app.py                   # Flask application setup
├── docker-compose.yml       # Docker Compose configuration
├── requirements.txt         # Python dependencies
└── README.md                # Project documentation
```

---

## 📜 API Documentation

- Swagger UI is available at: **`/docs`**
- The OpenAPI specification is generated dynamically for all endpoints.

---

## ✨ Technologies Used

- 🐍 **Python 3**
- ⚡ **Flask** - Web Framework
- 🏗️ **SQLAlchemy** - ORM
- 📝 **Pydantic** - Data validation and serialization
- 💻 **Typer** - CLI for Python
- 🐳 **Docker** & **Docker Compose** - Containerization


---

💡 *Designed with Hexagonal Architecture for clean, testable, and maintainable code.* 🚀
