def is_leap_year(year):
    def year_div_by(num):
        return year % num == 0

    if year_div_by(400):
      return True
    elif year_div_by(100):
      return False
    elif year_div_by(4):
      return True

    return False
