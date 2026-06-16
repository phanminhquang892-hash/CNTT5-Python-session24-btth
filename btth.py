class Drink:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.__price = price
        self.is_available = True

    @property
    def price(self):
        """Getter an toàn để đọc giá bán (không có setter)."""
        return self.__price

    def toggle_available(self):
        """Đổi trạng thái kinh doanh: True <-> False"""
        self.is_available = not self.is_available


menu = [
    Drink("CF01", "Cà phê sữa", 35000),
    Drink("TS01", "Trà sữa matcha", 45000),
    Drink("TD01", "Trà đào cam sả", 40000)
]


def print_menu_list():
    print("--- DANH SÁCH ĐỒ UỐNG ---")
    print(f"{'Mã món'} | {'Tên món'} | {'Giá bán'} | {'Trạng thái'}")
    
    for d in menu:
        if d.is_available:
            status = "Đang bán"
        else:
            status = "Ngừng bán"
        print(f"{d.code} | {d.name} | {d.price} | {status}")
    print()


def add_new_drink():
    print("--- THÊM ĐỒ UỐNG MỚI ---")
    code = input("Nhập mã món: ").strip()
    if code == "":
        print("Mã món không được để trống!")
        return

    duplicate = False
    for d in menu:
        if d.code == code:
            duplicate = True
            break
    if duplicate:
        print("Mã món đã tồn tại trong hệ thống!")
        return

    name = input("Nhập tên món: ").strip()
    if name == "":
        print("Tên món không được để trống!")
        return

    price_input = input("Nhập giá bán: ").strip()
    try:
        price = int(price_input)
        if price <= 0:
            print("Giá bán không hợp lệ! (phải lớn hơn 0)")
            return
    except ValueError:
        print("Giá bán không hợp lệ! (phải là số nguyên dương)")
        return

    new_drink = Drink(code, name, price)
    menu.append(new_drink)
    print(f"Thành công: Đã thêm món {new_drink.name} vào thực đơn!")


def update_availability():
    print("--- CẬP NHẬT TRẠNG THÁI KINH DOANH ---")
    code = input("Nhập mã món cần cập nhật: ").strip()
    if code == "":
        print("Mã món không được để trống!")
        return

    flag = None
    for d in menu:
        if d.code == code:
            flag = d
            break

    if not flag:
        print("Không tìm thấy món có mã này!")
        return

    flag.toggle_available()
    if flag.is_available:
        status = "Đang bán"
    else:
        status = "Ngừng bán"

    print(f"Đã cập nhật trạng thái món {flag.code}.")
    print(f"Trạng thái hiện tại: {status}")


def main():
    while True:
        print("=== HỆ THỐNG QUẢN LÝ THỰC ĐƠN RIKKEI COFFEE ===")
        print("1. Xem danh sách đồ uống")
        print("2. Thêm đồ uống mới")
        print("3. Cập nhật trạng thái kinh doanh")
        print("4. Thoát chương trình")
        
        choice = input("Chọn chức năng (1-4): ").strip()

        match choice:
            case "1":
                print_menu_list()

            case "2":
                add_new_drink()

            case "3":
                update_availability()

            case "4":
                print("Cảm ơn bạn đã sử dụng hệ thống quản lý thực đơn Rikkei Coffee!")
                break

            case _:
                print("Lựa chọn không hợp lệ, vui lòng nhập từ 1-4.")

    main()