import datetime
import random

class DoomsdayModel():

    def __init__(self):
        pass
    
    def draw_date(self, start_year: int, end_year: int) -> datetime.date:
        """
        Draws a random date in the range between the start year and end year.
        """
        start_date = datetime.date(start_year, 1, 1)
        end_date = datetime.date(end_year, 12, 31)
        days_between_dates = (end_date - start_date).days
        rand_number_days = random.randrange(days_between_dates + 1) # + 1 to include end date
        return start_date + datetime.timedelta(days=rand_number_days)
    
    def get_weekday(self, date: datetime.date) -> int:
        return date.isoweekday()