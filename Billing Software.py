import os
from datetime import date

class Item:
    def __init__(self, name, price, qty):
        self.name = name
        self.price = price
        self.qty = qty

class Order:
    def __init__(self, customer, phone_number, date):
        self.customer = customer
        self.phone_number = phone_number
        self.date = date
        self.items = []

    def add_item(self, item):
        self.items.append(item)

def generate_bill_header(name, phone_number, date):
    print("\n\n")
    print("\t     Ziya's Store")
    print("\t   -----------------")
    print(f"Date: {date}")
    print(f"Invoice To: {name}")
    print(f"Phone Number: {phone_number}")  
    print("---------------------------------------")
    print("Items\t\tQty\t\tTotal")
    print("---------------------------------------")
    print("\n")

def generate_bill_body(item, qty, price):
    total = qty * price
    print(f"{item}\t\t{qty}\t\t{total:.2f}")

def generate_bill_footer(total):
    print("\n")
    discount = 0.1 * total
    net_total = total - discount
    cgst = 0.09 * net_total
    sgst = 0.09 * net_total
    grand_total = net_total + 2 * cgst
    
    print("---------------------------------------")
    print(f"Sub Total\t\t\t{total:.2f}")
    print(f"Discount @10%\t\t\t{discount:.2f}")
    print("\t\t\t\t-------")
    print(f"Net Total\t\t\t{net_total:.2f}")
    print(f"CGST @9%\t\t\t{cgst:.2f}")
    print(f"SGST @9%\t\t\t{sgst:.2f}")
    print("---------------------------------------")
    print(f"Grand Total\t\t\t{grand_total:.2f}")
    print("---------------------------------------\n")

def save_order(order):
    with open("StoreBill.dat", "a") as file:
        file.write(f"Customer: {order.customer}\n")
        file.write(f"Phone Number: {order.phone_number}\n")
        file.write(f"Date: {order.date}\n")
        file.write("Items:\n")
        for item in order.items:
            file.write(f"{item.name}\t{item.qty}\t{item.price:.2f}\n")
        file.write("\n")

def show_all_invoices():
    if not os.path.exists("StoreBill.dat"):
        print("No invoices found.")
        return
    
    with open("StoreBill.dat", "r") as file:
        print("\n  *****Your Previous Invoices*****\n")
        print(file.read())

def search_invoice_by_name(name):
    found = False
    if not os.path.exists("StoreBill.dat"):
        print("No invoices found.")
        return
    
    with open("StoreBill.dat", "r") as file:
        invoice_lines = file.readlines()
        i = 0
        while i < len(invoice_lines):
            if f"Customer: {name}" in invoice_lines[i]:
                found = True
                print(f"\t*****Invoice of {name}*****\n")
                print(invoice_lines[i], end="")
                i += 1
                while i < len(invoice_lines) and "Customer:" not in invoice_lines[i]:
                    print(invoice_lines[i], end="")
                    i += 1
                break
            i += 1
        
    if not found:
        print(f"Sorry, the invoice for {name} does not exist.")

def search_invoice_by_phone(phone_number):
    found = False
    if not os.path.exists("StoreBill.dat"):
        print("No invoices found.")
        return
    
    with open("StoreBill.dat", "r") as file:
        invoice_lines = file.readlines()
        i = 0
        while i < len(invoice_lines):
            if f"Phone Number: {phone_number}" in invoice_lines[i]:
                found = True
                customer = ""
                while "Customer:" not in invoice_lines[i]:
                    if "Customer: " in invoice_lines[i]:
                        customer = invoice_lines[i].strip().split(": ")[1]
                    i += 1
                if customer:
                    print(f"\t*****Invoice of {customer}*****\n")
                print(invoice_lines[i], end="")
                i += 1
                while i < len(invoice_lines) and "Customer:" not in invoice_lines[i]:
                    print(invoice_lines[i], end="")
                    i += 1
                break
            i += 1
        
    if not found:
        print(f"Sorry, no invoice found for the phone number {phone_number}.")

def main():
    contFlag = 'y'

    while contFlag == 'y':
        os.system("clear")
        total = 0
        invoiceFound = False

        print("\t============Ziya's Store============")
        print("\n\nPlease select your preferred operation")
        print("\n\n1.Generate Invoice")
        print("2.Show all Invoices")
        print("3.Search Invoice by Customer Name")
        print("4.Search Invoice by Phone Number")
        print("5.Exit")

        opt = int(input("\n\nYour choice:\t"))

        if opt == 1:
            os.system("clear")
            customer = input("\nPlease enter the name of the customer:\t")
            phone_number = input("Please enter the phone number:\t")
            today = date.today().strftime("%Y-%m-%d")
            order = Order(customer, phone_number, today)

            n = int(input("\nPlease enter the number of items:\t"))

            for i in range(n):
                print(f"\n\nPlease enter item {i + 1}:")
                item_name = input("Item name:\t")
                qty = int(input("Quantity:\t"))
                price = float(input("Unit price:\t"))
                item = Item(item_name, price, qty)
                order.add_item(item)
                total += qty * price

            generate_bill_header(order.customer, order.phone_number, order.date)
            for item in order.items:
                generate_bill_body(item.name, item.qty, item.price)
            generate_bill_footer(total)

            save_bill = input("\nDo you want to save the invoice [y/n]:\t")
            if save_bill.lower() == 'y':
                save_order(order)
                print("\nInvoice saved successfully.")

        elif opt == 2:
            os.system("clear")
            show_all_invoices()

        elif opt == 3:
            os.system("clear")
            name = input("Enter the name of the customer:\t")
            search_invoice_by_name(name)

        elif opt == 4:
            os.system("clear")
            phone_number = input("Enter the phone number of the customer:\t")
            search_invoice_by_phone(phone_number)

        elif opt == 5:
            print("\n\t\t Bye Bye :)\n\n")
            break

        else:
            print("Sorry, invalid option")

        contFlag = input("\nDo you want to perform another operation? [y/n]:\t")

    print("\n\t\t Bye Bye :)\n\n")

if __name__ == "__main__":
    main()
