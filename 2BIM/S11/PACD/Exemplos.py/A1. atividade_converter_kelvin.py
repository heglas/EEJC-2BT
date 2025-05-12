# Converter Celsius para Kelvin
def converter_para_kelvin(temperaturas_celsius):
    for indice, temp_c in enumerate(temperaturas_celsius, start=1):
        kelvin = temp_c + 273.15
        print(f'Temperatura {indice}: {temp_c}°C = {kelvin:.2f}K')

temperaturas_celsius = [25, 30, 15, 10]
converter_para_kelvin(temperaturas_celsius)
