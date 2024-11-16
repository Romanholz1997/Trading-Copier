from app.extensions import db
from datetime import datetime, timedelta

class MasterAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(150))
    account = db.Column(db.Integer)
    password = db.Column(db.String(150))
    server = db.Column(db.String(150))
    plan = db.Column(db.String(150))
    flag = db.Column(db.Integer)
    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'account': self.account,
            'password':self.password,
            'server': self.server,
            'plan': self.plan,
            'flag': self.flag
        }
    def __repr__(self):
        return f'<Master "{self.type}">'
    
class SlaveAccount(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(150))
    account = db.Column(db.Integer)
    password = db.Column(db.String(150))
    server = db.Column(db.String(150))
    plan = db.Column(db.String(150))
    flag = db.Column(db.Integer)
    def to_dict(self):
        return {
            'id': self.id,
            'type': self.type,
            'account': self.account,
            'password':self.password,
            'server': self.server,
            'plan': self.plan,
            'flag': self.flag
        }
    def __repr__(self):
        return f'<Slave "{self.account}">'
    
class masterOpenPosition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket = db.Column(db.Integer, unique=True, nullable=False)
    symbol = db.Column(db.String(20), nullable=False)
    volume = db.Column(db.Float, nullable=False)
    profit = db.Column(db.Float, nullable=False)
    price_open = db.Column(db.Float, nullable=False)
    price_current = db.Column(db.Float, nullable=False)
    type = db.Column(db.Integer, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    flag = db.Column(db.Integer, nullable=False)
    def to_dict(self):
        return {
            'id': self.id,
            'ticket': self.ticket,
            'symbol': self.symbol,
            'volume': self.volume,
            'profit': self.profit,
            'price_open': self.price_open,
            'price_current': self.price_current,           
            'type': self.type,
            'timestamp': self.timestamp,
            'flag': self.flag
        }
    def __repr__(self):
        return f"<OpenPosition {self.ticket} - {self.symbol}>"

class masterClosePosition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ticket = db.Column(db.Integer, unique=True, nullable=False)
    open_ticket = db.Column(db.Integer, nullable=False)
    symbol = db.Column(db.String(20), nullable=False)
    volume = db.Column(db.Float, nullable=False)
    price_open = db.Column(db.Float, nullable=False)
    price_close = db.Column(db.Float, nullable=False)
    profit = db.Column(db.Float, nullable=False)
    type = db.Column(db.Integer, nullable=False)
    time = db.Column(db.DateTime, default=datetime.utcnow)
    flag = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'ticket': self.ticket,
            'open_ticket': self.open_ticket,
            'symbol': self.symbol,
            'volume': self.volume,
            'price_open': self.price_open,
            'price_close': self.price_close,
            'profit': self.profit,
            'type': self.type,
            'time': self.time,
            'flag': self.flag
        }

    def __repr__(self):
        return f"<ClosedOrder {self.ticket} - {self.symbol}>"
    
class slaveOpenPosition(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.Integer, nullable=False) 
    ticket = db.Column(db.Integer, unique=True, nullable=False)
    open_ticket = db.Column(db.Integer, nullable=False)
    symbol = db.Column(db.String, nullable=False)
    volume = db.Column(db.Float, nullable=False)
    price_open = db.Column(db.Float, nullable=False)
    sl = db.Column(db.Float, nullable=False)
    tp = db.Column(db.Float, nullable=False)   
    type = db.Column(db.Integer, nullable=False)
    time = db.Column(db.DateTime, default=datetime.utcnow)
    flag = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'account': self.account,
            'ticket': self.ticket,
            'open_ticket': self.open_ticket,
            'symbol': self.symbol,
            'volume': self.volume,
            'price_open': self.price_open,
            'sl': self.sl,
            'tp': self.tp,
            'type': self.type,
            'time': self.time,
            'flag': self.flag
        }

    def __repr__(self):
        return f"<OpenPosition {self.ticket} - {self.symbol}>"
    
class slaveClosePosition(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    account = db.Column(db.Integer, nullable=False) 
    ticket = db.Column(db.Integer, unique=True, nullable=False)
    open_ticket = db.Column(db.Integer, nullable=False)
    symbol = db.Column(db.String, nullable=False)
    volume = db.Column(db.Float, nullable=False)
    price_close  = db.Column(db.Float, nullable=False) 
    type = db.Column(db.Integer, nullable=False)
    time = db.Column(db.DateTime, default=datetime.utcnow)
    flag = db.Column(db.Integer, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'account': self.account,
            'ticket': self.ticket,
            'open_ticket': self.open_ticket,
            'symbol': self.symbol,
            'volume': self.volume,
            'price_close': self.price_close,
            'type': self.type,
            'time': self.time,
            'flag': self.flag
        }

    def __repr__(self):
        return f"<OpenPosition {self.ticket} - {self.symbol}>"