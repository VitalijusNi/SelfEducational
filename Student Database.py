from tkinter import *
from tkinter import ttk
import sqlite3
import re


class StudentDB:
    db_conn = 0
    theCursor = 0
    curr_student = 0

    def quit_app(self, event=None):
        root.quit()

    def setup_db(self):

        self.db_conn = sqlite3.connect('studentDB.db')

        self.theCursor = self.db_conn.cursor()

        try:
            self.db_conn.execute(
                "CREATE TABLE if not exists Students(ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, FName TEXT NOT NULL, " +
                "LName TEXT NOT NULL, Course TEXT NOT NULL, Phone TEXT NOT NULL, Email TEXT NOT NULL);")

            self.db_conn.commit()

        except sqlite3.OperationalError:
            print("ERROR : Table not created")


    def valid_number(self, event=None):
        regex = self.phone_entry_value.get()
        inccorect_numb = "Incorrect number"

        if re.search("[\w+370]-\d{8}", regex):
            return regex
        else:
            return inccorect_numb


    def valid_email(self, event=None):
        regexemail = self.email_entry_value.get()
        inccorect_email = "Email Not Valid"

        if re.search(r"[\w.+%_-]+@[a-zA-Z0-9-]+\.[\w+\.]+", regexemail):
            return regexemail
        else:
            return inccorect_email


    def stud_submit(self):

        self.db_conn.execute("INSERT INTO Students (FName, LName, Course, Phone, Email) " +
                             "VALUES ('" +
                             self.fn_entry_value.get() + "', '" +
                             self.ln_entry_value.get() + "', '" +
                             self.cour_entry.get() + "', '" +
                             self.valid_number() + "', '" +
                             self.valid_email() + "')")

        self.fn_entry.delete(0, "end")
        self.ln_entry.delete(0, "end")
        self.phone_entry.delete(0,"end")
        self.phone_entry_value.set("+370-")
        self.email_entry.delete(0, "end")

        # Updating list box
        self.update_listbox()
        self.db_conn.commit()


    def update_listbox(self):

        self.list_box.delete(0, END)

        try:
            result = self.theCursor.execute("SELECT ID, FName, LName, Course, Phone, Email FROM Students")

            for row in result:
                stud_id = row[0]
                stud_fname = row[1]
                stud_lname = row[2]
                course = row[3]
                phone = row[4]
                email = row[5]

                self.list_box.insert(stud_id,
                        stud_fname + " " + stud_lname + "   Course:  " + course + "    Phone:  " + phone + "    Email:  " + email)

        except sqlite3.OperationalError:
            print("The Table Doesn't Exist")

        except:
            print("1: Couldn't Retrieve Data From Database")


    def load_student(self, event=None):

        lb_widget = event.widget
        index = str(lb_widget.curselection()[0] + 1)

        self.curr_student = index

        try:
            result = self.theCursor.execute("SELECT ID, FName, LName, Course, Phone, Email FROM Students WHERE ID=" + index)

            for row in result:
                stud_id = row[0]
                stud_fname = row[1]
                stud_lname = row[2]
                course = row[3]
                phone = row[4]
                email = row[5]

                self.fn_entry_value.set(stud_fname)
                self.ln_entry_value.set(stud_lname)
                self.cour_entry.set(course)
                self.phone_entry_value.set(phone)
                self.email_entry_value.set(email)

        except sqlite3.OperationalError:
            print("The Table Doesn't Exist")

        except:
            print("2 : Couldn't Retrieve Data From Database")


    def update_student(self, event=None):

        try:
            self.db_conn.execute("UPDATE Students SET FName='" +
                                 self.fn_entry_value.get() +
                                 "', LName='" +
                                 self.ln_entry_value.get() +
                                 "', Course='" +
                                 self.cour_entry.get() +
                                 "', Phone='" +
                                 self.valid_number() +
                                 "', Email='" +
                                 self.valid_email() +
                                 "' WHERE ID=" +
                                 self.curr_student)

            self.db_conn.commit()

        except sqlite3.OperationalError:
            print("Database couldn't be Updated")

        self.update_listbox()

    def __init__(self, root):

        root.title("Student Database")
        root.geometry("480x410")
        root.resizable(width=False, height=False)
        
            # ----- 1st Row -----
        fn_label = Label(root, text="First Name")
        fn_label.grid(row=0, column=0, padx=10, pady=10, sticky=W)

        self.fn_entry_value = StringVar(root, value="")
        self.fn_entry = ttk.Entry(root,
                                  textvariable=self.fn_entry_value)
        self.fn_entry.grid(row=0, column=1, padx=10, pady=10, sticky=W)

            # ----- 2nd Row -----
        ln_label = Label(root, text="Last Name")
        ln_label.grid(row=1, column=0, padx=10, pady=10, sticky=W)

        self.ln_entry_value = StringVar(root, value="")
        self.ln_entry = ttk.Entry(root,
                                  textvariable=self.ln_entry_value)
        self.ln_entry.grid(row=1, column=1, padx=10, pady=10, sticky=W)

            # ----- 3rd Row -----
        self.submit_button = ttk.Button(root,
                                        text="Submit",
                                        command=lambda: self.stud_submit())
        self.submit_button.grid(row=2, column=0,
                                padx=10, pady=10, sticky=W)

        self.update_button = ttk.Button(root,
                                        text="Update",
                                        command=lambda: self.update_student())
        self.update_button.grid(row=2, column=1,
                                padx=10, pady=10)

            # ----- Quit Button ----

        self.submit_button = ttk.Button(root,
                                        text="Quit",
                                        command=lambda: self.quit_app())
        self.submit_button.grid(row=4, column=3,
                                padx=10, pady=10, sticky=SE)

            # ---- Additional information box ---
            # ADD A VALUES FOR COURSES
        lb_frame = LabelFrame(root, text="Additional Information",
                              padx=5, pady=5)
        cour_spinbox_name = Label(lb_frame, text="Course")
        cour_spinbox_name.grid()

        self.cour_entry = StringVar()
        self.cour_spinbox = Spinbox(lb_frame, from_=1, to=4, textvariable=self.cour_entry)
        self.cour_spinbox.grid(row=0, column=3, padx=10, pady=10, sticky=W)
        phone_label = Label(lb_frame, text="Phone")
        phone_label.grid()

        self.phone_entry_value = StringVar(root, value="+370-")
        self.phone_entry = ttk.Entry(lb_frame,
                                  textvariable=self.phone_entry_value)
        self.phone_entry.grid(row=1, column=3, padx=10, pady=10, sticky=W)

        email_label = Label(lb_frame, text="E-mail")
        email_label.grid()

        self.email_entry_value = StringVar(root, value="")
        self.email_entry = ttk.Entry(lb_frame,
                                     textvariable=self.email_entry_value)
        self.email_entry.grid(row=2, column=3, padx=10, pady=10, sticky=W)

        lb_frame.grid(row=0, rowspan=3, column=3, padx=10, pady=10, sticky=E)

            # ----- 4th Row -----

        self.list_box = Listbox(root)

        self.list_box.bind('<<ListboxSelect>>', self.load_student)

        self.list_box.insert(1, "Students Here")

        self.list_box.grid(row=3, column=0, columnspan=4, padx=10, pady=10, sticky=W + E)

        self.setup_db()

        self.update_listbox()


root = Tk()
studDB = StudentDB(root)
root.mainloop()