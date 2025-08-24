# FastAPI Blog Project

A simple blog API built with FastAPI and SQLAlchemy.

## Setup

1. Create virtual environment:
```bash
python -m venv blog-env
```

2. Activate virtual environment:
```bash
blog-env\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
uvicorn blog.main:app --reload
```

## API Endpoints

- `POST /blog`: Create a new blog post
- `GET /blog`: Get all blog posts
- `GET /blog/{id}`: Get a specific blog post