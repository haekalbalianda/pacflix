from tabulate import tabulate

class User:
    data = {
    "Shandy": ["Basic Plan", 12, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"]
}

    def __init__(self, username, current_plan, duration_plan):
        self.username = username
        self.current_plan = current_plan
        self.duration_plan = duration_plan

    def check_benefit(self):
        # Cetak informasi pengguna sebelum tabel
        print(f"Username: {self.username}")
        print(f"Current Plan: {self.current_plan}")
        print(f"Duration: {self.duration_plan}")
        print("PacFlix Plan List\n")

        # Header tabel
        headers = ["Basic Plan", "Standard Plan", "Premium Plan", "Services"]

        # Data tabel yang diputar agar sesuai tampilan yang diinginkan
        data = [
            [True, True, True, "Bisa Stream"],
            [True, True, True, "Bisa Download"],
            [True, True, True, "Kualitas SD"],
            [False, True, True, "Kualitas HD"],
            [False, False, True, "Kualitas UHD"],
            [1, 2, 4, "Number of Devices"],
            ["3rd party Movie only", "Basic Plan Content + Sports", 
             "Basic Plan + Standard Plan + PacFlix Original Series", "Jenis Konten"],
            [120000, 160000, 200000, "Harga"]
        ]

        # Cetak tabel dengan format "fancy_grid"
        print(tabulate(data, headers=headers, tablefmt="fancy_grid"))

    def check_plan (self, username)

# Contoh penggunaan
user = User("Haekal", "Basic Plan", 12)
user.check_benefit()
