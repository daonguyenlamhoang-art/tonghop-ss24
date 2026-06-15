class Drink:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.__price = price
        self.is_available = True

    @property
    def price(self):
        return self.__price

    def toggle_available(self):
        self.is_available = not self.is_available


menu = [Drink("CF01", "Cà phê sữa", 35000),Drink("TS01", "Trà sữa matcha", 45000),Drink("TD01", "Trà đào cam sả", 40000)]

while True:
    print("HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE")
    print("1. Xem danh sách đồ uống")
    print("2. Thêm đồ uống mới")
    print("3. Cập nhật trạng thái kinh doanh")
    print("4. Thoát chương trình")
    choice = input("Chọn chức năng (1-4): ")

    if choice == "1":
        print("--- DANH SÁCH ĐỒ UỐNG ---")
        print("Mã món | Tên món | Giá bán | Trạng thái")
        for drink in menu:
            status = "Đang bán"
            if not drink.is_available:
                status = "Ngừng bán"
            print(f"{drink.code} | " f"{drink.name} | " f"{drink.price} | " f"{status}")

    elif choice == "2":
        print("--- THÊM ĐỒ UỐNG MỚI ---")
        code = input("Nhập mã món: ")
        is_exist = False
        for drink in menu:
            if drink.code == code:
                is_exist = True
                break

        if is_exist:
            print("Mã món đã tồn tại trong hệ thống!")
            continue

        name = input("Nhập tên món: ")
        price = int(input("Nhập giá bán: "))

        if price <= 0:
            print("Giá bán không hợp lệ!")
            continue

        new_drink = Drink(code, name, price)
        menu.append(new_drink)

        print(f"Thành công: Đã thêm món {name} vào thực đơn!")

    elif choice == "3":
        print("--- CẬP NHẬT TRẠNG THÁI KINH DOANH ---")
        code = input("Nhập mã món cần cập nhật: ")
        found = None

        for drink in menu:
            if drink.code == code:
                found = drink
                break

        if found is None:
            print("Không tìm thấy món có mã này!")
        else:
            found.toggle_available()
            status = "Đang bán"
            if not found.is_available:
                status = "Ngừng bán"
            print(f"Đã cập nhật trạng thái món {code}.")
            print("Trạng thái hiện tại:", status)

    elif choice == "4":
        print("Cảm ơn ")
        break

    else:
        print("Lựa chọn không hợp lệ!")
