from mailing import Mailing
from address import Address

to_address = Address("152138" , "Москва" , "Ленина", "10", "20")

from_address = Address("138152" , "Ленинград", "Ленина", "10" , "20")


mailing = Mailing(30,to_address,from_address, "40")


print(mailing)