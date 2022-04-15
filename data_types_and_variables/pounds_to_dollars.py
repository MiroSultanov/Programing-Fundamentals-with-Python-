# Write a program that converts British pounds (integer) to US dollars formatted to the 3rd decimal point.
# 1 British Pound = 1.31 Dollars.


british_pound = int(input())

us_dollar = british_pound * 1.31

print(f"{us_dollar:.3f}")

