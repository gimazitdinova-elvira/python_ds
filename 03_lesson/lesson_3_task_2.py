from smartphone import Smartphone

catalog = [
    Smartphone("Samsung", "Galaxy_A52", "+7(999)123‑45‑67"),
    Smartphone("Xiaomi", "Redmi_Note10", "+7(999)765‑43‑21"),
    Smartphone("Apple", "iPhone13", "+7(999)555‑12‑34")
 ]
for smartphone in catalog:
    print(f"{smartphone.brand} - {smartphone.model} . {smartphone.number}")
