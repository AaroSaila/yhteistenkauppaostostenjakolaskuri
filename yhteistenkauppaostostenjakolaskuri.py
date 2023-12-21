class Ostos:
    ostokset = []
    def __init__(self, hinta, tyyppi):
        self.hinta = float(hinta)
        self.tyyppi = int(tyyppi)  # int, 1=yhteinen, 2=toisen, 3=oma
        Ostos.ostokset.append(self)

    def laske_hinnat(self):
        kokonaishinta = 0.0
        oma_hinta = 0.0
        toisen_hinta = 0.0
        for ostos in Ostos.ostokset:
            kokonaishinta += ostos.hinta
            match(ostos.tyyppi):
                case 1:
                    toisen_hinta += ostos.hinta / 2
                    oma_hinta += ostos.hinta / 2
                case 2:
                    toisen_hinta += ostos.hinta
                case 3:
                    oma_hinta += ostos.hinta
                case _:
                    print("ERROR")
                    exit()
        print(f"Kokonaishinta: {kokonaishinta}\nOma hinta: {oma_hinta}\nToisen hinta: {toisen_hinta}")


print("Anna tuotteen hinta ja tyyppi. -1 poistuaksesi. Syötä tyhjä rivi, kun olet valmis. (1=yhteinen, 2=toisen, 3=oma)")
option = -3
while option != -1:
    option = input()
    match(option):
        case "-1":
            exit()
        case "":
            Ostos.laske_hinnat(Ostos)
            exit()
        case _:
            option = option.split()
            Ostos(option[0], option[1])
