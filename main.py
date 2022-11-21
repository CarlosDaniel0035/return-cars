carros = []
consumo = []

def entrada_carro():
    while len(carros) < 4:
        cars = input("Modelo do carro:")
        carros.append(cars)
    return cars

def entrada_consumo():
    for i in range(len(carros)):
        valor = int(input("Consumo do veiculo:"))
        consumo.append(valor)
    return valor

def economico():
    if consumo[0] < consumo[1] and consumo [0] < consumo[2] and consumo[0] < consumo[3]:
        return carros[0]

    elif consumo[1] < consumo[2] and consumo[1] < consumo[3]:
        return carros[1]

    elif consumo[2] < consumo[3]:
        return carros[2]

    else:
        return carros[3]


def main():
    entrada_carro()
    entrada_consumo()
    print(economico())
main()