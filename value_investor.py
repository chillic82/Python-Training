from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("Value Investor v1.0")
root.iconbitmap('c:/python_stuff/VI.ico')
root.geometry("1280x720")

winframe = LabelFrame(root, text = "", padx=5, pady=5)
winframe.pack(padx=10, pady=10)

dateframe = LabelFrame(winframe, text = "", padx=20, pady=5)
dateframe.grid(row=0, column=0)
headframe = LabelFrame(winframe, text = "", padx=0, pady=0)
headframe.grid(row=0, column=1)
contframe = LabelFrame(winframe, text = "", padx=0, pady=0)
contframe.grid(row=0, column=2)
sideframe = LabelFrame(winframe, text = "", padx=0, pady=0)
sideframe.grid(row=1, column=0)
mainframe = LabelFrame(winframe, text = "", padx=5, pady=5)
mainframe.grid(row=1, column=1, columnspan=2, padx=10, pady=10)

game_date = Label(dateframe, text = "Nov 2024", font = 'calibri' '25' 'bold_font', padx=2, pady=20)
game_header = Label(headframe, text = "Value Investor v1.0", font = 'calibri' '25' 'bold', padx=380, pady=30)
cont_button = Button(contframe, text = "CONTINUE", padx=20, pady=20)

inbox_button = Button(sideframe, text = "Inbox/News", padx=1, pady=16, width=20)
market_button = Button(sideframe, text = "Stockmarket", padx=1, pady=16, width=20)
portfolio_button = Button(sideframe, text = "Portfolio", padx=1, pady=16, width=20)
personal_button = Button(sideframe, text = "Personal Finances", padx=1, pady=16, width=20)
analysis_button = Button(sideframe, text = "Stock Analysis", padx=1, pady=16, width=20)
dividend_button = Button(sideframe, text = "Dividend Calendar", padx=1, pady=16, width=20)

main_text = Label(mainframe, text = "This is where the main screen for that page will be displayed", font = 'calibri' '12' , padx=300, pady=180)


game_header.grid(row=0, column=1)
game_date.grid(row=0, column=0)
cont_button.grid(row=0, column=2)

inbox_button.grid(row=1, column=0)
market_button.grid(row=2, column=0)
portfolio_button.grid(row=3, column=0)
personal_button.grid(row=4, column=0)
analysis_button.grid(row=5, column=0)
dividend_button.grid(row=6, column=0)

main_text.grid(row=1, column=2, columnspan=2)



root.mainloop()
