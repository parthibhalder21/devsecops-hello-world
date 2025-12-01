from flask import Flask
from prometheus_client import make_wsgi_app, Counter
from werkzeug.middleware.dispatcher import DispatcherMiddleware
from werkzeug.serving import run_simple
app = Flask(__name__)
REQUEST_COUNT = Counter('http_requests_total', 'Total number of requests to the app')
@app.route('/')
def hello():
    REQUEST_COUNT.inc()
    return "Hello, World! Remotely deployed via GitHub Actions."
app_with_metrics = DispatcherMiddleware(app.wsgi_app, {'/metrics': make_wsgi_app()})
if __name__ == '__main__':
    run_simple('0.0.0.0', 8080, app_with_metrics)
