from flask import Flask, jsonify, request
import threading
import signal
import sys
from config import Config
from app.extensions import db
from app.routes.home_routes import bp as home_bp
from app.order import trading_start
trading_thread = None
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

    @app.route('/start_trading', methods=['POST'])
    def start_trading():
        global trading_thread
        try:
            data = request.get_json()
            toggle_state = data.get('toggle')
            if toggle_state == 1:                
                if trading_thread and trading_thread.is_alive():
                    return jsonify({'status': 'error', 'message': 'Service is already running.'}), 400
                stop_event.clear()

                # Start the trading thread
                trading_thread = threading.Thread(target=trading_start, args=(app, stop_event))
                trading_thread.start()
                print("Service Started")
                # Your logic here
                return jsonify({'status': 'success', 'message': 'Service started.'}), 200
            elif toggle_state == 0:
                if not trading_thread or not trading_thread.is_alive():
                    return jsonify({'status': 'error', 'message': 'Service is not running.'}), 400

                stop_event.set()
                trading_thread.join()
                print("Service Stopped")
                # Your logic here
                return jsonify({'status': 'success', 'message': 'Service stopped.'}), 200
            else:
                return jsonify({'status': 'error', 'message': 'Invalid toggle state.'}), 400

        except Exception as e:
            print(f"Error: {e}")
            return jsonify({'status': 'error', 'message': 'An error occurred processing the request.'}), 500
        


    @app.route('/test/')
    def test_page():
        return '<h1>Testing the Flask Application Factory Pattern</h1>'

    return app