print("GENERATION IDENTIFIER")
print("**********************")
print()
year = int (input("which year were you born "))
if year <= 1900:
  print("Lost Generation")
elif year <= 1927:
  print("Greatest Generation")
elif year <= 1945:
  print("Silent Generation")
elif year <= 1964:
  print("Baby Boomers")
elif year <= 1980:
  print("Generation X")
elif year <= 1996:
  print("Millenials")
elif year <= 2012:
  print("Generation z")
elif year >=2012:
  print("Generation Alpha")
else:
  print("Enter Your Year of birth")
