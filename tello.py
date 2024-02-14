from djitellopy import Tello
import time

dron = Tello()
dron.connect()
dron.takeoff()
time.sleep(3)
energy = dron.get_battery()
print(energy)
time.sleep(3)
dron.move_forward(100)
dron.land()


class App:
    def __init__(self):
        super().__init__()

        self.drone = Tello()
        self.drone.connect()
        self.drone.takeoff()
        time.sleep(3)
        energy = self.drone.get_battery()
        print(energy)
        time.sleep(3)
        self.drone.move_forward(100)
        self.drone.land()

    def mainloop(self):
        pass


if __name__ == "__main__":
    app = App()
    app.mainloop()