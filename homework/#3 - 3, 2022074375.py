from datetime import date
today = date.today()

def check_adult(year, month, day):
    if today.year - int(year) >= 20:
        return True
    elif today.year - int(year) == 19:
        if today.month > int(month):
            return True
        elif today.month == int(month):
            if today.day >= int(day):
                return True
            else:
                return False
        else:
            return False
    else:
        return False
            
