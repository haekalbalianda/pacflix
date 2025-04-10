from tabulate import tabulate

class User:
    data = {
        "Shandy": ["Basic Plan", 12, "shandy-2134"],
        "Cahya": ["Standard Plan", 24, "cahya-abcd"],
        "Ana": ["Premium Plan", 5, "ana-2f9g"],
        "Bagus": ["Basic Plan", 11, "bagus-9f92"],
        "Haekal": ["Standard Plan", 12, "hae1345"],
        "Indira": ["Basic Plan", 6, "indira-22gs"]  # Tambah Indira dengan referral code indira-22gs
    }

    def __init__(self, username, duration_plan, current_plan):
        self.username = username
        self.duration_plan = duration_plan
        self.current_plan = current_plan

    def check_benefit(self):
        table = [
            [True, True, True, "Bisa Stream"],
            [True, True, True, "Bisa Download"],
            [True, True, True, "Kualitas SD"],
            [False, True, True, "Kualitas HD"],
            [False, False, True, "Kualitas UHD"],
            [1, 2, 4, "Number of Devices"],
            ["3rd party Movie only", "Basic Plan Content + Sports", "Basic Plan + Standard Plan + PacFlix Original Series", "Jenis Konten"],
            [120_000, 160_000, 200_000, "Harga"]
        ]
s
        headers = ["Basic Plan", "Standard Plan", "Premium Plan", "Services"]
        print("PacFlix Plan List")
        print("")
        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

    def check_plan(self):
        for key, value in self.data.items():
            if key == self.username:
                print(f"Plan: {value[0]}")
                print(f"Duration: {value[1]} Bulan")
                print("")
                
                try:
                    if value[0] == "Basic Plan":
                        table = [
                            [True, "Bisa Stream"],
                            [True, "Bisa Download"],
                            [True, "Kualitas SD"],
                            [False, "Kualitas HD"],
                            [False, "Kualitas UHD"],
                            [1, "Number of Devices"],
                            ["3rd party Movie only", "Jenis Konten"],
                            [120_000, "Harga"]
                        ]

                        headers = ["Basic Plan", "Services"]
                        print(f"{value[0]} PacFlix Benefit List")
                        print("")
                        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

                    elif value[0] == "Standard Plan":
                        table = [
                            [True, "Bisa Stream"],
                            [True, "Bisa Download"],
                            [True, "Kualitas SD"],
                            [True, "Kualitas HD"],
                            [False, "Kualitas UHD"],
                            [2, "Number of Devices"],
                            ["Basic Plan + Sports (F1, Football, Basketball)", "Jenis Konten"],
                            [160_000, "Harga"]
                        ]

                        headers = ["Standard Plan", "Services"]
                        print(f"{value[0]} PacFlix Benefit List")
                        print("")
                        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

                    elif value[0] == "Premium Plan":
                        table = [
                            [True, "Bisa Stream"],
                            [True, "Bisa Download"],
                            [True, "Kualitas SD"],
                            [True, "Kualitas HD"],
                            [True, "Kualitas UHD"],
                            [4, "Number of Devices"],
                            ["Basic Plan + Standard Plan + PacFlix Original Series or Movies", "Jenis Konten"],
                            [200_000, "Harga"]
                        ]

                        headers = ["Premium Plan", "Services"]
                        print(f"{value[0]} PacFlix Benefit List")
                        print("")
                        print(tabulate(table, headers=headers, tablefmt="fancy_grid"))

                    else:
                        raise Exception("Plan didn't exist")
                except Exception as e:
                    print(f"Error: {str(e)}")
                return
        print(f"User {username} not found in the database.")

    def upgrade_plan(self, current_plan, new_plan):
        if new_plan != self.current_plan:
            if self.duration_plan > 12:
                if new_plan == "Basic Plan":
                    total = 120_000 - (120_000 * 0.05)
                    self.current_plan = new_plan
                    print(f"Upgrade ke Basic Plan berhasil! Biaya: Rp {total}")
                    return total
                elif new_plan == "Standard Plan":
                    total = 160_000 - (160_000 * 0.05)
                    self.current_plan = new_plan
                    print(f"Upgrade ke Standard Plan berhasil! Biaya: Rp {total}")
                    return total
                elif new_plan == "Premium Plan":
                    total = 200_000 - (200_000 * 0.05)
                    self.current_plan = new_plan
                    print(f"Upgrade ke Premium Plan berhasil! Biaya: Rp {total}")
                    return total
                else:
                    raise Exception("Plan didn't exist")
            else:
                if new_plan == "Basic Plan":
                    total = 120_000
                    self.current_plan = new_plan
                    print(f"Upgrade ke Basic Plan berhasil! Biaya: Rp {total}")
                    return total
                elif new_plan == "Standard Plan":
                    total = 160_000
                    self.current_plan = new_plan
                    print(f"Upgrade ke Standard Plan berhasil! Biaya: Rp {total}")
                    return total
                elif new_plan == "Premium Plan":
                    total = 200_000
                    self.current_plan = new_plan
                    print(f"Upgrade ke Premium Plan berhasil! Biaya: Rp {total}")
                    return total
                else:
                    raise Exception("Plan didn't exist")
        else:
            print("You are already on this plan.")
            return 0

class NewUser:
    check_list = []

    def __init__(self, username):
        self.username = username
        self.current_plan = None

    def convert_data_to_list(self, data):
        self.check_list = []
        for user_data in data.values():
            referral_code = user_data[2]
            self.check_list.append(referral_code)
        return self.check_list

    def pick_plan(self, new_plan, referral_code):
        if referral_code in self.check_list:
            if new_plan == "Basic Plan":
                total = 120_000 - (120_000 * 0.04)
                self.current_plan = new_plan
                print(f"Berhasil memilih {new_plan} dengan referral code {referral_code}!")
                print(f"Biaya setelah diskon: Rp {total}")
                return total
            elif new_plan == "Standard Plan":
                total = 160_000 - (160_000 * 0.04)
                self.current_plan = new_plan
                print(f"Berhasil memilih {new_plan} dengan referral code {referral_code}!")
                print(f"Biaya setelah diskon: Rp {total}")
                return total
            elif new_plan == "Premium Plan":
                total = 200_000 - (200_000 * 0.04)
                self.current_plan = new_plan
                print(f"Berhasil memilih {new_plan} dengan referral code {referral_code}!")
                print(f"Biaya setelah diskon: Rp {total}")
                return total
            else:
                print("Plan doesn't exist")
                return None
        else:
            raise Exception(f"Referral Code '{referral_code}' doesn't exist")

# check user 1
user_1 = User("Shandy", 12, "Basic Plan")
user_1.check_benefit()
user_1.check_plan(user_1.username)
user_1.upgrade_plan(user_1.current_plan, "Standard Plan")

# check user 2
user_2 = User("Haekal", 24, "Premium Plan")
user_2.check_benefit()
user_2.check_plan(user_2.username)

# check new user faizal
faizal = NewUser("faizal_icikiwir")
faizal.convert_data_to_list(User.data)
faizal.pick_plan("Basic Plan", "indira-22gs")