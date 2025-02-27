from os import remove, path
from json import load, dump
from threading import Thread
import requests
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from awesometkinter.bidirender import render_text
from mechanicalsoup import StatefulBrowser
from playsound import playsound

class Al_Hadba():
    def __init__(self):
        self.__email = None
        self.__passwd = None
        self.__config_path = path.join(path.dirname(path.abspath(__file__)), "config/config.json")
        self.__icon_path = path.join(path.dirname(path.abspath(__file__)), "assets/images/icon.png")
        self.__startup_sound = path.join(path.dirname(path.abspath(__file__)), "assets/sounds/startup.m4a")
        self.__welcome_image_path = path.join(path.dirname(path.abspath(__file__)), "assets/images/welcome_image.png")
        self.__browser = None
        self.__response = None
        self.__login_page = None
        self.__loading_page = None
        self.__home_page = None
        self.__info_page = None
        self.__logout_page = None

    def startup(self):
        """Application startup procedure"""
        # Try to load saved login information
        try:
            data = load(open(self.__config_path, 'r'))
            self.__email = data['email']
            self.__passwd = data['passwd']
            self.Switch()
        except FileNotFoundError:
            self.LoginPage()

    def LoginPage(self):
        """Setting Login Page (LoginPage)"""
        self.__login_page = Tk()
        self.__login_page.title("Al-Hadba University")
        self.__login_page.geometry("700x400")
        self.__login_page.resizable(False, False)
        icon = PhotoImage(file=self.__icon_path)
        self.__login_page.iconphoto(True, icon)

        # right side of page
        image = PhotoImage(file=self.__welcome_image_path)
        image_label = Label(self.__login_page, image=image)
        image_label.pack(side="right", fill="y")

        # left side of page
        left_frame = Frame(self.__login_page)
        welcome_label = Label(left_frame, text="       Welcome, Log-in to continue.\n\n\n", font=("Arial", 16))
        email_label = Label(left_frame, text="Enter your email:")
        email_entry = Entry(left_frame)
        passwd_label = Label(left_frame, text="Enter password OR ID card:")
        passwd_entry = Entry(left_frame, show="*")
        login_button = Button(left_frame, text="LOGIN",
            fg="white", bg="blue", activebackground="#8ac926",
            command=lambda: self.login_process(email_entry, passwd_entry))

        # pack
        left_frame.pack(side="left", padx=20, pady=20, fill="y")
        welcome_label.pack(pady=5)
        email_label.pack(pady=5, padx=10)
        email_entry.pack(pady=0, padx=10)
        passwd_label.pack(pady=0, padx=10)
        passwd_entry.pack(pady=0, padx=10)
        login_button.pack(pady=20, padx=0)

        self.__login_page.mainloop()
            
    def login_process(self, email_entry, passwd_entry):
        """Stores login credentials and initiates the login process."""
        self.__email = email_entry.get()
        self.__passwd = passwd_entry.get()
        self.Switch()

    def Switch(self):
        """Verifies login information and navigates to the home page."""
        if 0 in (len(self.__email), len(self.__passwd)):
            messagebox.showerror(
                "ERROR!", 
                "Eemail or password cannot be empty.")
            return

        # Attempt to access using information
        self.__browser = StatefulBrowser()
        self.__browser.open("http://92.119.61.166:9091/Account/login", timeout=10)
        self.__browser.select_form('form[action="/Account/Login"]')
        self.__browser["PhoneNumber"] = self.__email
        self.__browser["Password"] = self.__passwd
        self.__browser["AcademicYear"] = "105"
        self.__browser["AcademicYearName"] = "2024-2025"
        response = self.__browser.submit_selected()
        if "ShowPatient" in response.url:
            dump({
                'email': self.__email,
                'passwd': self.__passwd}, open(
                self.__config_path, 'w'), indent=4)
            if self.__login_page:
                self.__login_page.destroy()
            self.__response = response
            self.Homepage()
        else:
            messagebox.showerror("ERROR!", "Invalid login information")
            return

    def StartupSound(self):
        playsound(self.__startup_sound)
        return
        
    def Homepage(self):
        """Displays the home page with navigation buttons."""
        self.__home_page = Tk()
        self.__home_page.title("Al-Hadba University - Home")
        self.__home_page.geometry("350x400")
        self.__home_page.resizable(False, False)
        icon = PhotoImage(file=self.__icon_path)
        self.__home_page.iconphoto(True, icon)

        Label(
            self.__home_page, text="Welcome in Home Page", font=("Arial", 18)
        ).grid(row=0, column=0, sticky="N")
        Button(
            self.__home_page, text="My Informations", activebackground="blue",
            command=self.InfoPage, width=40, height=5
        ).grid(row=1, column=0, sticky="s")
        Button(
            self.__home_page, text="Mid-Term", activebackground="yellow",
            command=self.MidTerm, width=20, height=10
        ).grid(row=2, column=0, padx=0, pady=0, sticky="w")
        Button(
            self.__home_page, text="Final-Term", activebackground="green",
            command=self.FinalTerm, width=20, height=10
        ).grid(row=2, column=0, padx=0, pady=0, sticky="e")
        Button(
            self.__home_page, text="Logout", activebackground="red",
            command=self.Logout, width=40, height=2
        ).grid(row=3, column=0, pady=20, sticky="S")
        startup_sound = Thread(target=self.StartupSound)
        startup_sound.start()
        self.__home_page.mainloop()

    def InfoPage(self):
        """Displays user information in a table."""
        self.__info_page = Tk()
        self.__info_page.title("Al-Hadba University - My informations")
        self.__info_page.geometry("400x300")
        self.__info_page.resizable(False, False)

        # get info from web site
        datas = {
            "اسم الطالب": self.__response.soup.find('input', {'id':'NameStud'})['value'],
            "القسم": self.__response.soup.find('input', {'id':'dept_NameDept'})['value'],
            "القناة": self.__response.soup.find('input', {'id':'chStud1_ChStude'})['value'],
            "نوع الدراسة": self.__response.soup.find('input', {'id':'TypeStudy'})['value'],
            "رقم الهاتف": self.__response.soup.find('input', {'id':'PhoneNumber'})['value']
        }

        tree = ttk.Treeview(self.__info_page, column=("Information","Value"), show="headings")
        tree.heading("Information", text="Information")
        tree.heading("Value", text="Value")
        for data in datas:
            values = (
                render_text(data),
                render_text(datas[data])
            )
            tree.insert("", END, values=values)
        tree.pack()
        self.__info_page.mainloop()

    def MidTerm(self):
        self.__mid_term = Tk()
        self.__mid_term.title("Al-Hadba University - Mid-Term result")
        self.__mid_term.geometry("600x400")
        self.__mid_term.resizable(False, False)

        columns = ("Name", "Term", "Result")
        tree = ttk.Treeview(self.__mid_term, columns=columns, show="headings")
        self.__browser.open("http://92.119.61.166:9091/Students/Marks")
        if len(self.__browser.page.find_all("tr")) != 1:
            for i in range(1, len(self.__browser.page.find_all("tr"))):
                tr = self.__browser.page.find_all("tr")[i]
                values = (
                    render_text(tr.select("td")[0].text.strip()),
                    render_text(tr.select("td")[1].text.strip()),
                    render_text(tr.select("td")[2].text.strip())
                )
                tree.insert('', END, values=values)
            tree.pack()
        else:
            messagebox.showinfo("NOTICE", "Exam result have not been announced by university yet.\nPlease wait for further updates.")
            self.__mid_term.destroy()
        self.__mid_term.mainloop()

    def FinalTerm(self):
        self.__final_term = Tk()
        self.__final_term.title("Al-Hadba University - Final-Term result")
        self.__final_term.geometry("600x400")
        self.__final_term.resizable(False, False)

        columns = ("Name", "Term", "Result")
        tree = ttk.Treeview(self.__final_term, columns=columns, show="headings")
        self.__browser.open("http://92.119.61.166:9091/Students/MarkStudFinal")
        if len(self.__browser.page.find_all("tr")) != 1:
            for i in range(1, len(self.__browser.page.find_all("tr"))):
                tr = self.__browser.page.find_all("tr")[i]
                values = (
                    render_text(tr.select("td")[0].text.strip()),
                    render_text(tr.select("td")[1].text.strip()),
                    render_text(tr.select("td")[2].text.strip())
                )
                tree.insert('', END, values=values)
            tree.pack()
        else:
            messagebox.showinfo("NOTICE", "Exam result have not been announced by university yet.\nPlease wait for further updates.")
            self.__final_term.destroy()
        self.__final_term.mainloop()

    def Logout(self):
        if messagebox.askokcancel("WARNING", "If you log out, your login information will be lost\nAre you sure you want to proceed?"):
            remove(self.__config_path)
            self.__home_page.destroy()
            self.LoginPage()
        else:
            # if user cancel logout
            pass


if "__main__" == __name__:
    try:
        al_hadba_app = Al_Hadba()
        al_hadba_app.startup()
    except (
            requests.exceptions.ConnectionError,
            requests.exceptions.ReadTimeout,
            requests.exceptions.ConnectTimeout):
        messagebox.showerror(
            "ERROR in connection",
            "Check your connection and try again later.")
