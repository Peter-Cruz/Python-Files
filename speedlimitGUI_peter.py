#speedlimitGUI_peter.py

import tkinter

class speedGUI:
    def __init__(self):
        self.main_window=tkinter.Tk()

        #Create the frames:
        self.frame1_peter=tkinter.Frame(self.main_window)
        self.frame2_peter=tkinter.Frame(self.main_window)
        self.frame3_peter=tkinter.Frame(self.main_window)
        self.frame4_peter=tkinter.Frame(self.main_window)
        self.frame5_peter=tkinter.Frame(self.main_window)

        #Create labels, buttons, entry boxes, etc..
        self.limitlabel = tkinter.Label(self.frame1_peter, text="Please enter the speed limit of the zone: ")
        self.limitentry = tkinter.Entry(self.frame1_peter)

        self.speedlabel = tkinter.Label(self.frame2_peter, text="Please enter the speed the vehicle was travelling: ")
        self.speedentry = tkinter.Entry(self.frame2_peter)

        self.zonelabel1 = tkinter.Label(self.frame3_peter, text="Certain zones have different fine rates: Regular - R, School - S, Workers Present - W, or Housing - H.  If a valid zone is not provided, the zone will be considered a school zone. ")
        self.zonelabel2 = tkinter.Label(self.frame3_peter, text="Please enter the zone the vehicle was in: ")
        self.zoneentry = tkinter.Entry(self.frame3_peter)

        #The text is set to an empty string so that it can be configured after the calculations are complete.
        self.calclabel = tkinter.Label(self.frame4_peter, text="")

        self.calcbutton = tkinter.Button(self.frame5_peter, text="Calculate Fine", command=self.calcfine)
        self.quitbutton = tkinter.Button(self.frame5_peter, text='Quit', command=self.main_window.destroy)

        #Packing of the elements
        self.limitlabel.pack(side='top')
        self.limitentry.pack(side='top')
        self.frame1_peter.pack()

        self.speedlabel.pack(side='top')
        self.speedentry.pack(side='top')
        self.frame2_peter.pack()

        self.zonelabel1.pack(side='top')
        self.zonelabel2.pack(side='top')
        self.zoneentry.pack(side='top')
        self.frame3_peter.pack()

        self.calclabel.pack()
        self.frame4_peter.pack()

        self.calcbutton.pack()
        self.quitbutton.pack()
        self.frame5_peter.pack()

        #Create the GUI loop
        tkinter.mainloop()

    def calcfine(self):
        #The fine is calculated based on the user inputs
        speedlimit = float(self.limitentry.get())
        carspeed = float(self.speedentry.get())
        zone = str(self.zoneentry.get())

        #The same calculations from the 3rd assignment
        if (carspeed - speedlimit) < 0:
            fine = 0.00
        elif 0 < (carspeed - speedlimit) < 10:
            fine = 49.50
        elif 10 <= (carspeed - speedlimit) < 20:
            fine = 99.00
        elif 20 <= (carspeed - speedlimit) < 30:
            fine = 129.50
        elif 30 <= (carspeed - speedlimit) < 40:
            fine = 199.00
        elif 40<= (carspeed - speedlimit):
            fine = 0.00
            self.calclabel.config(text='Fine to be decided in court.')
            #This string does not print in the GUI and I cannot think of a way to make it do so without creating an error.

        #The messages inform the user if their fine is going to be amplified.  
        if zone == "R" or zone == "r":
            msg = "Driving in Regular zone."
        elif zone == "H" or zone == "h":
            msg = "Driving in Housing Zone; fine multiplied by 1.5."
            fine = (fine * 1.5)
        elif zone == "W" or zone == "w":
            msg = "Driving while Workers are Present; fine doubled."
            fine = (fine * 2)
        elif zone == "S" or zone == "s":
            msg = "Driving in School Zone; fine tripled."
            fine = (fine * 3)
        else:
            msg = "Invalid zone entered.  Setting zone to S; fine tripled."
            fine = (fine * 3)

        #This is the final product that the 4th frame displays.  Using .config() allows the calclabel function to change the empty string with the new text.
        self.calclabel.config(text=f'{msg} \n ${fine}')

if __name__ == '__main__':
    speed_GUI = speedGUI()