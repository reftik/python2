Rokiv=int(input("Скільки вам рочків?"))
Stat=input("Ви чоловік чи жінка?")
if Rokiv < 6 and Rokiv > 0:
    if Stat == "Чоловік" or "чоловік"  or "чоловіча":
        print("Дошколяр")
    else:
        print("Дошколярка")
if age < 18:
    if Stat == "Чоловік" or "чоловік"  or "чоловіча":
        print("Школяр")
    else:
        print("Школярка")
if age < 60:
    if Stat == "Чоловік" or "чоловік"  or "чоловіча":
        print("Дорослий")
    else:
        print("Доросла")
if age > 60:
    if Stat == "Чоловік" or "чоловік"  or "чоловіча":
        print("Пенсіонер")
    else:
        print("Пенсіонерка")