# Created By - Satyam Kulkarni
    
# Importing required Libraries

from tkinter import *
from bs4 import BeautifulSoup
import requests

# Function to search Products

def search():
    listbox_1.delete('0', 'end')
    try:
        search = var.get()

        base_url = "https://www.flipkart.com/search?q="+search+"&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        print(search)
        link = requests.get(base_url)

        c = link.content

        
        soup = BeautifulSoup(c, "html.parser")

        if search=="Smartphones" or "Laptops":
            names = soup.find_all("div", "_3wU53n")
            sample = soup.find_all("div", "_1vC4OE")
        if search=="CPUs":
            names = soup.find_all("a", "_2cLu-l")
            sample = soup.find_all("div", "_1vC4OE")
        if search=="Motherboard":
            names = soup.find_all("a", "_2cLu-l")
            sample = soup.find_all("div", "_1vC4OE")
        if search=="Graphics Cards & Ram":
            names = soup.find_all("a", "_2cLu-l")
            sample = soup.find_all("div", "_1vC4OE")

        try:
            list1 = []
            list2 = []

            for product_name in names:
                lol = product_name.contents[0]
                list1.append(lol)
            for price in sample:
                olo = price.contents[0]
                list2.append(olo)

            for x in range(11):
                listbox_1.insert(END, f"Product name: {list1[x]} and price is {list2[x]}")
        except IndexError:
           listbox_1.insert(END, "No product Found")
    except requests.exceptions.ConnectionError:
        listbox_1.insert(END, "Internet not found!")


# Defining fonts
Montserrat = ('Montserrat Semibold', 8)
Poppins = ('Poppins Semibold', 12)


# Main loop for GUI
root = Tk()
root.title("eNfinity Tech Store")
root.geometry("400x315")
root.config(bg="light blue")


# image = Image(Graphic1.png)

# Brand
brand_name = Label(root, text="Welcome to eNfinity Tech Store", font=Poppins, bg="light blue")
brand_name.place(x=80, y=10)

# Drop down Menu
var = StringVar(root)
var.set("Smartphones")
option = OptionMenu(root, var, "Smartphones & Mobiles", "Laptops", "CPUs", "Motherboard", "Graphics Cards & Ram")
option.place(x=130, y = 50)

# Search Button
search_button = Button(root, text="Search", command=search, font=Montserrat, bg="light blue")
search_button.place(x=163, y = 90)

# Scroll Bar
scrollbar = Scrollbar(root, orient= HORIZONTAL)
scrollbar.pack(side=BOTTOM, fill=X)

# Product Info Show
listbox_1 = Listbox(root, width=56, height=10, xscrollcommand=scrollbar.set, font=Montserrat)
listbox_1.place(x=0, y=120)
scrollbar.config(command=listbox_1.xview)

root.mainloop()
