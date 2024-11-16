import MetaTrader5 as mt5
from datetime import datetime, timedelta
from app.service.master import set_masterOpenOrder,set_masterCloseOrder

class PositionTracker:
    def __init__(self):
        """
        Initializes the PositionTracker with an empty set of previous tickets and closed orders.
        """
        self.previous_tickets = set()
        self.closed_tickets = set()    
    def get_new_open_positions(self):
        """
        Retrieves new open positions from MT5 that were not present in the previous call.
        Saves new positions to the database.

        Returns:
            list: A list of dictionaries containing data of new open positions.
        """
        positions = mt5.positions_get()
        new_positions = []

        if positions is None:
            print("No positions found or failed to retrieve positions.")
            return new_positions  # Return empty list if no positions

        # Extract current open position tickets
        current_tickets = set(position.ticket for position in positions)

        # Identify new tickets by set difference
        added_tickets = current_tickets - self.previous_tickets

        # Update the previous_tickets set
        self.previous_tickets = current_tickets

        # Retrieve data for new positions and save to DB
        for position in positions:
            if position.ticket in added_tickets:
                pos_data = {
                    "ticket": position.ticket,
                    "symbol": position.symbol,
                    "volume": position.volume,
                    "profit": position.profit,
                    "price_open": position.price_open,
                    "price_current": position.price_current,
                    "type": position.type,
                }
                new_positions.append(pos_data)

                # Save to database
                open_position = set_masterOpenOrder(position.ticket, position.symbol, position.volume, position.profit, position.price_open, position.price_current, position.type)
                

        return new_positions

    def get_new_close_positions(self, status = False):
        """
        Retrieves new closed orders that were not present in the previous call.
        Saves closed orders to the database.

        Returns:
            list: A list of dictionaries containing data of newly closed orders.
        """
        now = datetime.now()
        # Fetch closed deals within the last 24 hours
        deals = mt5.history_deals_get(now - timedelta(days=1), now)
        new_closed_orders = []

        if deals is None:
            print("No closed deals found or failed to retrieve history deals.")
            return new_closed_orders

        # Check for newly closed orders
        for deal in deals:
            if deal.ticket not in self.closed_tickets and deal.entry == mt5.DEAL_ENTRY_OUT:
                # Add the new closed ticket to the set to avoid duplicates
                self.closed_tickets.add(deal.ticket)
                
                closed_order_data = {
                    "ticket": deal.ticket,
                    "open_ticket": deal.position_id,  # This links to the original open position
                    "symbol": deal.symbol,
                    "volume": deal.volume,
                    "price_open": deal.price,
                    "price_close": deal.price,
                    "profit": deal.profit,
                    "type": deal.type,
                    "time": datetime.fromtimestamp(deal.time).strftime('%Y-%m-%d %H:%M:%S'),
                }
                new_closed_orders.append(closed_order_data)
                if status != True:
                    close_position = set_masterCloseOrder(deal.ticket, deal.position_id, deal.symbol, deal.volume, deal.price, deal.price, deal.profit, deal.type)
        
        return new_closed_orders

    def reset(self):
        """
        Resets the tracker by clearing the previous_tickets and closed_tickets sets.
        """
        self.previous_tickets.clear()
        self.closed_tickets.clear()