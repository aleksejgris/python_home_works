from smartphone import Smartphone


catalog = [
    Smartphone("nokia","3310","+79334445566"),
    Smartphone("samsung" , "а300" , "+79229998877"),
    Smartphone("motorola" , "c200" , "+79112220033"),
    Smartphone("simens" , "c45" , "+7900551112244"),
    Smartphone("alkatel" , "310" ,  "+79444444444")
]

for smartphone in catalog:
    print(f"{smartphone.phone_brand} - {smartphone.phone_model} , {smartphone.number}")