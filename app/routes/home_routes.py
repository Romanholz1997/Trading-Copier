from flask import Blueprint, render_template, request, jsonify
bp = Blueprint('home', __name__)
import threading
from app.service.master import insert_master, all_master, insert_slave, all_slave, get_MasterOpenOrder, get_MasterCloseOrder, get_SlaveCloseOrder, get_SlaveOpenOrder,delete_slave_account, delete_master_account
from app.order import trading_start

@bp.route('/')
def home():
    return render_template('index.html')


@bp.route('/add_master', methods=['POST'])
def add_master():
    # Get data from the form
    trading_platform = request.form.get('trading_platform') 
    account_login = request.form.get('account_login')
    password = request.form.get('password')
    server = request.form.get('server')
    plan = request.form.get('plan')

    if not all([trading_platform, account_login, password, server, plan]):
        return jsonify({'message': 'All fields are required', 'status': 'error'}), 400

    try:
        # Process the data
        master = insert_master(trading_platform, account_login, password, server, plan)
        masters_list = master.to_dict() 
        return jsonify({'message': 'success', 'status': masters_list}), 200
    except Exception as e:
        return jsonify({'message': str(e), 'status': 'error'}), 500

@bp.route('/add_slave', methods=['POST'])
def add_slave():
    # Get data from the form
    trading_platform = request.form.get('trading_platform') 
    account_login = request.form.get('account_login')
    password = request.form.get('password')
    server = request.form.get('server')
    plan = request.form.get('plan')

    if not all([trading_platform, account_login, password, server, plan]):
        return jsonify({'message': 'All fields are required', 'status': 'error'}), 400

    try:
        # Process the data
        slave = insert_slave(trading_platform, account_login, password, server, plan)
        slave_list = slave.to_dict() 
        return jsonify({'message': 'success', 'status': slave_list}), 200
    except Exception as e:
        return jsonify({'message': str(e), 'status': 'error'}), 500


@bp.route('/delete_slaveAccount', methods=['POST'])
def delete_slaveAccount():
    # Get data from the form
    account_id = request.form.get('id')

    # Check if id is provided
    if not account_id:
        return jsonify({"error": "ID is required"}), 400

    # Call the service function
    response, status_code = delete_slave_account(account_id)

    return jsonify(response), status_code

@bp.route('/delete_masterAccount', methods=['POST'])
def delete_masterAccount():
    # Get data from the form
    account_id = request.form.get('id')

    # Check if id is provided
    if not account_id:
        return jsonify({"error": "ID is required"}), 400

    # Call the service function
    response, status_code = delete_master_account(account_id)

    return jsonify(response), status_code

@bp.route('/get_master', methods=['GET'])  # Corrected route
def get_master():
    try:
        masters = all_master()
        # Serialize the masters to a list of dictionaries
        masters_list = [master.to_dict() for master in masters]  # Assuming you have a to_dict method
        return jsonify(masters_list), 200
    except Exception as e:
        print(f'Error occurred: {e}')
        return jsonify({'message': 'error', 'status': 'fail', 'error': str(e)}), 500
    
@bp.route('/get_slave', methods=['GET'])  # Corrected route
def get_slave():
    try:
        slaves = all_slave()
        # Serialize the masters to a list of dictionaries
        slaves_list = [slave.to_dict() for slave in slaves]  # Assuming you have a to_dict method
        return jsonify(slaves_list), 200
    except Exception as e:
        print(f'Error occurred: {e}')
        return jsonify({'message': 'error', 'status': 'fail', 'error': str(e)}), 500

@bp.route('/get_masterOpen', methods=['GET'])  # Corrected route
def get_masterOpen():
    try:
        masterOpens = get_MasterOpenOrder()
        # Serialize the masters to a list of dictionaries
        masters_list = [opens.to_dict() for opens in masterOpens]  # Assuming you have a to_dict method
        return jsonify(masters_list), 200
    except Exception as e:
        print(f'Error occurred: {e}')
        return jsonify({'message': 'error', 'status': 'fail', 'error': str(e)}), 500

@bp.route('/get_masterClose', methods=['GET'])  # Corrected route
def get_masterClose():
    try:
        masterCloses = get_MasterCloseOrder()
        # Serialize the masters to a list of dictionaries
        masters_list = [closes.to_dict() for closes in masterCloses]  # Assuming you have a to_dict method
        return jsonify(masters_list), 200
    except Exception as e:
        print(f'Error occurred: {e}')
        return jsonify({'message': 'error', 'status': 'fail', 'error': str(e)}), 500

@bp.route('/get_slaveOpen', methods=['GET'])  # Corrected route
def get_slaveOpen():
    try:
        slaveOpens = get_SlaveOpenOrder()
        # Serialize the masters to a list of dictionaries
        slave_list = [opens.to_dict() for opens in slaveOpens]  # Assuming you have a to_dict method
        return jsonify(slave_list), 200
    except Exception as e:
        print(f'Error occurred: {e}')
        return jsonify({'message': 'error', 'status': 'fail', 'error': str(e)}), 500

@bp.route('/get_slaveClose', methods=['GET'])  # Corrected route
def get_slaveClose():
    try:
        slaveCloses = get_SlaveCloseOrder()
        # Serialize the masters to a list of dictionaries
        slave_list = [closes.to_dict() for closes in slaveCloses]  # Assuming you have a to_dict method
        return jsonify(slave_list), 200
    except Exception as e:
        print(f'Error occurred: {e}')
        return jsonify({'message': 'error', 'status': 'fail', 'error': str(e)}), 500

