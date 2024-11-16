import MetaTrader5 as mt5
import sys
import time
from app.trackerPosition import PositionTracker
from app.service.master import set_slaveCloseOrder, set_slaveOpenOrder, all_master, all_slave, get_SlaveOpenOrder
def get_init():    
    if not mt5.initialize():
        print("initialize() failed")
        mt5.shutdown()
        sys.exit()   

def get_account_login(account_number, password, server):
    if not mt5.login(account_number, password, server):
        print(f"Failed to connect to account #{account_number}")
        mt5.shutdown()
        sys.exit()
    else:
        print(f"Successfully connected to account #{account_number}")
    return True


def should_open_sell(symbol, acount_number,  position_id, type = 0):
    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is None:
        print(symbol, "not found, can not call order_check()")
        mt5.shutdown()
        quit()
    
    # if the symbol is unavailable in MarketWatch, add it
    if not symbol_info.visible:
        print(symbol, "is not visible, trying to switch on")
        if not mt5.symbol_select(symbol,True):
            print("symbol_select({}}) failed, exit",symbol)
            mt5.shutdown()
            quit()
    
    lot = 0.1
    point = mt5.symbol_info(symbol).point
    price = mt5.symbol_info_tick(symbol).bid
    deviation = 20
    sl =  price + 100 * point
    tp = price - 100 * point
    if type == 0:
        request = { 
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": mt5.ORDER_TYPE_SELL,
            "price": price,
            "sl": price + 100 * point,
            "tp": price - 100 * point,
            "deviation": deviation,
            "magic": 234000,
            "comment": "python script open",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_RETURN
        }
        result = mt5.order_send(request)
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            print(f"Error code sell :{result}")            
        else:
            print(f"success sell open: {result}")
            set_slaveSellOpen = set_slaveOpenOrder(acount_number, result.order, position_id, symbol, lot, price, sl, tp, 1)
            return result.order
    else:
        request = { 
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": mt5.ORDER_TYPE_SELL,
            "position": position_id,
            "price": price,           
            "deviation": deviation,
            "magic": 234000,
            "comment": "python script close",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_RETURN
        }
        result = mt5.order_send(request)
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            print(f"Error code sell close:{result}")            
        else:
            print(f"success close sell: {result}")            
            set_slaveSellClose = set_slaveCloseOrder(acount_number, result.order, position_id, symbol, lot, price, 1)
            return 0

def should_open_buy(symbol, acount_number,  position_id, type = 0):
    symbol_info = mt5.symbol_info(symbol)
    if symbol_info is None:
        print(symbol, "not found, can not call order_check()")
        mt5.shutdown()
        quit()
    
    # if the symbol is unavailable in MarketWatch, add it
    if not symbol_info.visible:
        print(symbol, "is not visible, trying to switch on")
        if not mt5.symbol_select(symbol,True):
            print("symbol_select({}}) failed, exit",symbol)
            mt5.shutdown()
            quit()
    
    lot = 0.1
    point = mt5.symbol_info(symbol).point
    price = mt5.symbol_info_tick(symbol).ask
    deviation = 20
    sl = price - 100 * point
    tp = price + 100 * point
    if type == 0:
        request = {
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": mt5.ORDER_TYPE_BUY,
            "price": price,
            "sl": sl,
            "tp": tp,
            "deviation": deviation,
            "magic": 234000,
            "comment": "python script open",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_RETURN,
        }        
        # send a trading request
        result = mt5.order_send(request)
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            print(f"Error code buy:{result}")            
        else:
            print(f"success buy open: {result}")
            set_slaveBuyOpen = set_slaveOpenOrder(acount_number, result.order, position_id, symbol, lot, price, sl, tp, 0)
            return result.order
    else:
        request={
            "action": mt5.TRADE_ACTION_DEAL,
            "symbol": symbol,
            "volume": lot,
            "type": mt5.ORDER_TYPE_BUY,
            "position": position_id,
            "price": price,
            "deviation": deviation,
            "magic": 234000,
            "comment": "python script close",
            "type_time": mt5.ORDER_TIME_GTC,
            "type_filling": mt5.ORDER_FILLING_RETURN,
        }
        result = mt5.order_send(request)
        if result.retcode != mt5.TRADE_RETCODE_DONE:
            print(f"Error code buy close:{result}")            
        else:
            print(f"success buy close: {result}")
            set_slaveBuyClose = set_slaveCloseOrder(acount_number, result.order, position_id, symbol, lot, price, 0)
            return 0
        
# account_number=5031495068
# password="!q0cGgXi"
# server="MetaQuotes-Demo"
# Optionally, initialize the tracker to set the current positions as the baseline
open_position_ids = []
def process_trade_open(positions, slave_lists):
    for slave in slave_lists:
        account_number = slave["account"]
        password = slave.get("password")  # Assuming 'password' is part of the slave dictionary
        server = slave.get("server")  # Assuming 'server' is part of the slave dictionary
        if get_account_login(account_number, password, server):
            time.sleep(1)  # Adjust the sleep time as needed
            for position in positions:
                # Access individual position attributes correctly
                if position["type"] == 0:  # Assuming type 0 is for buy positions
                    position_id = should_open_buy(position["symbol"], account_number, position["ticket"])
                    if position_id:
                        open_position = {
                            "master_id": position["ticket"],
                            "slave_id": position_id
                        }
                        open_position_ids.append(open_position)
                        print(f"Opened buy position ID: {position_id}")
                else:
                    position_id = should_open_sell(position["symbol"], account_number, position["ticket"])
                    if position_id:
                        open_position = {
                            "master_id": position["ticket"],
                            "slave_id": position_id
                        }
                        open_position_ids.append(open_position)
                        print(f"Opened sell position ID: {position_id}")
            
        else:
            print("Login failed.")
            return False
    return True
    
def process_trade_close(positions, slave_lists):
    openOrders = get_SlaveOpenOrder()
    slaves_Order = [slave.to_dict() for slave in openOrders]  # Assuming you have a to_dict method
    for slave in slave_lists:
        account_number = slave["account"]
        password = slave.get("password")  # Assuming 'password' is part of the slave dictionary
        server = slave.get("server")  # Assuming 'server' is part of the slave dictionary
        if get_account_login(account_number, password, server):
            time.sleep(1)  # Adjust the sleep time as needed            
            for position in positions:
                open_position_id = None
                for orders in slaves_Order:
                    if orders["open_ticket"] == position["open_ticket"] and orders["account"] == account_number:
                        open_position_id = orders["ticket"]
                        break
                # Find the matching open position by master_id
                # for ids in open_position_ids:
                #     if ids["master_id"] == position["open_ticket"]:
                #         open_position_id = ids["slave_id"]
                #         break

                if open_position_id is None:
                    print(f"No matching open position found for ticket {position['open_ticket']}")
                    continue

                # Close the corresponding position based on its type
                if position["type"] == 0:  # Assuming type 0 is for buy positions
                    position_id = should_open_buy(position["symbol"], account_number, open_position_id, 1)
                    print(f"Closed buy position ID: {position_id}")
                else:
                    position_id = should_open_sell(position["symbol"], account_number, open_position_id, 1)
                    print(f"Closed sell position ID: {position_id}")
            
        else:
            print("Login failed.")
            return False
    return True

def trading_start(app, stop_event):
    with app.app_context():
        slaves = all_slave()
        slaves_list = [slave.to_dict() for slave in slaves]  # Assuming you have a to_dict method
        print(slaves_list)        
        if not mt5.initialize():
            print("MT5 initialization failed")
            mt5.shutdown()
        tracker = PositionTracker()
        status = True
        masters = all_master()
        master_list = [master.to_dict() for master in masters]
        for master in master_list:
            account_number = master["account"]
            password = master.get("password")  # Assuming 'password' is part of the slave dictionary
            server = master.get("server")  # Assuming 'server' is part of the slave dictionary

            if get_account_login(account_number, password, server):   
                status = False 
                tracker.get_new_close_positions(True)
                current_positions = mt5.positions_get()    
                if current_positions:
                    for position in current_positions:
                        tracker.previous_tickets.add(position.ticket)
                break
        try:
            while not stop_event.is_set():   
                if status:
                    get_account_login(account_number, password, server)
                new_positions = tracker.get_new_open_positions()
                closed_positions = tracker.get_new_close_positions()
                if new_positions:
                    status = True
                    print(new_positions)
                    process_trade_open(new_positions, slaves_list)        
                elif closed_positions:
                    status = True   
                    print(closed_positions)
                    process_trade_close(closed_positions, slaves_list)           
                else:
                    status = False
                    print("No open positions found.")
                    time.sleep(1)  # Adjust the sleep time as needed

        except KeyboardInterrupt:
            print("Real-time data fetching stopped.")

        except Exception as e:
            print(f"An unexpected error occurred: {e}")

        finally:
            # Shutdown MT5 connection
            mt5.shutdown()
            print("MT5 connection shutdown.")