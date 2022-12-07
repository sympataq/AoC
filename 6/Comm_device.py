

class Comm_device:

    def __init__(self, signal):
        self.signal = signal

    def detect_packet(self, disct=4) -> int :
        for i in range(len(self.signal)):
            s = set(self.signal[i:i+disct])
            if len(s) == disct:
                return i+disct
        return 0

