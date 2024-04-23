from pid import Pid
from motor import Motor, NoisyMotor
from plotting import (
    Plotter,
    TelemetryMessage
)

from signal_generator import StepGenerator


def main():

    generator = StepGenerator(10.0)
    setpoints = generator.generate(100)
    disturbance = (25, 75)
    disturbance_amplitude = 3.0

    for i, setpoint in enumerate(setpoints):
        if (i > disturbance[0] and i < disturbance[1]):
            setpoint = setpoint + disturbance_amplitude


    pid = Pid(
        p=0.90,
        i=0.005,
        d=0.5,
        max_output=10.0)

    # motor = Motor()
    motor = NoisyMotor(
        max_accel=3.0,
        std_dev=0.001)

    feedback_speed = 0.0
    output = [feedback_speed]
    commands = []

    for setpoint_speed in setpoints:
        # Generate next motor request (0 - 100%)
        speed_command = pid.next(setpoint_speed, feedback_speed)
        commands.append(speed_command)

        # Command motor, and see what we get
        feedback_speed = motor.next(speed_command) 

        # Log output
        output.append(feedback_speed)

    print(output)
    plotter = Plotter()
    print(f"Setpoints: {setpoints}")
    print(f"Output: {output}")
    plotter.plot([
        TelemetryMessage("output", [num for num in range(len(output))], output),
        TelemetryMessage("input", [num for num in range(len(setpoints))], setpoints),
        TelemetryMessage("pid", [num for num in range(len(commands))], commands)
        # TelemetryMessage("ch2", [0, 1, 2, 3, 4, 5, 6, 7, 8, 9], output)
    ])

if __name__ == "__main__":
    main()