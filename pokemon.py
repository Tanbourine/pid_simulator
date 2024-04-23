from typing import (
    List
)
class Pokemon():
    def __init__(self, name, level=0, type="Unknown"):
        self.name = name
        self.level = level
        self.type = type

    def __repr__(self):
        return f"{self.name} || Level: {self.level} || Type: {self.type}"

    def level_up(self) -> None:
        self.level += 1
        print(f"{self.name} is now level {self.level}!")

    def strong_against(self) -> List[str]:
        return []

    def weak_against(self) -> List[str]:
        return []

class ElectricPokemon(Pokemon):
    def __init__(self, name, level):
        super().__init__(name, level, type="Electric")

    def strong_against(self) -> List[str]:
        return ["Water", "Flying"]

    def weak_against(self) -> List[str]:
        return ["Ground"]

    def level_up(self):
        if self.level > 30 and "THUNDERSTONE" in self.inventory:
            self.evolve()

class FirePokemon(Pokemon):
    def __init__(self, name, level):
        super().__init__(name, level, type="Fire")

    def strong_against(self) -> List[str]:
        return ["Water", "Flying"]

    def weak_against(self) -> List[str]:
        return ["Ground"]



def main():
    pikachu = ElectricPokemon(
        name="Pikachu",
        level=10,
    )

    charmander = Pokemon(
        name="Charmander",
        level=8,
        type="Fire"
    )

    squirtle = Pokemon(
        name="Squirtle",
        level=6,
        type="Water"
    )

    pokemans = [
        pikachu,
        charmander,
        squirtle
    ]

    for pokemon in pokemans:
        print(pokemon)

    print("===========================")

    for pokemon in pokemans:
        pokemon.level_up()
        print(pokemon)
    
        # print(f"{pokemon.name}: Level: {pokemon.level} || Type: {pokemon.type}")

if __name__ == "__main__":
    main()