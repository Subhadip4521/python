

class train:

    def __init__(self, name, fare, seats):
        self.name = name
        self.fare = fare
        self.seats = seats
    def trainName(self):
        print(f"The name of the train is {self.name}")

    def trainFare(self):
        print(f"The fare of a seat of this train is:Rs {self.fare}")

    def trainSeats(self):
        print(f"Seats left in the train is: {self.seats}")

    @staticmethod
    def greet():
        print("\nHello sir/ma'am,\nWelcome to sdbookmyticket.in\n")

    @staticmethod
    def greet02():
        print("\n*****Thank you sir/ma'am for visiting our site*****\n")

    def bookTicket(self):
        print("\nIf you want to book a ticket, Press 1\nIf you want to cancel your ticket, Press 2\nIf you want to exit, Press 0")
        press = int(input("---> "))
        if press == 0:
            exit(1)
        if press == 1:
            book = int(input("How many seats you want to book: "))
            if self.seats >= book:
                print("Your ticket/tickets has/have been booked.")
                if book == 1:
                    print(f"Your seat number is {self.seats}")
                    self.seats = self.seats-1
                if book > 1:
                    print("Your seat numbers are: ")
                    for i in range(1, book+1):
                        print(f"{i}) {self.seats}")
                        self.seats = self.seats-1

            elif (self.seats < book and self.seats != 0):
                print(f"sorry sir/ma'am, Only {self.seats} are available.")
            elif self.seats == 0:
                print("Sorry no seat is available now!!")

        if press==2:
            cancel= int(input("How many tickets you want to cancel: "))
            if (self.seats==300 and self.seats + cancel>=300):
                print("Invalid input!!!")
            else:
                for j in range(1,cancel+1):
                    seatNo= int(input(f"Put your seat {j}, you want to cancel: "))
                    self.seats=self.seats+1
                print(f"Your {cancel} ticket(s) has/have been canceled.")
                


trainStatus = train("'Rajdhani Express: 48037'", 100, 300)
trainStatus.greet()
trainStatus.trainName()
trainStatus.trainFare()
trainStatus.trainSeats()
i = True
while i:
    trainStatus.bookTicket()
    trainStatus.trainSeats()
    trainStatus.greet02()
