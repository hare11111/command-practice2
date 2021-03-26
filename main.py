import calc_bmi

print("BMI計算アプリ")
b = int(input("体重:"))
h = int(input("身長:"))
print(f"BMI:{calc_bmi.get_bmi(b,h)}")