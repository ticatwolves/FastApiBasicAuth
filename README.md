# 🚀 FastAPI Basic Auth

A **production-ready FastAPI boilerplate** with authentication, user management, and profile handling.  
Built with modern Python packaging (`hatchling`) and a clean `src/` layout.  

---

## 📦 Features
- 🔑 **JWT Authentication** (login, signup, refresh tokens)  
- 👤 **User Profiles** (CRUD operations)  
- 🔒 **Password Hashing** with `passlib[bcrypt]`  
- 🗂️ **SQLAlchemy ORM + Alembic migrations**  
- 📖 **Interactive API Docs** (Swagger UI & ReDoc)  
- 🐳 Optional **Docker support** for deployment  
- 📂 Modern `src/` folder layout  
- 🧪 Pytest setup for testing  

---

## 🛠️ Project Structure
```
FastApiBasicAuth/
├── pyproject.toml
├── requirements/
│   ├── base.txt
│   ├── prod.txt
│   └── dev.txt
├── src/
│   └── fastapi_basic_auth/
│       ├── __init__.py
│       ├── main.py
│       ├── api/
│       ├── core/
│       ├── models/
│       ├── schemas/
│       └── db.py
└── tests/
    └── test_auth.py
```

---

## ⚡ Installation

### Clone the repo
```bash
git clone https://github.com/ticatwolves/FastApiBasicAuth
cd FastApiBasicAuth
```

### Install dependencies
Using **prod** requirements:
```bash
pip install -r requirements/prod.txt
```

Or install in **editable mode**:
```bash
pip install -e .
```

### Run migrations
```bash
alembic upgrade head
```

### Start the server
```bash
uvicorn fastapi_basic_auth.main:app --reload
```

API available at → [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🐍 Packaging & Publishing

This project uses **hatchling** with [`hatch-requirements-txt`](https://pypi.org/project/hatch-requirements-txt/).  
Dependencies are dynamically loaded from `requirements/prod.txt`.

### Build
```bash
hatch build
```

### Publish to PyPI
```bash
hatch publish
```

---

## 🧪 Testing
Install dev dependencies:
```bash
pip install -r requirements/dev.txt
```

Run tests:
```bash
pytest
```

---

## 🛣️ Roadmap
- [ ] Social login (Google/GitHub)  
- [ ] Role-based access control (RBAC)  
- [ ] Multi-tenant support (for SaaS)  
- [ ] WebSocket notifications  
- [ ] Docker + CI/CD workflows  

---

## 🤝 Contributing
Contributions are welcome!  
- Fork the repo  
- Create a feature branch  
- Submit a PR 🚀  

---

## 📜 License
This project is licensed under the **MIT License**.  
See [LICENSE](LICENSE) for details.  
