class Casa:
    def __init__(self, ventanas, puertas, techo, habitaciones):
        self.ventanas = ventanas
        self.puertas = puertas
        self.techo = techo
        self.habitaciones = habitaciones

    def describir(self):
        return (f"Casa con {self.ventanas} ventanas, {self.puertas} puertas, "
                f"techo de tipo '{self.techo}', y {self.habitaciones} habitaciones.")

class ViviendaFamiliar(Casa):
    def __init__(self):
        super().__init__(ventanas=8, puertas=3, techo="tejas", habitaciones=4)
        self.patio = True
        self.garaje = True

    def describir(self):
        base = super().describir()
        return f"{base} Tiene patio: {self.patio}, Garaje: {self.garaje}."

class Apartamento(Casa):
    def __init__(self):
        super().__init__(ventanas=4, puertas=1, techo="plano", habitaciones=2)
        self.piso = 5
        self.balcon = True

    def describir(self):
        base = super().describir()
        return f"{base} Está en el piso {self.piso}, Tiene balcón: {self.balcon}."

class Bungalo(Casa):
    def __init__(self):
        super().__init__(ventanas=6, puertas=2, techo="a dos aguas", habitaciones=3)
        self.terraza = True

    def describir(self):
        base = super().describir()
        return f"{base} Tiene terraza: {self.terraza}."

def main():
    casa1 = ViviendaFamiliar()
    casa2 = Apartamento()
    casa3 = Bungalo()

    print(casa1.describir())
    print(casa2.describir())
    print(casa3.describir())

if __name__ == "__main__":
    main()