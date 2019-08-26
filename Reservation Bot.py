import pickle
import sys
import random


class train:
    def __init__(self,name = '', num = 0, arr_time = '',dep_time = '',src = '' ,des = '',day_of_travel = '',seat_available_in_1AC = 0,seat_available_in_2AC = 0,seat_available_in_SL = 0,fare_1ac = 0, fare_2ac = 0 ,fare_sl = 0):
        self.name = name
        self.num = num
        self.arr_time = arr_time
        self.dep_time = dep_time
        self.src = src
        self.des = des
        self.day_of_travel = day_of_travel
        self.seats = {'1AC' : seat_available_in_1AC, '2AC': seat_available_in_2AC,'SL': seat_available_in_SL}
        self.fare = {'1AC' : fare_1ac,'2AC' : fare_2ac ,'SL' : fare_sl}
    def print_seat_availablity(self):
    	print("No. of seats available in 1AC :- "+str(self.seats['1AC']))
    	print("No. of seats available in 2AC :- "+str(self.seats['2AC']))
    	print("No. of seats available in SL :- "+str(self.seats['SL']))
    def check_availabilty(self,coach='',ticket_num = 0):
    	coach = coach.upper()
    	if coach not in ('SL','1AC','2AC'):
    		print_seat_availablity()
    		coach = input("Enter the coach(1AC/2AC/SL) :-")
    	else:
    		if self.seats[coach] == 0:
    			return False
    		elif self.seats[coach] >= ticket_num:
    			return True
    		else:
    			return False
    def book_ticket(self,coach = '',no_of_tickets = 0):
    	self.seats[coach] -= no_of_tickets
    	return True


class user:
	def __init__(self,uid = 0,name = '',hometown = '',cell_num = '',pwd = ''):
		self.uid = uid
		self.name = name
		self.hometown = ''
		self.cell_num = ''
		self.pwd = pwd
		self.history = {}
 
 # def book_ticket(self)

class ticket:
	def __init__(self,train,user,ticket_num):
		self.pnr = str(train.num)+str(user.uid)+str(random.randint(100,999))
		self.train_name = train.name
		self.user_name = user.name
		self.ticket_num = ticket_num
		user.history.update({self.pnr : self})
		ticket_dict.update({self.pnr : self})



def book_ticket():
	try:
		uid = int(input("Enter your User ID = "))
	except ValueError:
		print("\nEnter valid User ID\n")
		book_ticket()
	pwd = input("Enter your password :- ")
	if uid in users and users[uid].pwd == pwd:		
		print("Welcome ",users[uid].name," !")
	else:
		print("\n\nNo such user ID / Wrong Password !\n\n")
		menu()
	check_seat_availabilty('p')
	try:
		choice = int(input("Enter the train number :- "))
	except ValueError:
		print("\n\nPlease properly enter the train number.\n\n")
		menu()
		book_ticket()
	if choice in trains:
			trains[choice].print_seat_availablity()
	else:
		print("\n\nEnter valid train number\n\n")
		menu()
	coach = input("Enter the coach :- ")
	coach = coach.upper()
	if coach in ('SL','1AC','2AC'):	
		ticket_num = int(input("Enter the number of tickets :- "))
		if trains[choice].check_availabilty(coach,ticket_num):
			prompt = input("Confirm Ticket(s) (y/n) ? :- ")
			if prompt == 'y':
				trains[choice].book_ticket(coach,ticket_num)
				print("Booking Successful!\n\n")
				tick = ticket(trains[choice],users[uid],ticket_num)
				print("Please note PNR number :- ",tick.pnr,"\n\n")
				menu()
			else:
				print("Exiting...\n\n")
				menu()
		else:
			print(ticket_num," tickets not available")
			menu()
	else:
		print("\n\nEnter proper coach\n\n")
		menu()

def cancel_ticket():
	pnr = input("Enter the PNR number :- ")
	if pnr in ticket_dict:
		check_pnr(pnr)
		choice = input("Do you want to cancel(y/n):- ")
		if choice == 'y':
			uid = int(input("Enter your id :- "))
			pwd = input("Enter the password :- ")
			if uid in users:
				if users[uid].pwd == pwd:
					print("\n\nTicket Cancelled.\n\n")
				else:
					print("\nEnter the right password\n")
			else:
				print("\nNo such user.Ticket not cancelled\n")
				menu()
		else:
			print("\nTicket not cancelled\n")
			menu()
	menu()



def check_seat_availabilty(flag = ''):
	src = input("Enter the source station:- ")
	des = input("Enter the destination station:- ")
	flag_2 = 0
	for i in trains:
		if trains[i].src == src and trains[i].des == des:
			print("Train Name :- ",trains[i].name ," " ,"Number ",trains[i].num ," ","Day of Travel :- ",trains[i].day_of_travel)
			flag_2 += 1
	if flag_2 == 0:
		print("\n\nNo trains found between the stations you entered.\n\n")
		menu()
	if flag == '':
		choice = int(input("Enter the train number :- "))
		trains[choice].print_seat_availablity()
		menu()
	else:
		pass

def check_pnr(pnr_num = ''):
	if pnr_num == '':
		pnr_num = input("Enter the PNR number :- ")
	if pnr_num in ticket_dict:
		print("User name:- ",ticket_dict[pnr_num].user_name)
		print("Train name:- ",ticket_dict[pnr_num].train_name)
		print("No. of Tickets Booked :- ",ticket_dict[pnr_num].ticket_num)
	else:
		print("\nNo such PNR number exists.\n")
	# menu()

def create_new_acc():
	user_name = input("Enter your user name:- ")
	pwd = input("Enter your password :- ")
	uid = random.randint(1000,9999)
	hometown = input("Enter your hometown :- ")
	cell_num = input("Enter your phone number :- ")
	u = user(uid, user_name, hometown, cell_num, pwd)
	print("Your user ID is :- ",uid)
	users.update({u.uid : u})
	menu()



t1 = train('chennai',101,'12:30','22:12','chen','hyd','Wed',100,100,100,2205,320,234)
t2 = train('hyderbad',102,'02:34','23:10','hyd','ban','Mon',100,100,100,3434,435,234)
t3 = train('bangalore',103,'11:56','03:12','ban','pon','Fri',100,100,100,455,325,533)
t4 = train('pondicherry',104,'09:56','15:10','pon','coi','Fri',100,100,100,2500,320,500)
t5 = train('coimbatore',105,'03:50','08:12','coi','chen','Fri',100,100,100,399,325,502)

trains = {t1.num:t1,t2.num:t2,t3.num:t3,t4.num:t4,t5.num:t5}
ticket_dict = {}

print("--------------------------------------------------Welcome to R.A.I.C.E---------------------------------------------------------------")
print("--------------------------------------------------Welcome to Railway Reservation Portal----------------------------------------------")
print("-------------------------------------------------------------------------------------------------------------------------------------")


def menu():
	print("Hi there i am R.A.I.C.E ..!")
	print("What is your name?")
	print("What can i do for you?")
	print("1.Book Ticket")
	print("2.Cancel Ticket")
	print("3.Check PNR ")
	print("4.Check seat availibity")
	print("5.Create new account")
	print("6.Check previous transaction")
	try:
		option = int(input("Option = "))
	except ValueError:
		print("\n\nPlease enter a valid option.\n\n")
		menu()
	if option == 1:
		book_ticket()
	elif option == 2:
		cancel_ticket()
	elif option == 3:
		check_pnr()
	elif option == 4:
		check_seat_availabilty()
	elif option == 5:
		create_new_acc()

menu()
