class Star_Cinema:
    hall_list = []
    
    def entry_hall(self, hall):
        Star_Cinema.hall_list.append(hall)


class Hall(Star_Cinema):
    def __init__(self, row, cols, hall_no) -> None:
        self.__row = row
        self.__cols = cols
        self.__hall_no = hall_no
        self.__seats = dict()
        self.__show_list = []
        self.entry_hall(self)        
    
    def entry_show(self, id, movie_name, time):
        info = (id, movie_name, time)
        self.__show_list.append(info)
        seat_list = [[0] * self.__cols for j in range(self.__row)]
        self.__seats[id] = seat_list

    def book_seats(self, id, seat_point):
        row = seat_point[0]
        col = seat_point[1]
        if id in self.__seats:
            if row < self.__row and col < self.__cols:
                if self.__seats[id][row][col] != 1:
                    self.__seats[id][seat_point[0]][seat_point[1]] = 1
                    print("Thank you for being with us")
                else:
                    print("The seat is already booked")
            else:
                print("The seat point is invalid")
        else:
            print("This Movie is not available right now")
    
    def view_show_list(self):
        print()
        for shows in self.__show_list:
            print(f"movie name : {shows[1]}({shows[0]}) and Time: {shows[2]}")
        print()

    def view_available_seats(self, id):
        if id in self.__seats:
            print()
            for rows in self.__seats[id]:
                print(rows)
            print()
        else:
            print("This Movie is not available right now")



big_cinema = Hall(10, 10, 1)
big_cinema.entry_show(1, "jawan", "2.30")
big_cinema.entry_show(2, "dunki", "4.30")

while True:
    print("Press 1. to View show list")
    print("Press 2. to View available seats")
    print("Press 3. to Book ticket")
    print("Press 4. to Exit")
    choice = input()
    if choice == '1':
        big_cinema.view_show_list()
    elif choice == '2':
        movie_id = int(input("Enter movie id: "))
        big_cinema.view_available_seats(movie_id)
    elif choice == '3':
        movie_id = int(input("Enter movie id: "))
        seat_row = int(input("Enter row: "))
        seat_col = int(input("Enter col: "))
        seat = (seat_row, seat_col)
        big_cinema.book_seats(movie_id, seat)
    else:
        break
