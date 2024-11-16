from flask import Flask, jsonify
import threading
import signal
import sys
from config import Config
from app.extensions import db
from app.routes.home_routes import bp as home_bp
from app.order import trading_start

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    with app.app_context():
        db.create_all()  # This creates all tables
    
    app.register_blueprint(home_bp)
    # @app.route('/start_trading', methods=['GET'])
    # def start_trading():
    #     trading_thread = threading.Thread(target=trading_start,args=(app,))
    #     trading_thread.start()
    # @app.route('/start_trading', methods=['GET'])
    # def start_trading():
    # trading_thread = threading.Thread(target=trading_start,args=(app,))
    # trading_thread.start()
    stop_event = threading.Event()

    def signal_handler(sig, frame):
        print("Shutting down gracefully...")
        stop_event.set()  # Signal the thread to stop
        sys.exit(0)  # Exit the program

    signal.signal(signal.SIGINT, signal_handler)

    # Start the trading thread
    trading_thread = threading.Thread(target=trading_start, args=(app, stop_event))
    trading_thread.start()

    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app