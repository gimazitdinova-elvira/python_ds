from address import Address
from Mailing import Mailing

to_address = Address("101000", "Москва", "Тверская", "15", "42")
from_address = Address(" 190000", "Санкт‑Петербург", "Невский проспект", "27", "10")

Mailing = Mailing(to_address = to_address, from_address = from_address, cost = 350.0, track = 123456789)

track_info = f"Отправление {Mailing.track} из "
from_info = f"{from_address.index} {from_address.city} {from_address.street} {from_address.house} - {from_address.apartment}"
to_info = f" в {to_address.index} {to_address.city} {to_address.street} {to_address.house} - {to_address.apartment}"
cost_info = f". Стоимость {Mailing.cost} рублей."
print(track_info + from_info + to_info + cost_info)