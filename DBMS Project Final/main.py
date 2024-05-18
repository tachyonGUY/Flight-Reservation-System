from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mbox
from PIL import ImageTk, Image
import mysql.connector
from tkcalendar import DateEntry
from tkinter import font as tkFont

# connect to MySQL database
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="airline"
)
# create cursor object
cursor = db.cursor()

def home_page():
        # Create the GUI
        root = Tk()
        root.title("Airport Mangement System")
        root.geometry("1000x600")
        helv36 = tkFont.Font(family='Helvetica', size=10, weight='bold')

        bg_image = Image.open("airport1.png")
        bg_photo = ImageTk.PhotoImage(bg_image)
        # Set the background image
        bg_label = Label(root, image=bg_photo)
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        # Create a label for the title
        title_label = Label(root, text="Welcome To Flight Booking System", font=("Arial", 30, "bold"), fg="white", bg="#4682B4")
        title_label.config(highlightthickness=2, highlightcolor="blue", bd=0, relief="solid")
        title_label.place(relx=0.6, rely=0.4, anchor=CENTER)
        # Set the anchor to center
        title_label.pack(pady=70, anchor=CENTER)
        # Create the functions for each role
        # Create the user page
        def user_page():
            for widget in root.winfo_children():
                widget.destroy()
            bg_label = Label(root, image=bg_photo)
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)

            # Create a label for the title
            title_label = Label(root, text="User Page", font=("Arial", 20, "bold"), fg="white", bg="#4682B4")
            title_label.config(highlightthickness=2, highlightcolor="blue", bd=0, relief="solid")
            title_label.place(relx=0.5, rely=0.2, anchor=CENTER)
            # Set the anchor to center
            title_label.pack(anchor=CENTER)

            # Create a function to book a ticket
            def book_ticket():

                # Create a new window for booking a ticket
                book_window = Toplevel(root)
                book_window.title("Check Flights")
                book_window.geometry("1000x600")

                # Set the window background color
                bg_label = Label(book_window, image=bg_photo)
                bg_label.place(x=0, y=0, relwidth=1, relheight=1)
                            # Create a label for the title
                title_label = Label(book_window, text="Check Flights", font=("Arial", 20, "bold"), fg="white", bg="#4682B4")
                title_label.config(highlightthickness=2, highlightcolor="blue", bd=0, relief="solid")
                title_label.place(relx=0.5, rely=0.2, anchor=CENTER)
                # Set the anchor to center
                title_label.pack(anchor=CENTER)

                cursor.execute("SELECT CITY FROM AIRPORT")
                city_codes = [row[0] for row in cursor.fetchall()]

                # Create a StringVar to store the selected city
                selected_source = StringVar(book_window)
                selected_source.set(city_codes[0])

                selected_dest = StringVar(book_window)
                selected_dest.set(city_codes[0])

                source_label = Label(book_window, text="SOURCE",font=helv36, bg="#4682B4", fg="white")
                source_option_menu = OptionMenu(book_window, selected_source, *city_codes)

                source_label.pack(pady=2)
                source_option_menu.pack(pady=2)

                dest_label = Label(book_window, text="DESTINATION", font=helv36, bg="#4682B4", fg="white")
                dest_option_menu = OptionMenu(book_window, selected_dest, *city_codes)

                dest_label.pack(pady=2)
                dest_option_menu.pack(pady=2)

                # Create a function to retrieve the available flights and display them in a new window
                def show_flights():
                    source = selected_source.get()
                    dest = selected_dest.get()

                    # Query the database to get all available flights for the given source and destination
                    cursor.execute("SELECT FLIGHT_CODE, AP_NAME, DEPARTURE, DURATION FROM FLIGHT WHERE SOURCE=%s AND DESTINATION=%s", (source, dest))
                    flights = cursor.fetchall()

                    # Create a new window to display the available flights
                    flight_window = Toplevel(book_window)
                    flight_window.title("Available Flights")
                    flight_window.geometry("1000x600")

                    # Create a label and table to display the flight details
                    flight_label = Label(flight_window, text="Available Flights", font=("Arial", 20, "bold"), fg="white", bg="#4682B4")
                    flight_label.config(highlightthickness=2, highlightcolor="blue", bd=0, relief="solid")
                    flight_label.place(relx=0.5, rely=0.1, anchor=CENTER)
                    # Set the anchor to center
                    flight_label.pack(anchor=CENTER)

                    # Create a treeview to display the flight details
                    tree = ttk.Treeview(flight_window, columns=("flight_code","ap_name", "departure", "duration"), show="headings")
                    tree.heading("flight_code", text="Flight Code")
                    tree.heading("ap_name", text="Airport Name")
                    tree.heading("departure", text="Departure Time")
                    tree.heading("duration", text="Duration")
                    for flight in flights:
                        tree.insert("", "end", values=flight)
                    tree.pack(pady=20)

                    # Create a function to book the selected flight
                    def book_flight():
                        # Get the selected flight details
                        selected_flight = tree.selection()
                        if selected_flight:
                            booking_page = Toplevel(book_window)
                            booking_page.title("Booking Page")
                            booking_page.geometry("1000x600")
                            bg_label = Label(booking_page, image=bg_photo)
                            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
                            title_label = Label(booking_page, text="Booking Details", font=("Arial", 20, "bold"), fg="white", bg="#4682B4")
                            title_label.config(highlightthickness=2, highlightcolor="blue", bd=0, relief="solid")
                            title_label.place(relx=0.6, rely=0.4, anchor=CENTER)
                            title_label.pack(anchor=CENTER)

                            flight_code = tree.item(selected_flight)["values"][0]
                            departure = tree.item(selected_flight)["values"][1]
                            arrival = tree.item(selected_flight)["values"][2]

                            # Create labels and entries for the passenger details
                            passport_no_label = Label(booking_page, text="Passport Number",font=helv36,  bg="#4682B4", fg="white")
                            passport_no_entry = Entry(booking_page)
                            passport_no_label.pack(pady=2)
                            passport_no_entry.pack(pady=2)
                            name_label = Label(booking_page, text="Full Name", bg="#4682B4", font=helv36, fg="white")
                            name_entry = Entry(booking_page)
                            name_label.pack(pady=2)
                            name_entry.pack(pady=2)

                            age_label = Label(booking_page, text="Age", bg="#4682B4",font=helv36,  fg="white")
                            age_entry = Entry(booking_page)
                            age_label.pack(pady=2)
                            age_entry.pack(pady=2)

                            gender_label = Label(booking_page, text="Gender", bg="#4682B4",font=helv36,  fg="white")
                            gender_entry = ttk.Combobox(booking_page, values=["Male", "Female", "Other"])
                            gender_entry.config(state="readonly")
                            gender_entry.current(0)
                            gender_label.pack(pady=2)
                            gender_entry.pack(pady=2)

                            address_label = Label(booking_page, text="Address", bg="#4682B4",font=helv36,  fg="white")
                            address_entry = Entry(booking_page)
                            address_label.pack(pady=2)
                            address_entry.pack(pady=2)

                            contact_no_label = Label(booking_page, text="Contact Number", bg="#4682B4",font=helv36,  fg="white")
                            contact_no_entry = Entry(booking_page)
                            contact_no_label.pack(pady=2)
                            contact_no_entry.pack(pady=2)

                            def update_fare(*args):
                                class_prices = {"Economy": 34700, "Business": 112900, "First Class": 276800}
                                flight_class = flight_class_entry.get()
                                fare.set(str(class_prices[flight_class]))

                            fare = StringVar()
                            flight_class_label = Label(booking_page, text="Class", font=helv36, bg="#4682B4", fg="white")
                            flight_class_entry = ttk.Combobox(booking_page, values=["Economy", "Business", "First Class"])
                            flight_class_entry.config(state="readonly")
                            flight_class_entry.current(0)
                            flight_class_entry.bind("<<ComboboxSelected>>", update_fare)
                            flight_class_label.pack(pady=2)
                            flight_class_entry.pack(pady=2)

                            fare_label = Label(booking_page, text="Fare", font=helv36, bg="#4682B4", fg="white")
                            fare_entry = Entry(booking_page, textvariable=fare, state="readonly")
                            fare_label.pack(pady=2)
                            fare_entry.pack(pady=2)
                            # set the initial value of `fare`
                            update_fare()

                            travel_date_label=Label(booking_page, text= "Date Of Travel", bg= '#4682B4',font=helv36,  fg="white")
                            #Create a Calendar using DateEntry
                            travel_date_entry = DateEntry(booking_page, selectmode='day',width= 16, background= "magenta3", foreground= "white",bd=2)
                            travel_date_label.pack(pady=2)
                            travel_date_entry.pack(pady=2)

                            # Create a function to insert the booking into the database
                            def insert_booking():
                                passport_no = passport_no_entry.get()
                                name = name_entry.get()
                                age = age_entry.get()
                                gender = gender_entry.get()
                                contact_no = contact_no_entry.get()
                                address=address_entry.get()
                                flight_class = flight_class_entry.get()
                                travel_date=travel_date_entry.get_date()
                                fare=fare_entry.get()

                                # Insert the booking into the PASSENGER and BOOKING table
                                cursor.execute("INSERT INTO TICKET2 (CLASS, PRICE) VALUES (%s,%s)", (flight_class,fare))
                                db.commit()
                                cursor.execute("INSERT INTO PASSENGER(PASSPORTNO,FLIGHT_CODE, FULL_NAME,ADDRESS, AGE, SEX, PHONE) VALUES (%s, %s, %s,%s, %s, %s, %s)", (passport_no,flight_code, name,address, age, gender, contact_no,))
                                db.commit()
                                cursor.execute("INSERT INTO TICKET1 (SOURCE, DESTINATION, DATE_OF_TRAVEL) VALUES (%s, %s, %s)", (source, dest, travel_date))
                                db.commit()
                                mbox.showinfo("Success", "Ticket booked successfully! Ticket Number: {}".format(cursor.lastrowid))
                                book_window.destroy()

                            # Create a button to submit the booking
                            submit_button =Button(booking_page, text="Confirm",bg="#4682B4", fg="white", font=('Helvetica',10,'bold'),width=10, height=1,  command=insert_booking)
                            submit_button.pack(pady=20)
                        else:
                            mbox.showerror("Error", "No Flight Selcted!")
                            show_flights()

                    book_button =Button(flight_window, text="Book Flight",bg="#4682B4", fg="white", font=('Helvetica',10,'bold'),width=10, height=1, command=lambda:[book_flight(), flight_window.withdraw(),book_window.withdraw()])
                    book_button.pack(pady=20)

                flight_button =Button(book_window, text="Search Flights", bg="#4682B4", fg="white", font=('Helvetica',10,'bold'),width=15, height=1,command=show_flights)
                flight_button.pack(pady=10)
                back_button =Button(book_window, text="Back", bg="#4682B4", fg="white", font=('Helvetica',10,'bold'),width=10, height=1,command=lambda:[book_window.withdraw(), root.deiconify()])
                back_button.pack(pady=10)       
                                                    
            # Create a function to check a ticket
            def check_ticket():
                # Create a new window for checking a ticket
                check_window = Toplevel(root)
                check_window.title("Check Ticket")
                check_window.geometry("1000x600")

                bg_label = Label(check_window, image=bg_photo)
                bg_label.place(x=0, y=0, relwidth=1, relheight=1)

                # Create labels and entries for the flight code and passport number
                ticket_no_label = Label(check_window, text="Ticket No", bg= '#4682B4',font=helv36,  fg="white")
                ticket_no_entry = Entry(check_window)

                ticket_no_label.pack(pady=2)
                ticket_no_entry.pack(pady=2)
                text_label = Label(check_window, text=" OR",bg= '#4682B4',font=helv36,  fg="white")
                text_label.pack(pady=5)

                passport_no_label = Label(check_window, text="Passport No",bg= '#4682B4',font=helv36,  fg="white")
                passport_no_entry = Entry(check_window)
                passport_no_label.pack(pady=2)
                passport_no_entry.pack(pady=2)

                # Create a function to check if the ticket exists in the database
                def check_booking():
                    ticket_no = ticket_no_entry.get()
                    passport_no = passport_no_entry.get()
                    # Check if the booking exists in the PASSENGER3 table
                    cursor.execute("""SELECT t1.TICKET_NUMBER,p.FLIGHT_CODE,t1.SOURCE, t1.DESTINATION, date_format(t1.DATE_OF_TRAVEL,'%b-%m'), t1.SEAT_NO, t2.CLASS, t2.PRICE, p.FULL_NAME, DATE_FORMAT(f.departure, '%H:%i')
                                                FROM ticket1 t1
                                                INNER JOIN ticket2 t2 ON t1.SEAT_NO = t2.SEAT_NO
                                                INNER JOIN passenger p ON t1.PID = p.PID
                                                INNER JOIN flight f ON p.flight_code=f.flight_code
                                                WHERE t1.TICKET_NUMBER =%s OR p.PASSPORTNO=%s""", (ticket_no,passport_no))
                    result = cursor.fetchall()

                    if result:
                        # Create a new window to display Show Details
                        ticket_details = Toplevel(check_window)
                        ticket_details.title("Ticket Details")
                        ticket_details.geometry("800x300")
                        ticket_details.resizable(False, False)


                        bg_img = Image.open("ticket.png")

                        # Convert the image to a tkinter-compatible format
                        bg_photo = ImageTk.PhotoImage(bg_img)

                        # Create a label and set the image as the background
                        bg_label = Label(ticket_details, image=bg_photo)
                        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
                        bg_label.image = bg_photo
                        # Create labels to display the flight details
                        full_name_label = Label(ticket_details, text=f"{result[0][8]}",font=("Arial", 11))
                        flight_code_label = Label(ticket_details, text=f"{result[0][1]}",font=("Arial", 11))
                        source_label = Label(ticket_details, text=f"{result[0][2]}",font=("Arial", 11))
                        destination_label = Label(ticket_details, text=f"{result[0][3]}",font=("Arial", 11))
                        date_of_travel_label = Label(ticket_details, text=f"{result[0][4]}",font=("Arial", 11))
                        seat_no_label = Label(ticket_details, text=f"{result[0][5]}",font=("Arial", 11))
                        departure_time_label = Label(ticket_details, text=f"{result[0][9]}",font=("Arial", 11))
                        full_name_label2 = Label(ticket_details, text=f"{result[0][8]}")
                        flight_code_label2 = Label(ticket_details, text=f"{result[0][1]}")
                        source_label2 = Label(ticket_details, text=f"{result[0][2]}")
                        destination_label2 = Label(ticket_details, text=f"{result[0][3]}")
                        date_of_travel_label2= Label(ticket_details, text=f"{result[0][4]}")
                        seat_no_label2= Label(ticket_details, text=f"{result[0][5]}")
                        departure_time_label2= Label(ticket_details, text=f"{result[0][9]}")

                        flight_code_label.place(x=213, y=186)
                        flight_code_label2.place(x=757, y=203)
                        source_label.place(x=210, y=141)
                        source_label2.place(x=635,y=125)
                        destination_label.place(x=313, y=141)
                        destination_label2.place(x=620, y=165)
                        date_of_travel_label.place(x=325, y=190)
                        date_of_travel_label2.place(x=620, y=203)
                        seat_no_label.place(x=455, y=190)
                        seat_no_label2.place(x=623, y=240)
                        full_name_label.place(x=210, y=97)
                        full_name_label2.place(x=635, y=85)
                        departure_time_label.place(x=410, y=235)
                        departure_time_label2.place(x=705, y=240)

                    else:
                        mbox.showerror("Error", "Ticket not found!")
                # Create a button to submit the check
                submit_button = Button(check_window, text="Check Ticket",bg="#4682B4", fg="white", font=('Helvetica',10,'bold'),width=20, height=1, command=check_booking)
                submit_button.pack(pady=10)
                back_button =Button(check_window, text="Back", bg="#4682B4", fg="white", font=('Helvetica',10,'bold'),width=10, height=1,command=lambda:[check_window.withdraw(), root.deiconify()])
                back_button.pack(pady=10)

            # Create a function to cancel a ticket
            def cancel_ticket():
                # Create a new window for cancelling a ticket
                cancel_window = Toplevel(root)
                cancel_window.title("Cancel Ticket")
                cancel_window.geometry("1000x600")

                bg_label = Label(cancel_window, image=bg_photo)
                bg_label.place(x=0, y=0, relwidth=1, relheight=1)

                # Create labels and entries for the flight code and passport number
                ticket_no_label = Label(cancel_window, text="Ticket No",bg= '#4682B4',font=helv36,  fg="white")
                ticket_no_entry = Entry(cancel_window)

                ticket_no_label.pack(pady=1)
                ticket_no_entry.pack(pady=1)
                text_label = Label(cancel_window, text=" OR",font=helv36)
                text_label.pack(pady=5)

                passport_no_label = Label(cancel_window, text="Passport No",bg= '#4682B4',font=helv36,  fg="white")
                passport_no_entry = Entry(cancel_window)
                passport_no_label.pack(pady=1)
                passport_no_entry.pack(pady=1)

                # Create a function to check if the ticket exists in the database
                def check_booking():
                    ticket_no = ticket_no_entry.get()
                    passport_no = passport_no_entry.get()


                    # Check if the booking exists in the PASSENGER3 table
                    cursor.execute("""SELECT t1.TICKET_NUMBER,p.FLIGHT_CODE,t1.SOURCE, t1.DESTINATION, t1.DATE_OF_TRAVEL, t1.SEAT_NO, t2.CLASS, t2.PRICE, p.FULL_NAME
                                      FROM ticket1 t1
                                      INNER JOIN ticket2 t2 ON t1.SEAT_NO = t2.SEAT_NO
                                      INNER JOIN passenger p ON t1.PID = p.PID
                                      WHERE t1.TICKET_NUMBER =%s OR p.PASSPORTNO=%s""", (ticket_no,passport_no))
                    result = cursor.fetchall()
                    if result:
                        # Create a new window to display the available flights
                        check_ticket = Toplevel(cancel_window)
                        check_ticket.title("Ticket Details")
                        check_ticket.geometry("1000x600")

                        # Create a label and table to display the flight details
                        flight_label = Label(check_ticket, text="View Ticket", font=("Arial", 20, "bold"), fg="white", bg="#4682B4")
                        flight_label.config(highlightthickness=2, highlightcolor="blue", bd=0, relief="solid")
                        flight_label.place(relx=0.5, rely=0.1, anchor=CENTER)
                        # Set the anchor to center
                        flight_label.pack(anchor=CENTER)
                        # Create a treeview to display the flight details
                        tree = ttk.Treeview(check_ticket, columns=("ticket_number","flight_code","source","destination","date_of_travel","seat_no","class","price","full_name" ), show="headings")
                        tree.heading("ticket_number", text="Ticket Number")
                        tree.heading("flight_code", text="Flight Code")
                        tree.heading("source", text="Source")
                        tree.heading("destination", text="Destination")
                        tree.heading("date_of_travel", text="Date Of Travel")
                        tree.heading("seat_no", text="Seat No")
                        tree.heading("class", text="Class")
                        tree.heading("price", text="Price")
                        tree.heading("full_name", text="Full Name")
                        tree.column("ticket_number", minwidth=0, width=100)
                        tree.column("flight_code", minwidth=0, width=100)
                        tree.column("source", minwidth=0, width=100)
                        tree.column("destination", minwidth=0, width=100)
                        tree.column("date_of_travel", minwidth=0, width=100)
                        tree.column("seat_no",minwidth=0, width=100)
                        tree.column("class", minwidth=0, width=100)
                        tree.column("price", minwidth=0, width=100)
                        tree.column("full_name", minwidth=0, width=100)
                        for flight in result:
                            tree.insert("", "end", values=flight)
                        tree.pack(pady=20)
                    else:
                        mbox.showerror("Error", "Ticket not found!")

                    # Create a function to delete the booking from the database
                    def delete_booking():
                        selected_flight = tree.selection()

                        if selected_flight:
                            ticket_no= tree.item(selected_flight)["values"][0]
                            passport_no=tree.item(selected_flight)["values"][4]

                            # Delete the booking from the PASSENGER3 table
                            cursor.execute("""DELETE t1, t2, p
                                            FROM ticket1 t1
                                            INNER JOIN ticket2 t2 ON t1.SEAT_NO = t2.SEAT_NO
                                            INNER JOIN passenger p ON t1.PID = p.PID
                                            WHERE t1.TICKET_NUMBER = %s
                                            OR p.PASSPORTNO = %s""", (ticket_no,passport_no ))
                            db.commit()

                            mbox.showinfo("Success", "Ticket cancelled successfully!")
                        else:
                            mbox.showerror("Error", "No Ticket Selected To Cancel!")
                            delete_booking()

                    # Create a button to submit the cancellation
                    submit_button = Button(check_ticket, text="Cancel Selected Ticket",bg="#4682B4", fg="white", font=('Helvetica',10,'bold'),width=20, height=1, command=lambda:[delete_booking(), check_ticket.withdraw()])
                    submit_button.pack(pady=10)
                # Create a button to submit the check
                submit_button = Button(cancel_window, text="Submit",bg="#4682B4", fg="white", font=('Helvetica',10,'bold'),width=10, height=1, command=check_booking)
                submit_button.pack(pady=10)
                back_button =Button(cancel_window, text="Back", bg="#4682B4", fg="white", font=('Helvetica',10,'bold'),width=10, height=1,command=lambda:[cancel_window.withdraw(), root.deiconify()])
                back_button.pack(pady=5)

            # Create buttons for each function
            book_button = Button(root, text="Book Ticket",bg="#4682B4", fg="white", font=helv36,width=20, height=3, command=lambda:[book_ticket(),root.withdraw()])
            check_button = Button(root, text="Check Ticket",bg="#4682B4", fg="white",font=helv36, width=20, height=3, command=lambda:[check_ticket(),root.withdraw()])
            cancel_button = Button(root, text="Cancel Ticket",bg="#4682B4", fg="white",font=helv36, width=20, height=3, command=lambda:[cancel_ticket(),root.withdraw()])

            book_button.place(relx=0.5, rely=0.4, anchor=CENTER)
            check_button.place(relx=0.5, rely=0.5, anchor=CENTER)
            cancel_button.place(relx=0.5, rely=0.6, anchor=CENTER)
            # back_button.place(relx=0.5, rely=0.7, anchor=CENTER)

        # Create the buttons for each role
        user_button = Button(root, text="Home", width=15, height=2,bg="#4682B4", fg="white",font=helv36,borderwidth=10, command=user_page)
        user_button.place(relx=0.5, rely=0.4, anchor=CENTER)

        # Run the GUI
        root.mainloop()
home_page();
