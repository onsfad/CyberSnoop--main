from app import app
from flask import render_template, jsonify, Response
from prometheus_client import generate_latest, CONTENT_TYPE_LATEST
from app.metrics import REQUEST_COUNT, CREATED_COUNT

@app.before_request
def before_request():
    REQUEST_COUNT.inc()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/actuator')
def actuator_root():
    return jsonify({
        "status": "UP",
        "metrics": "/actuator/prometheus",
        "home": "/"
    })

@app.route('/actuator/prometheus')
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

@app.route('/test-counter')
def test_counter():
    CREATED_COUNT.inc()
    return f"Counter value: {CREATED_COUNT._value.get()}"

