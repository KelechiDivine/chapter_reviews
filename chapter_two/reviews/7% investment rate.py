principal = 1000
rate = 7 / 100
number_of_year = [10, 20, 30]

for year in number_of_year:
    a = principal * (1 + rate) ** year
    print(f'year = {year}, a  = {a: 2f}')
