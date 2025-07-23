from datetime import datetime

class Birthday:
    # Some data for this object: the number of days in each month.
    # For simplicity, we ignore leap years and keep February at 28.
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def __init__(self, month, day):
        """Basic constructor. It validates the arguments past to it
        and if they are out of range, it assigns a default value of
        January 1."""
        # Protect month value
        if 1 <= month <= 12:
            self.__month = month
        else:
            # In case of out-of-range month, default to January
            self.__month = 1

        # Protect day value (use –1 in array to sync months)
        if 1 <= day <= Birthday.days_in_month[self.__month - 1]:
            self.__day = day
        else:
            # In case of out-of-range day, default to 1st of month
            self.__day = 1
    # end basic constructor

    def set_day(self, day):
        """Mutator for day. Only changes the day if the
        passed argument is within the valid range for the month."""
        if 1 <= day <= Birthday.days_in_month[self.__month - 1]:
            self.__day = day
    # end set_day

    def get_month(self):
        return self.__month

    def get_day(self):
        return self.__day

    def set_month(self, month):
        """Mutator for month. Only changes the month if 1 ≤ month ≤ 12."""
        if 1 <= month <= 12:
            self.__month = month
    # end set_month

    def days_until(self):
        # 1) get today's month/day as a day-of-year
        today = datetime.today()
        d_t = self.day_in_year(today.month, today.day)

        # 2) get birthday's month/day as a day-of-year
        d_b = self.day_in_year(self.get_month(), self.get_day())

        # 3) compute difference; if today or already passed, wrap around a year
        diff = d_b - d_t
        if diff <= 0:
            diff = 365 + diff

        # 4) return the one final result
        return diff
    # end days_until

    def day_in_year(self, month, day):
        """Calculates the day number within the year for a given
        date (month, day), assuming February has 28 days."""
        count = 0
        for i in range(month - 1):
            count += Birthday.days_in_month[i]
        return count + day

    def __str__(self):
        """String representation for the object"""
        return f"[ {self.get_month()}/{self.get_day()} ]"
