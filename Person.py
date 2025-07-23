from Birthday import Birthday


class Person:

    def __init__(self, first_name, last_name):
        """A person is defined by a first and last name, a birthday in the 
        form (month, day), and a city they live in. Additional fields may 
        be added here later. A new object requires only a first and last 
        name to instatiate. The remaining fields can be set later using 
        the corresponding mutator methods."""
        self.first_name = first_name
        self.last_name = last_name
        self.birthday = None
        self.city = None

    def introduce(self):
        """Simple way for a person object to introduce itself."""
        print(
            f"Hello, my name is {self.first_name} and my birthday is on {self.say_birthday()}"
        )

    def set_birthday(self, month, day):
        """Mutator for birthday. Uses our very own Birthday class."""
        self._birthday = Birthday(month, day)

    def set_city(self, city):
        """Mutator for city."""
        self.city = city

    def get_first_name(self):
        """Accessor for first name"""
        return self.first_name

    def get_last_name(self):
        """Accessor for last name"""
        return self.last_name
    def say_birthday(self):
        """Return a conversational birthday like '29th of June'."""
        # pull day and month from the Birthday object
        day = self._birthday.get_day()
        month_num = self._birthday.get_month()

        # 1) figure out the right English ordinal suffix
        if 11 <= day % 100 <= 13:
            suffix = "th"
        elif day % 10 == 1:
            suffix = "st"
        elif day % 10 == 2:
            suffix = "nd"
        elif day % 10 == 3:
            suffix = "rd"
        else:
            suffix = "th"

        # 2) map month number to its name
        month_names = [
            None,
            "January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"
        ]
        month_name = month_names[month_num]

        # 3) build and return the final string
        return f"{day}{suffix} of {month_name}"


    def __lt__(self, other):
        """Allow sorting: Person A < Person B if A.first_name < B.first_name."""
        return self.first_name < other.first_name

    def __str__(self):
        """String representation for the object"""
        return f"[ {self.first_name} {self.last_name}]"
