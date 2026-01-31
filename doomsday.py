from .doomsday_model import DoomsdayModel
from .doomsday_gui import DoomsdayGui
import datetime

class DoomsdayControl():

    def __init__(self):
        self._model = DoomsdayModel()
        self._gui = DoomsdayGui()

    def draw_date(self, start_year: int, end_year: int) -> datetime.date:
        """
        Calls on model to draw date
        """
        return self._model.draw_date(start_year, end_year)

    def get_weekday(self, date: datetime.date) -> int:
        """
        Calls on model to get the relevant weekday for the date
        """
        return self._model.get_weekday(date)

    def doomsday():
        """
        
        """
        date = draw_date(start_year=start_year, end_year=end_year)
        weekday = date.isoweekday() # Returns number corresponding weekday, monday = 1, tuesday = 2 etc.