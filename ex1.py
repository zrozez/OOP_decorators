from datetime import date

class MyCustomDate:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        self.data = date(self.year, self.month, self.day)
        return str(self.data)

    def __eq__(self, other):
        return self.data == other.data

    def __ne__(self, other):
        return self.data != other.data

    def __gt__(self, other):
        return self.data > other.data

    def __ge__(self, other):
        return self.data >= other.data

    def __sub__(self, other):
        days_of_self = self.year*360 + self.month*30 + self.day
        days_of_other = other.year*360 + other.month*30 + other.day
        if days_of_self < days_of_other:
            raise ValueError("Попробуйте наоборот!")
        else:
            return days_of_self - days_of_other
    
    def __add__(self, other):
        summa = self.year*360 + self.month*30 + self.day + other.year*360 + other.month*30 + other.day
        return summa

data1 = MyCustomDate(14, 8, 2000)
data2 = MyCustomDate(30, 4, 1999)
data3 = MyCustomDate(31, 8, 2021)
data4 = MyCustomDate(3, 9, 2019)
data5 = MyCustomDate(3, 7, 2018)
print(data1, data2, data3, data4, data5)
print(data1 > data2, data3 < data4, data5 >= data1, data2 <= data3, data4 != data5, data1 == data2)
print(data1 - data2, data3-data4, data4-data5)
print(data1 + data2) 