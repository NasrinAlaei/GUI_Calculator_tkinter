from tkinter import *


# Create a calculator class
class calculator:

    def __init__(self, master):

        '''
        DOCSTRING: Define what to do on initialization
        '''

        self.master = master  # Assign reference to the main window of the application
        master.title("calculator")  # Add a name to our application
        master.geometry("298x400")
        master.resizable(0, 0)
        self.equation = Entry(master, width=45, borderwidth=7) #Create a line where we display the equation
        self.equation.grid(row=0, column=0, padx=5, pady=30, columnspan=5) #Assign a position for the equation line in the grey application window

        # Execute the .creteButton() method
        self.CreateButton()

    def AddButton(self, value):

        '''
        DOCSTRING: Method to process the creation of a button and make it clickable
        INPUT: value of the button (1,2,3,4,5,6,7,8,9,0,+,-,*,/,c,=)
        OUTPUT: returns a designed button object
        '''

        if value == '=':
            return Button(self.master, text=value, width=9, height=4, bg='light blue',
                          command=lambda: self.clickButton(str(value)))
        return Button(self.master, text=value, width=9, height=4, bg='light gray',
                      command=lambda: self.clickButton(str(value)))

    def CreateButton(self):

        '''
        DOCSTRING: Method that creates the buttons
        INPUT: nothing
        OUTPUT: creates a button
        '''

        # We first create each button one by one with the value we want
        # Using addButton() method which is described below
        b0 = self.AddButton(0)
        b1 = self.AddButton(1)
        b2 = self.AddButton(2)
        b3 = self.AddButton(3)
        b4 = self.AddButton(4)
        b5 = self.AddButton(5)
        b6 = self.AddButton(6)
        b7 = self.AddButton(7)
        b8 = self.AddButton(8)
        b9 = self.AddButton(9)
        b_add = self.AddButton('+')
        b_sub = self.AddButton('-')
        b_mul = self.AddButton('*')
        b_div = self.AddButton('/')
        b_clear = self.AddButton('C')
        b_equal = self.AddButton('=')

        # Arrange the buttons into lists which represent calculator rows
        row1 = [b7, b8, b9, b_add]
        row2 = [b4, b5, b6, b_sub]
        row3 = [b1, b2, b3, b_mul]
        row4 = [b_clear, b0, b_equal, b_div]

        # Assign each button to a particular location on the GUI
        r = 1
        for row in [row1, row2, row3, row4]:
            c = 0
            for btn in row:
                btn.grid(row=r, column=c, columnspan=1)
                c += 1
            r += 1

    def clickButton(self, value):

        '''
        DOCSTRING: Method to program the actions that will happen in the calculator after a click of each button
        INPUT: value of the button (1,2,3,4,5,6,7,8,9,0,+,-,*,/,c,=)
        OUTPUT: what action will be performed when a particular button is clicked
        '''

        # Get the equation that's entered by the user
        current_equation = str(self.equation.get())

        # If user clicked "c", then clear the screen
        if value == 'C':
            self.equation.delete(-1, END)

        # If user clicked "=", then compute the answer and display it
        elif value == '=':
            answer = str(eval(current_equation))
            self.equation.delete(-1, END)
            self.equation.insert(0, answer)

        # If user clicked any other button, then add it to the equation line
        else:
            self.equation.delete(0, END)
            self.equation.insert(0, current_equation + value)


if __name__ == '__main__':

    # Create the main window of an application
    root = Tk()

    # Tell our calculator class to use this window
    cl = calculator(root)

    # Executable loop on the application, waits for user input
    root.mainloop()
