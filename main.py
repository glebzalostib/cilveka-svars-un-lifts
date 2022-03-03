a = int(input("Ievadit cilveka masu: "))
b = int(input("Ievadit cilveka masu: "))
c = int(input("Ievadit cilveka masu: "))
print(a + b + c)
print(a + b + c / 3)

if a + b + c > 300:
  print("Cilvēkam nedrikst braukt lifta")
if a + b + c < 300:
  print("Cilvēkam drikst braukt lifta")