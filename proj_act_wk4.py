#1
if year_born >= 1997:
    print("You are a zoomer!")
elif year_born >= 1981:
    print("You are a millennial!")
elif year_born >= 1965:
    print("You are a gen x!")
elif year_born >= 1946:
    print("You are a baby boomer!")
else:
    print("I'm not sure which generation you belong to.")

#2
age = int(input("Enter your age: "))
current_year = 2026
while age > 1:
    print("You were alive in year:", current_year)
    current_year -= 1
    age -= 1
else:
    print("You were born in year:", current_year)

#3
for i in range(1,96):
    if i % 5 == 0:
    print(i)

#4
num = 5
while num <= 95:
    print(num)
    num += 5
