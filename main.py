from classes import Request, storage_1, storage_2, shop_1

print("Привет")

while True:
    print("Наличие товара:")
    print(f"storage_1: {storage_1}")
    print(f"storage_2: {storage_2}")
    print(f"shop_1: {shop_1}")
    user_text = input("Введите задание\n")

    if user_text == "стоп":
        break
    else:
        try:
            req = Request(user_text)
            req.movi()
        except Exception as e:
            print(f"Произошла ошибка {e}, но можно играть дальше!")
