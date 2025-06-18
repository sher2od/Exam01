import sys

vazn_str = input("Vazningizni kiriting (kg): ")
boy_str = input("Bo'yingizni kiriting (m): ")

# Sonlarga aylantirish
if not vazn_str.replace('.', '', 1).isdigit() or not boy_str.replace('.', '', 1).isdigit():
    print("Xatolik: Raqam kiritishingiz kerak.")
    sys.exit()

vazn = float(vazn_str)
boy = float(boy_str)



if vazn <= 0 or boy <= 0:
    print("Xatolik: Vazn va bo'y musbat bo'lishi kerak.")
elif not (1 <= vazn <= 500):
    print("Xatolik: Vazn 1–500 kg oralig'ida bo'lishi kerak.")
elif not (0.5 <= boy <= 3.0):
    print("Xatolik: Bo'y 0.5–3.0 m oralig'ida bo'lishi kerak.")
else:
    bmi = vazn / (boy ** 2)
    print(f"BMI: {bmi:.1f}")

    if bmi < 18.5:
        print("Kam vazn")
    elif bmi < 25:
        print("Normal vazn")
    elif bmi < 30:
        print("Ortiqcha vazn")
    else:
        print("Semizlik")
