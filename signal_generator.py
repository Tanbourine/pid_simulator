from numpy import char
from typing import (
    List
)

class Generator():
    def generate(self, length: int) -> List[float]:
        return []

class StepGenerator(Generator):
    def __init__(self, amplitude: float):
        self.amplitude = amplitude

    def generate(self, length: int) -> List[float]:
        output = [0.0]
        for _ in range(1, length):
            output.append(self.amplitude)
        return output
    
# class SineGenerator(Generator):
#     def __init__(self, amplitude: float):
#         self.amplitude = amplitude

#     def generate(self, length: int) -> List[float]:
#         output = [0.0]
#         t = np.linspace(0, 10, 500)
#         f = 4
#         w = 2 * np.pi * f
#         signal = A * np.sin(w * t)


def main():
    generator = StepGenerator(1.0)
    # generator = StepGenerator(1.0)
    output = generator.generate(10)
    print(output)


if __name__ == "__main__":
    main()



    
