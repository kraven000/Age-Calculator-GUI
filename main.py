import customtkinter as ctk
import tkcalendar
from datetime import date


class Age:
    def __init__(self) -> None:
        self.current_date = [date.today().year, date.today().month, date.today().day]  #[YYYY,MM,DD]
    
    
    def show_selected_date(self,arg=None) -> None:
        self.show_date.configure(text=f"Selected Date(YYYY-MM-DD): {self.dob.get_date()}")
    
    
    def calculate_age(self) -> None:
        selected_date:list = str(self.dob.get_date()).split("-")  # [YYYY,MM,DD]
        
        # converting all elements of selected_date list into integer
        selected_date:list = list(map(lambda x:int(x),selected_date))
        
        # calculate Age
        if (self.current_date[1]>selected_date[1]) or (self.current_date[1]==selected_date[1] and self.current_date[2]>=selected_date[2]):
            age = self.current_date[0]-selected_date[0]
        else:
            age = self.current_date[0]-selected_date[0]-1
        
        # check Age validity
        if age>=0:
            self.show_age.configure(text=f"Age: {age} years old")
        else:
            self.show_age.configure(text=f"Age: Error")
    
    
    def gui(self):
        window = ctk.CTk()
        window.geometry("613x527")
        
        # asking date
        ctk.CTkLabel(window,text="Choose Date of Birth: ",font=("Roboto",16)).place(x=0,y=1)
        
        # adding calendar widget to window to choose date
        self.dob:tkcalendar.Calendar = tkcalendar.Calendar(window,date_pattern="yyyy-mm-dd")
        self.dob.place(x=173,y=1)
        
        '''
        binding the windget with show_selected_date() function so that user get's to know which 
        date they have choose
        '''
        self.dob.bind("<<CalendarSelected>>", self.show_selected_date)
        
        
        # widget to show selected date to user
        self.show_date:ctk.CTkLabel = ctk.CTkLabel(window,text=f"Selected Date(YYYY-MM-DD): None",font=("Roboto",16))
        self.show_date.place(x=0,y=199)
        
        ctk.CTkButton(window,text="CALCULATE AGE",font=("Sans",16),command=self.calculate_age).place(x=0,y=231)
        
        # show Age
        self.show_age = ctk.CTkLabel(window,text="",font=("Aerial",20))
        self.show_age.place(x=0,y=273)
        
        window.mainloop()


if __name__=="__main__":
    app = Age()
    app.gui()