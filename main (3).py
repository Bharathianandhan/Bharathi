def isleapyear(year):
  if (year / 4 == 0 and year / 100 != 0) or year % 400 == 0:
    return True
  else:
    return False


year = int(input("Enter the year:"))
if isleapyear(year):
  print("{} Is a leap year".format(year))
else:
  print("{} Is not a leap year".format(year))
