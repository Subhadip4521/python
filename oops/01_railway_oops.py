class RailwayForm:
    formtype="Railway Form"

    def printdata(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

sdApplication= RailwayForm()
sdApplication.name= "subhadip Das"
sdApplication.train= "Rajdhani Express"
sdApplication.printdata()