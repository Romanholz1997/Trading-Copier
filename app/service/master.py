from app.models import MasterAccount, SlaveAccount, masterClosePosition, masterOpenPosition, slaveClosePosition, slaveOpenPosition, db

def insert_master(type, account, password, server, plan, flag = 0):
    new_master = MasterAccount(type = type, account = account, password = password, server = server, plan = plan, flag = flag)
    db.session.add(new_master)
    db.session.commit()
    return new_master

def all_master():
    return MasterAccount.query.all()

def insert_slave(type, account, password, server, plan, flag = 0):
    new_slave = SlaveAccount(type = type, account = account, password = password, server = server, plan = plan, flag = flag)
    db.session.add(new_slave)
    db.session.commit()
    return new_slave

def all_slave():
    return SlaveAccount.query.all()

def delete_slave_account(account_id):
    slave_account = SlaveAccount.query.get(account_id)

    # Check if the slave account exists
    if not slave_account:   
        return {"error": "Slave account not found"}, 404

    # Delete the slave account
    db.session.delete(slave_account)
    db.session.commit()

    return {"message": "Slave account deleted successfully"}, 200

def delete_master_account(account_id):
    master_account = MasterAccount.query.get(account_id)

    # Check if the slave account exists
    if not master_account:   
        return {"error": "Slave account not found"}, 404

    # Delete the slave account
    db.session.delete(master_account)
    db.session.commit()

    return {"message": "Slave account deleted successfully"}, 200

def set_masterOpenOrder(ticket, symbol, volume, profit, price_open, price_current, type):
    open_position = masterOpenPosition(
                    ticket=ticket,
                    symbol=symbol,
                    volume=volume,
                    profit=profit,
                    price_open=price_open,
                    price_current=price_current,
                    type=type,
                    flag=0
                )
    db.session.add(open_position)
    db.session.commit()
    return open_position

def get_MasterOpenOrder():
    return masterOpenPosition.query.all()

def get_MasterCloseOrder():
    return masterClosePosition.query.all()

def set_masterCloseOrder(ticket, position_id, symbol, volume, openPrice, closePrice, profit, type):
    closed_order = masterClosePosition(
                    ticket=ticket,
                    open_ticket=position_id,
                    symbol=symbol,
                    volume=volume,
                    price_open=openPrice,
                    price_close=closePrice,
                    profit=profit,
                    type=type,
                    flag=0
                )
    db.session.add(closed_order)
    db.session.commit()
    return closed_order

def set_slaveOpenOrder(account, ticket, open_ticket, symbol, volume, price_open, sl, tp, type):
    open_position = slaveOpenPosition(
                    account=account,
                    ticket=ticket,
                    open_ticket=open_ticket,
                    symbol=symbol,
                    volume=volume,
                    price_open=price_open,
                    sl=sl,                    
                    tp=tp,
                    type=type,
                    flag=0
                )
    db.session.add(open_position)
    db.session.commit()
    return open_position

def set_slaveCloseOrder(account, ticket, open_ticket, symbol, volume, price_close, type):
    close_position = slaveClosePosition(
                    account=account,
                    ticket=ticket,
                    open_ticket=open_ticket,
                    symbol=symbol,
                    volume=volume,
                    price_close=price_close,
                    type=type,
                    flag=0
                )
    db.session.add(close_position)
    db.session.commit()
    return close_position

def get_SlaveOpenOrder():
    return slaveOpenPosition.query.all()

def get_SlaveCloseOrder():
    return slaveClosePosition.query.all()

