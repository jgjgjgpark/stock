class Simulator:
    def __init__(self):
        self.algorithm_number = 1
        pass

    def get_algorithm_no(self):
        self.algorithm_number = int(input("algorithm number?"))
        print("algorithm number: ", self.algorithm_number)

    def run(self):
        print("algorithm number: ", self.algorithm_number)


if __name__ == "__main__":
    simulator = Simulator()
    simulator.get_algorithm_no()
