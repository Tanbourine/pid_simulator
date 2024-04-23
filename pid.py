import time

class Pid():
    def __init__(self, p: float, i: float, d: float, max_output: float):
        self.p = p
        self.i = i
        self.d = d
        self.max_output = max_output
        self.start_timestamp_ms = self._now_ms()
        self.accumulated_error = 0
        
        # Previous iteration's error stored for use in future calculations
        # If this is None, this means it is the first iteration
        self.previous_error = None


    def next(self, setpoint: float, feedback: float) -> float:
        error = setpoint - feedback
        p_component = self._calcuate_p(error)
        i_component = self._calculate_i(error)
        d_component = self._calculate_d(error)
        output = feedback + p_component + i_component + d_component
        # if output > self.max_output:
        #     output = self.max_output

        print(f"Output: {output} || Setpoint: {setpoint} || Feedback: {feedback} || Error: {error} || P: {p_component} || I: {i_component} || D: {d_component}")
        return output

    def _calcuate_p(self, error) -> float:
        # P term * error
        return error * self.p

    def _calculate_i(self, error) -> float:
        # I term * error * duration
        self.accumulated_error += error
        return self.i * self.accumulated_error

    def _calculate_d(self, error):
        if not self.previous_error:
            self.previous_error = 0
            return 0
        
        return - (self.d * (error - self.previous_error))
        
        

    
    def _now_ms(self) -> int:
        return int(time.time() * 1000)
