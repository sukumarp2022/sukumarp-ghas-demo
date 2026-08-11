"""Intentionally vulnerable examples for the CodeQL demonstration."""

import pickle
import subprocess
from pathlib import Path

import requests
from flask import render_template_string, request


def run_requested_command():
    command = request.args.get("command", "")
    return subprocess.run(
        command,
        shell=True,
        capture_output=True,
        text=True,
        check=False,
    ).stdout


def read_requested_file():
    filename = request.args.get("filename", "")
    return Path(filename).read_text(encoding="utf-8")


def fetch_requested_url():
    url = request.args.get("url", "")
    return requests.get(url, timeout=5).text


def load_requested_payload():
    payload = request.get_data()
    return pickle.loads(payload)


def render_requested_template():
    template = request.args.get("template", "")
    return render_template_string(template)
