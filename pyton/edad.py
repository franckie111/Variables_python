from datetime import datetime


año_actual = datetime.now().year


año_nacimiento = int(input("Por favor, introduce tu año de nacimiento: "))


edad = año_actual - año_nacimiento

print(f"Tu edad es {edad} años")
