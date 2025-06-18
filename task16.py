age = int(input("Yoshingizni kiriting > "))
narx = 100

if age <= 7:
    result = narx * 0.50
    print(f"Yakuniy narx: {result} so'm (50 % chegitma qollanildi) ")
elif 7 <= age <= 17:
    result = narx * 0.80
    print(f"Yakuniy narx: {result} so'm (20% chegirma qollanildi)")
elif age >= 60:
    result = narx * 0.70
    print(f"Yakuniy narx:{result} so'm (30 % chegirma qollanildi)")