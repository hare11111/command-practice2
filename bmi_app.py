import calc_bmi

print("BMI計算アプリ")
b = int(input("体重(kg):"))
h = int(input("身長(cm):")) /100
print(f"BMI:{calc_bmi.get_bmi(b,h)}")
print(f"BMI:{calc_bmi.get_bmi(b,h)}")