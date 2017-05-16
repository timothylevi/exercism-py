def is_leap_year(year):
    """Return true if year is determined to be a leap year."""

    def year_div_by(num):
        """Return true if year is divisible by number."""
        return year % num == 0

    if year_div_by(400):
      return True
    elif year_div_by(100):
      return False
    elif year_div_by(4):
      return True

    return False
