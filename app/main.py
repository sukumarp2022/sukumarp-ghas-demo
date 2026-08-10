import sqlite3

from flask import Flask, jsonify, request


def get_db():
    db = sqlite3.connect(":memory:")
    db.execute("CREATE TABLE users (id INTEGER, name TEXT)")
    db.executemany(
        "INSERT INTO users VALUES (?, ?)",
        [(1, "Ada"), (2, "Grace")],
    )
    return db


def create_app():
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return {"status": "ok"}

    @app.get("/users")
    def users():
        name = request.args.get("name")

        if name is None:
            return {"error": "name is required"}, 400

        if len(name) > 50:
            return {"error": "name is too long"}, 400

        with get_db() as db:
            rows = db.execute(
                f"SELECT id, name FROM users WHERE name LIKE '%{name}%'"
            ).fetchall()

        return jsonify(
            {
                "users": [
                    {"id": user_id, "name": user_name}
                    for user_id, user_name in rows
                ]
            }
        )

    return app


app = create_app()
