from datetime import datetime, timedelta


class Delivery:
    def __init__(self):
        self.date = datetime.now() + timedelta(days=10)

    def get_date(self):
        return self.date
