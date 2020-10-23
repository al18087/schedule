def leapYear(year):
    if (year % 4 != 0) or ((year % 100 == 0) and (year % 400 != 0)):
        return 0 #閏年ではないとき
    else:
        return 1 #閏年であるとき


def monthEndDay(month):
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        return 0 #31日まであるとき
    
    elif month == 4 or month == 6 or month == 9 or month == 11:
        return 1 #30日までのとき
    
    else:
        return 2 #28日までのとき


def calendar(year, month):
    day = -2 #2020年1月のスタート
    yearCount = 2020
    monthCount = 1

    while True:
        dayInMonth = []
        if monthEndDay(monthCount) == 0:
            EndOfMonth = 31
        elif monthEndDay(monthCount) == 1:
            EndOfMonth = 30
        else:
            if leapYear(yearCount) == 0:
                EndOfMonth = 28
            else:
                EndOfMonth = 29
        
        for i in range(0, 6):
            days = [] 
            for j in range(0, 7):
                if day <= EndOfMonth:
                    days.append(day)
                else:
                    break
                day += 1
            dayInMonth.append(days)

        if len(dayInMonth[5]) == 0:
            if len(dayInMonth[4]) == 7:
                day = 1
            else:
                day = -(len(dayInMonth[4]) - 1)
        else:
            day = -(len(dayInMonth[5]) - 1)

        
        if yearCount == year and monthCount == month:
            break
        else:
            if monthCount != 12:
                monthCount += 1
            else:
                monthCount = 1
                yearCount += 1
            

    return dayInMonth

        
    
        






