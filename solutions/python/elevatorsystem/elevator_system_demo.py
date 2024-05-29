from elevator_controller import ElevatorController

def run():
    controller = ElevatorController(3, 5)
    controller.request_elevator(5, 10)
    controller.request_elevator(3, 7)
    controller.request_elevator(8, 2)
    controller.request_elevator(1, 9)


if __name__ == "__main__":
    run()