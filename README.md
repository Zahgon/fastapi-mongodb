# flask-mongodb

[![developer](https://img.shields.io/badge/Dev-grillazz-green?style)](https://github.com/grillazz)
![language](https://img.shields.io/badge/language-python-blue?style)
![framework](https://img.shields.io/badge/framework-Flask-green?style)

![flask-mongodb](/static/greens.jpg)

### Project Description

Flask application with MongoDB backend. Migrated from FastAPI.

### How to Setup

1. Copy `.env.example` to `.env` and configure MongoDB settings
2. Run `uv sync` to install dependencies
3. Run `make up` to start with Docker Compose
4. Or run locally: `flask --app greens.main:app run`

### Running Tests

```bash
make test
```

### About UV
- https://docs.astral.sh/uv/
- https://hynek.me/articles/docker-uv/
- https://thedataquarry.com/posts/towards-a-unified-python-toolchain/
