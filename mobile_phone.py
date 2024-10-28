
class Call:
    def __init__(self):
        print("Call initialized")

    def dial_number(self, to_number):
        for number in to_number:
            print(f"Dialing {number}")

    def start_talking(self):
        print(f"Go ahead, talk")

    def make_call(self, to_number):
        print(f"Calling number {to_number}")
        self.dial_number(to_number)
        self.start_talking()

class GPS:
    lat = 61.12345
    lon = 40.23455

    def __init__(self):
        print("GPS initialized")

class Camera:
    def __init__(self):
        self.photo = ""
        print("Camera initialized")

    def take_photo(self, file_name = "image.jpg"):
        # call internal camera api to take photos
        print("Click, photo taken")
        self.photo = file_name

class Storage:
    def __init__(self):
        self.files = []

    def store_file(self, file):
        self.files.append(file)

    def show_all_files(self):
        for file in self.files:
            print(file)

class MobilePhone(Call, GPS, Camera, Storage):
    def __init__(self, brand, price):
        self.brand = brand
        self.price = price
        Camera.__init__(self)
        Storage.__init__(self)

        print("MobilePhone initialized")
        #super().__init__()

phone = MobilePhone("Nokia", 200)
phone.make_call("040-1231234")

print(phone.lat)
print(phone.lon)

print(f"Photo: {phone.photo}")
phone.take_photo()
print(f"Photo: {phone.photo}")

phone.store_file(phone.photo)
phone.take_photo("cat.jpg")
phone.store_file(phone.photo)

phone.take_photo("dog.jpg")
phone.store_file(phone.photo)

phone.show_all_files()