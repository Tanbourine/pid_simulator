from typing import (
    List,

)

import matplotlib.pyplot as plt

class TelemetryMessage():
    def __init__(self, name: str, time_ns: List[int], data: List[float]):
        self.name = name
        self.time_ns = time_ns
        self.data = data

class Plotter():
    def __init__(self):
        self.telemetry_messages = None
        self.fig, self.ax = plt.subplots()

    def plot(self, telemetry_messages: List[TelemetryMessage]):
        self.telemetry_messages = telemetry_messages
        for msg in self.telemetry_messages:
            self.ax.plot(msg.time_ns, msg.data, label=msg.name, marker=".")
        self.ax.legend()
        self.ax.grid()
        plt.show()





def main():
    data = [
        TelemetryMessage("ch1", [0, 1, 2, 3, 4], ["0.0", "0.1", "0.2", "0.3", "0.4"])
    ]
    plotter = Plotter()
    plotter.plot(data)

if __name__ == "__main__":
    main()