calculation_to_seconds = 24
Of_Hours = "Hours"

def days_to_units(num_of_days):
    return f"{num_of_days} days are {num_of_days * calculation_to_seconds} {Of_Hours}")


numerodigitado = input("Digite um numero: " )
user_input_number = int(numerodigitado)

calculated_value = days_of_hours(numerodigitado)
print(calculated_value)