from flask import Flask

app = Flask(__name__)

GITHUB_TOKEN = "ghp_1234567890abcdef1234567890abcdef1234"


from app import routes
