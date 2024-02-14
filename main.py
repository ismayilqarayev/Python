class App:
    def __init__(self):
        super().__init__()
        print("Input a number, please, and press Enter:")
        self.number = int(input())

        while self.number == 5:
            self.number += 1
            print(f"number = {self.number}")

    def get(self):
        if self.number == 6:
            self.number += 5
            print(f"Updated number = {self.number}")

    def mainloop(self):
        pass

if __name__ == "__main__":
    app = App()
    app.get()  # Call the 'get' method to perform the update if needed
    app.mainloop()
