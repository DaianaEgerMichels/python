class Dates:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def date_format(self):
        print("{:02d}/{:02d}/{}".format(self.day, self.month, self.year))