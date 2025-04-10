class DataIntegrity:
    def __init__(self, data):
        self.data = data
        self.errors = []  # Gunakan self.errors (bukan self.error)

    def check_null_values(self, column):
        for i, row in enumerate(self.data, start=1):
            if row.get(column) is None:
                self.errors.append(f"Null value in column '{column}' at record {i}")  

    def check_negative_values(self, column):
        for i, row in enumerate(self.data, start=1):
            value = row.get(column, None)  # Gunakan get() agar aman
            if value is not None and value < 0:
                self.errors.append(f"Negative value in column '{column}' at record {i}")

    def check_value_range(self, column, min_value, max_value):
        for i, row in enumerate(self.data, start=1):
            value = row.get(column, None)  # Gunakan get() agar tidak error
            if value is not None and not (min_value <= value <= max_value):
                self.errors.append(f"Out of range in column '{column}' at record {i}")

    def validate_data(self):
        return {"issues_found": len(self.errors), "issues": self.errors}

# Input Data
data = [
    {"id": 1, "sales": 100, "region": "North"},
    {"id": 2, "sales": -50, "region": None},
    {"id": 3, "sales": 200, "region": "East"}
]

# Membuat objek dan menjalankan validasi
integrity = DataIntegrity(data)
integrity.check_null_values(column="region")  # ✅ Nama kolom benar
integrity.check_negative_values(column="sales")  # ✅ Nama kolom benar
integrity.check_value_range(column="sales", min_value=0, max_value=50)

# Menampilkan hasil validasi
data_integrity = integrity.validate_data()
print(data_integrity)
