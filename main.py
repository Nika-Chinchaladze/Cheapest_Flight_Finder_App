from tkinter import *
from tkinter import ttk, messagebox
from tkcalendar import Calendar
from PIL import Image, ImageTk
from datetime import datetime
from Tequila_Class import TequilaFinder
from Files_Class import FileDealer
from Message_Class import SendEmail
from Cities_Class import CITIES

FONT = ("Courier", 25, "bold")
BNT_FONT = ("Helvetica", 12, "bold")
LB_FONT = ("Helvetica", 13, "normal")
CURRENCY = ("USD", "GBP", "EUR")


class PublicApp:
    def __init__(self, window):
        self.window = window
        self.window.title("Cheap Flight Finder")
        self.window.geometry("1360x800")
        self.window.state("zoomed")
        # extra variables:
        self.file_tool = FileDealer()
        self.symbol = None
        self.special_answer = None
        self.letter = None
        self.today = datetime.now()
        self.new_user_name = StringVar()
        self.new_user_surname = StringVar()
        self.new_user_email = StringVar()
        # info variables:
        self.chosen_city = StringVar()
        self.chosen_price = StringVar()
        self.chosen_currency = StringVar()
        self.minimum_duration = StringVar()
        self.maximum_duration = StringVar()

        # ========================================= TOP FRAME ============================================ #
        self.top_frame = Frame(self.window, bd=5, highlightthickness=5, relief=RIDGE, pady=5)
        self.top_frame.place(x=10, y=10, width=1340, height=70)

        self.header = Label(self.top_frame, text="Cheapest Flight Finder From TBILISI", font=FONT, justify="center",
                            fg="forest green")
        self.header.pack()

        # ========================================= RIGHT FRAME =========================================== #
        self.right_frame = Frame(self.window, bd=3, highlightthickness=3, relief=RIDGE)
        self.right_frame.place(x=1000, y=80, width=347, height=610)

        self.extract_button = Button(self.right_frame, text="Extract", font=BNT_FONT, justify="center",
                                     command=self.extract_active_method)
        self.extract_button.place(x=5, y=10, width=100, height=30)

        self.chosen_label = Label(self.right_frame, text="", font=LB_FONT, justify="center", bd=1, highlightthickness=1,
                                  relief=RIDGE)
        self.chosen_label.place(x=110, y=10, width=220, height=30)

        self.new_name = Label(self.right_frame, text="Name", font=LB_FONT, bd=1, highlightthickness=1, relief=RIDGE)
        self.new_name.place(x=5, y=70, width=100, height=30)

        self.name_entry = Entry(self.right_frame, font=LB_FONT, bd=1, highlightthickness=1, relief=RIDGE,
                                justify="center", textvariable=self.new_user_name)
        self.name_entry.place(x=110, y=70, width=220, height=30)

        self.new_surname = Label(self.right_frame, text="Surname", font=LB_FONT, bd=1, highlightthickness=1,
                                 relief=RIDGE)
        self.new_surname.place(x=5, y=105, width=100, height=30)

        self.surname_entry = Entry(self.right_frame, font=LB_FONT, bd=1, highlightthickness=1, relief=RIDGE,
                                   justify="center", textvariable=self.new_user_surname)
        self.surname_entry.place(x=110, y=105, width=220, height=30)

        self.new_email = Label(self.right_frame, text="Email", font=LB_FONT, bd=1, highlightthickness=1,
                               relief=RIDGE)
        self.new_email.place(x=5, y=140, width=100, height=30)

        self.email_entry = Entry(self.right_frame, font=LB_FONT, bd=1, highlightthickness=1, relief=RIDGE,
                                 justify="center", textvariable=self.new_user_email)
        self.email_entry.place(x=110, y=140, width=220, height=30)

        self.add_user = Button(self.right_frame, text="Add New User", font=BNT_FONT, justify="center",
                               bg="tan", command=self.add_new_user_method)
        self.add_user.place(x=5, y=175, width=323, height=30)

        self.user_list = Label(self.right_frame, text="Available Users", font=("Helvetica", 15, "bold"),
                               justify="center", bd=1, highlightthickness=1, relief=RIDGE)
        self.user_list.place(x=5, y=250, width=323, height=40)

        self.user_box = Listbox(self.right_frame, bd=1, highlightthickness=1, relief=RIDGE, font=LB_FONT)
        self.user_box.place(x=5, y=295, width=323, height=300)

        # ========================================= IMAGE LABEL =========================================== #
        used_image = Image.open("./IMG/map.jpg")
        used_photo = ImageTk.PhotoImage(used_image)
        self.image_label = Label(self.window, image=used_photo, bd=2, highlightthickness=2, relief=RIDGE)
        self.image_label.image = used_photo
        self.image_label.place(x=15, y=85, width=555, height=295)

        # ========================================= GMAIL FRAMES =========================================== #
        self.center_frame = Frame(self.window, bd=2, highlightthickness=2, relief=RIDGE)
        self.center_frame.place(x=575, y=83, width=424, height=299)

        self.receiver_label = Label(self.center_frame, text="To:", font=LB_FONT, bd=1, highlightthickness=1,
                                    relief=RIDGE, justify="left")
        self.receiver_label.place(x=5, y=5, width=40, height=30)

        self.receiver_entry = Label(self.center_frame, text="", font=LB_FONT, bd=1, highlightthickness=1,
                                    relief=RIDGE, justify="left")
        self.receiver_entry.place(x=90, y=5, width=320, height=30)

        self.subject_label = Label(self.center_frame, text="Subject:", font=LB_FONT, bd=1, highlightthickness=1,
                                   relief=RIDGE, justify="left")
        self.subject_label.place(x=5, y=40, width=70, height=30)

        self.subject_entry = Label(self.center_frame, text="", font=LB_FONT, bd=1, highlightthickness=1,
                                   relief=RIDGE, justify="left")
        self.subject_entry.place(x=90, y=40, width=320, height=30)

        self.main_text = Text(self.center_frame, bd=1, highlightthickness=1, relief=RIDGE, font=LB_FONT,
                              bg="white smoke")
        self.main_text.place(x=5, y=80, width=406, height=170)

        self.send_button = Button(self.center_frame, text="Send Message", font=BNT_FONT, justify="center", bd=1,
                                  highlightthickness=1, relief=RIDGE, bg="spring green",
                                  command=self.send_message_method)
        self.send_button.place(x=5, y=255, width=120, height=30)

        self.close_button = Button(self.center_frame, text="Close Application", font=BNT_FONT, justify="center", bd=1,
                                   highlightthickness=1, relief=RIDGE, bg="gold", command=self.close_application)
        self.close_button.place(x=255, y=255, width=155, height=30)

        self.refresh_button = Button(self.center_frame, text="Refresh", font=BNT_FONT, justify="center", bd=1,
                                     bg="khaki", highlightthickness=1, relief=RIDGE, command=self.refresh_application)
        self.refresh_button.place(x=130, y=255, width=120, height=30)

        # ========================================= LEFT FRAME =========================================== #
        self.left_frame = Frame(self.window, bd=3, highlightthickness=3, relief=RIDGE, pady=15)
        self.left_frame.place(x=10, y=385, width=562, height=305)

        self.info_label = Label(self.left_frame, text="Information Dashboard", font=("Helvetica", 15, "bold"),
                                justify="center", bd=1, highlightthickness=1, relief=RIDGE)
        self.info_label.place(x=5, y=0, width=542, height=40)

        # --------------------------------------------------------------------------------------------
        self.to_city = Label(self.left_frame, text="To City", font=LB_FONT, bd=1, highlightthickness=1,
                             relief=RIDGE)
        self.to_city.place(x=5, y=60, width=130, height=30)

        self.city_box = ttk.Combobox(self.left_frame, font=LB_FONT, justify="center", textvariable=self.chosen_city)
        self.city_box["values"] = CITIES
        self.city_box.current(0)
        self.city_box.place(x=140, y=60, width=130, height=30)

        self.get_code = Button(self.left_frame, text="Get Code", font=LB_FONT, bd=1, highlightthickness=1,
                               relief=RIDGE, fg="navy", command=self.get_code_method)
        self.get_code.place(x=5, y=100, width=130, height=30)

        self.city_code = Label(self.left_frame, text="", font=LB_FONT, bd=1, highlightthickness=1, relief=RIDGE)
        self.city_code.place(x=140, y=100, width=130, height=30)

        self.my_price = Label(self.left_frame, text="My Price", font=LB_FONT, bd=1, highlightthickness=1,
                              relief=RIDGE)
        self.my_price.place(x=5, y=140, width=130, height=30)

        self.price_entry = Entry(self.left_frame, font=LB_FONT, bd=1, highlightthickness=1, relief=RIDGE,
                                 justify="center", textvariable=self.chosen_price)
        self.price_entry.place(x=140, y=140, width=130, height=30)

        self.to_curr = Label(self.left_frame, text="Currency", font=LB_FONT, bd=1, highlightthickness=1,
                             relief=RIDGE)
        self.to_curr.place(x=5, y=180, width=130, height=30)

        self.curr_box = ttk.Combobox(self.left_frame, font=LB_FONT, justify="center", textvariable=self.chosen_currency)
        self.curr_box["values"] = CURRENCY
        self.curr_box.current(0)
        self.curr_box.place(x=140, y=180, width=130, height=30)
        # --------------------------------------------------------------------------------------------
        self.get_date_from = Button(self.left_frame, text="Get From Date", font=LB_FONT, bd=1, highlightthickness=1,
                                    relief=RIDGE, fg="navy", command=self.get_start_date_method)
        self.get_date_from.place(x=275, y=60, width=135, height=30)

        self.from_date = Label(self.left_frame, text="", font=LB_FONT, bd=1, highlightthickness=1,
                               relief=RIDGE)
        self.from_date.place(x=415, y=60, width=130, height=30)

        self.get_date_to = Button(self.left_frame, text="Get To Date", font=LB_FONT, bd=1, highlightthickness=1,
                                  relief=RIDGE, fg="navy", command=self.get_end_date_method)
        self.get_date_to.place(x=275, y=100, width=135, height=30)

        self.to_date = Label(self.left_frame, text="", font=LB_FONT, bd=1, highlightthickness=1,
                             relief=RIDGE)
        self.to_date.place(x=415, y=100, width=130, height=30)

        self.min_trip = Label(self.left_frame, text="Trip Duration Min", font=LB_FONT, bd=1, highlightthickness=1,
                              relief=RIDGE)
        self.min_trip.place(x=275, y=140, width=135, height=30)

        self.min_entry = Entry(self.left_frame, font=LB_FONT, bd=1, highlightthickness=1, relief=RIDGE,
                               justify="center", textvariable=self.minimum_duration)
        self.min_entry.place(x=415, y=140, width=130, height=30)

        self.max_trip = Label(self.left_frame, text="Trip Duration Max", font=LB_FONT, bd=1, highlightthickness=1,
                              relief=RIDGE)
        self.max_trip.place(x=275, y=180, width=135, height=30)

        self.max_entry = Entry(self.left_frame, font=LB_FONT, bd=1, highlightthickness=1, relief=RIDGE,
                               justify="center", textvariable=self.maximum_duration)
        self.max_entry.place(x=415, y=180, width=130, height=30)

        self.submit_button = Button(self.left_frame, text="Search Results", font=LB_FONT, bd=1, highlightthickness=1,
                                    relief=RIDGE, bg="light blue", command=self.submit_search_method)
        self.submit_button.place(x=5, y=230, width=540, height=30)

        # ========================================= BOTTOM FRAMES =========================================== #
        self.calendar_frame = Frame(self.window)
        self.calendar_frame.place(x=575, y=385, width=222, height=305)

        self.calendar = Calendar(self.calendar_frame, selectmode="day", year=self.today.year, month=self.today.month,
                                 day=self.today.day)
        self.calendar.place(x=1, y=5, width=208, height=296)

        self.bottom_frame = Frame(self.window)
        self.bottom_frame.place(x=790, y=385, width=210, height=266)

        self.search_output = Text(self.bottom_frame, font=LB_FONT, width=47, height=17, bg="white smoke",
                                  fg="dark slate gray", bd=2, highlightthickness=2, relief=RIDGE)
        self.search_output.place(x=0, y=3, width=210, height=260)

        self.generate_button = Button(self.window, text="Generate Message", font=BNT_FONT, justify="center",
                                      bg="salmon", command=self.generate_message)
        self.generate_button.place(x=790, y=655, width=210, height=30)

        self.fill_user_listbox()

    # ====================================== FUNCTIONALITY ========================================== #
    def add_new_user_method(self):
        if len(self.new_user_name.get()) > 0 and len(self.new_user_surname.get()) > 0 \
                and len(self.new_user_email.get()) > 0:
            index = self.user_box.size()
            self.user_box.insert(index, self.new_user_email.get())
            self.file_tool.update_json(email=self.new_user_email.get(), name=self.new_user_name.get(),
                                       surname=self.new_user_surname.get())
            self.new_user_name.set("")
            self.new_user_surname.set("")
            self.new_user_email.set("")
        else:
            messagebox.showerror(title="Error", message="All Field must be filled!")

    def extract_active_method(self):
        self.chosen_label.config(text=f"{self.user_box.get(ACTIVE)}")

    def fill_user_listbox(self):
        answer = self.file_tool.read_json()
        order = 1
        for item in answer:
            self.user_box.insert(order, item)
            order += 1

    def get_start_date_method(self):
        answer_1 = str(self.calendar.get_date()).split("/")
        answer_2 = datetime(year=int(f"20{answer_1[-1]}"), month=int(answer_1[0]), day=int(answer_1[1]))
        result = answer_2.strftime("%d/%m/%Y")
        self.from_date.config(text=f"{result}")

    def get_end_date_method(self):
        answer_1 = str(self.calendar.get_date()).split("/")
        answer_2 = datetime(year=int(f"20{answer_1[-1]}"), month=int(answer_1[0]), day=int(answer_1[1]))
        result = answer_2.strftime("%d/%m/%Y")
        self.to_date.config(text=f"{result}")

    def get_code_method(self):
        tool = TequilaFinder()
        result = tool.get_iat_code(self.chosen_city.get())
        self.city_code.config(text=result)

    def submit_search_method(self):
        if len(self.city_code.cget("text")) > 0 and len(self.chosen_price.get()) > 0 \
                and len(self.from_date.cget("text")) > 0 and len(self.to_date.cget("text")) > 0 \
                and len(self.minimum_duration.get()) > 0 and len(self.maximum_duration.get()) > 0:
            tool = TequilaFinder()
            self.special_answer = tool.get_flight_info(to_code=self.city_code.cget("text"),
                                                       date_from=self.from_date.cget("text"),
                                                       date_to=self.to_date.cget("text"),
                                                       min_duration=self.minimum_duration.get(),
                                                       max_duration=self.maximum_duration.get(),
                                                       currency=self.chosen_currency.get())
            if self.chosen_currency.get() == "GBP":
                self.symbol = "£"
            elif self.chosen_currency.get() == "EUR":
                self.symbol = "€"
            else:
                self.symbol = "$"

            if float(self.chosen_price.get()) > float(self.special_answer["price"]):
                output = f"""
            Good News!
            \nFrom {self.special_answer["city_from"]} ({self.special_answer["iat_from"]})
            \nTo {self.special_answer["city_to"]} ({self.special_answer["iat_to"]}),
            \nPeriod:
            \n{self.special_answer["start_date"]} : {self.special_answer["end_date"]}
            \nPrice - {self.symbol} {self.special_answer["price"]}
            """
                self.search_output.config(bg="pale green")
                self.search_output.delete("1.0", END)
                self.search_output.insert("1.0", f"{output}")
            else:
                output = f"""\n\n\n
            BAD NEWS!
            \n   Flight Is NOT Available!
            """
                self.search_output.config(bg="salmon")
                self.search_output.delete("1.0", END)
                self.search_output.insert("1.0", f"{output}")
        else:
            messagebox.showerror(title="Error", message="All Field must be Filled!")

    def good_or_bad_news(self):
        a = self.search_output.get("1.0", END)
        b = a.split()
        c = [item.strip() for item in b]
        return c

    def generate_message(self):
        try:
            if len(str(self.search_output.get("1.0", END))) > 0 and len(self.chosen_label.cget("text")) > 0:
                personal_info = self.file_tool.return_wanted_user(self.chosen_label.cget("text"))
                check_point = self.good_or_bad_news()
                if ("BAD" in check_point) and ("NOT" in check_point):
                    self.letter = f"""Dear {personal_info['name']} {personal_info['surname']}!
Unfortunately, There is not any available Flight
For These requirements!
Flight Agency!
"""
                else:
                    self.letter = f"""Dear {personal_info['name']} {personal_info['surname']}!
There is Good News For You,
Only {self.symbol} {self.special_answer['price']} to fly from
{self.special_answer['city_from']} ({self.special_answer['iat_from']}) to {self.special_answer['city_to']} ({self.special_answer['iat_to']}),
from {self.special_answer['start_date']} to {self.special_answer['end_date']}.
If you are interested - Please let us know
Flight Agency!
"""
                self.file_tool.save_message(notification=self.letter)
                answer = self.file_tool.get_message()
                self.main_text.delete("1.0", END)
                self.main_text.insert("1.0", f"{answer}")
                self.receiver_entry.config(text=self.chosen_label.cget("text"))
                self.subject_entry.config(text="Cheapest Flight Notification")
            else:
                messagebox.showerror(title="Error", message="All Field must be Filled!")
        except TypeError:
            messagebox.showerror(title="Error", message="All Field must be Filled!")

    def send_message_method(self):
        if len(self.receiver_entry.cget("text")) > 0 and len(self.subject_entry.cget("text")) > 0:
            tool = SendEmail(receiver=self.receiver_entry.cget("text"), subject=self.subject_entry.cget("text"),
                             body=self.main_text.get("1.0", END))
            tool.send_mail()
            messagebox.showinfo(title="Confirm", message="Message has been sent, Successfully!")
        else:
            messagebox.showerror(title="Error", message="All Field must be Filled!")

    def refresh_application(self):
        confirm = messagebox.askyesno(title="Confirmation", message="Do You Want To Refresh The Program?")
        if confirm > 0:
            self.city_code.config(text="")
            self.chosen_price.set("")
            self.from_date.config(text="")
            self.to_date.config(text="")
            self.minimum_duration.set("")
            self.maximum_duration.set("")
            self.search_output.delete("1.0", END)
            self.search_output.config(bg="white smoke")
            self.receiver_entry.config(text="")
            self.subject_entry.config(text="")
            self.main_text.delete("1.0", END)
            self.new_user_name.set("")
            self.new_user_surname.set("")
            self.new_user_email.set("")
            self.chosen_label.config(text="")
            return
        else:
            pass

    def close_application(self):
        confirm = messagebox.askyesno(title="Cheapest Flight Finder", message="Do You Want To Close The Program?")
        if confirm > 0:
            self.window.destroy()
            return
        else:
            pass


def launch_app():
    app = Tk()
    PublicApp(app)
    app.mainloop()


if __name__ == "__main__":
    launch_app()
