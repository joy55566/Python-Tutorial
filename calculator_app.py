import tkinter as tk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("300x400")
        
        # Create display
        self.display = tk.Entry(root, width=25, justify="right", font=("Arial", 20))
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        # Create buttons
        self.create_buttons()
        
        # Initialize variables
        self.current = ""
        self.operation = ""
        self.first_number = None
    
    def create_buttons(self):
        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        row = 1
        col = 0
        
        for button_text in button_texts:
            button = tk.Button(self.root, 
                             text=button_text,
                             width=5, height=2,
                             font=("Arial", 14),
                             command=lambda x=button_text: self.button_click(x))
            button.grid(row=row, column=col, padx=2, pady=2)
            
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Clear button
        clear_button = tk.Button(self.root,
                               text='C',
                               width=24, height=2,
                               font=("Arial", 14),
                               command=self.clear)
        clear_button.grid(row=row, column=0, columnspan=4, padx=2, pady=2)
    
    def button_click(self, text):
        if text in '0123456789.':
            self.current += text
            self.display.delete(0, tk.END)
            self.display.insert(0, self.current)
        
        elif text in '+-*/':
            if self.current:
                if self.first_number is None:
                    self.first_number = float(self.current)
                else:
                    self.calculate()
                self.operation = text
                self.current = ""
        
        elif text == '=':
            if self.current and self.first_number is not None:
                self.calculate()
                self.operation = ""
                self.first_number = None
    
    def calculate(self):
        second_number = float(self.current)
        if self.operation == '+':
            result = self.first_number + second_number
        elif self.operation == '-':
            result = self.first_number - second_number
        elif self.operation == '*':
            result = self.first_number * second_number
        elif self.operation == '/':
            if second_number != 0:
                result = self.first_number / second_number
            else:
                result = "Error"
        
        self.display.delete(0, tk.END)
        self.display.insert(0, str(result))
        self.current = str(result)
        self.first_number = float(result)
    
    def clear(self):
        self.current = ""
        self.first_number = None
        self.operation = ""
        self.display.delete(0, tk.END)

def main():
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()

if __name__ == "__main__":
    main()
