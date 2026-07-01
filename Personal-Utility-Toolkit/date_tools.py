from datetime import date

def today_date():
    return date.today().strftime("%A, %d %B %Y")

def days_until_deadline(year, month, day):
    today = date.today()
    deadline = date(year, month, day)
    return (deadline - today).days

def calculate_age(birth_year):
    current_year = date.today().year
    return current_year - birth_year