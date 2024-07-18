import datetime

# Initialize storage for each entity
customers = []
rooms_categories = []
today_prices = []
reservations = []
rooms = []
payments = []
invoices = []
bills = []

# Take user input for customer-related data
def customer_func():
    print("Add a new customer:")
    name = input("Enter customer name (e.g., Awais): ")
    email = input("Enter customer email (e.g., awaissmr@gmail.com): ")
    country = input("Enter customer country (e.g., Paksitan): ")
    ssn = input("Enter customer SSN (e.g., 123-45-6789): ")
    gld_num = input("Enter customer GLD number (e.g., G123): ")

    customer = {
        'CustomerID': len(customers) + 1,
        'Name': name,
        'Email': email,
        'Country': country,
        'SSN': ssn,
        'GldNum': gld_num
    }
    customers.append(customer)

# Take user input for room category data
def room_cat_func():
    print("\nAdd a new room category:")
    room_category_name = input("Enter room category name (e.g., Deluxe): ")
    cus_id = int(input("Enter customer ID (e.g., 1): "))

    room_category = {
        'RoomCategoryID': len(rooms_categories) + 1,
        'Name': room_category_name,
        'CusID': cus_id
    }
    rooms_categories.append(room_category)

# Take user input for today's price data
def today_price_func():
    print("\nAdd today's price:")
    today = datetime.date.today()
    days_stay = int(input("how many days will you be staying?"))
    start_date = datetime.timedelta(days=days_stay).strftime('%d-%m-%Y')
    print(start_date)
    end_date = input("Enter end date (dd-mm-yyyy) (e.g., 02-05-2024): ")
    price = float(input("Enter price (e.g., 150.0): "))
    available_rooms = int(input("Enter available rooms (e.g., 5): "))
    date = input("Enter date (dd-mm-yyyy) (e.g., 01-05-2024): ")

    today_price = {
        'PriceID': len(today_prices) + 1,
        'StartDate': start_date,
        'EndDate': end_date,
        'Price': price,
        'AvailableRooms': available_rooms,
        'Date': date
    }
    today_prices.append(today_price)

# Take user input for reservation data
def reservation_func():
    print("\nAdd a new reservation:")
    customer_id = int(input("Enter customer ID (e.g., 1): "))
    reservation_date = input("Enter reservation date (dd-mm-yyyy) (e.g., 01-05-2024): ")
    period = input("Enter reservation period (e.g., 2 days): ")
    start_date_res = input("Enter start date (dd-mm-yyyy) (e.g., 01-05-2024): ")
    end_date_res = input("Enter end date (dd-mm-yyyy) (e.g., 02-05-2024): ")

    reservation = {
        'ReservationID': len(reservations) + 1,
        'CustomerID': customer_id,
        'Date': reservation_date,
        'Period': period,
        'StartDate': start_date_res,
        'EndDate': end_date_res
    }
    reservations.append(reservation)

# Take user input for room data
def room_func():
    print("\nAdd a new room:")
    room_category_id = int(input("Enter room category ID (e.g., 1 )"))
    reservation_id = int(input("Enter reservation ID (e.g., {reservation['ReservationID']}): "))
    check_in_out_date = input("Enter check-in/check-out date (dd-mm-yyyy) (e.g., 01-05-2024): ")

    room = {
        'RoomID': len(rooms) + 1,
        'RoomCategoryID': room_category_id,
        'ReservationID': reservation_id,
        'CheckInOutDate': check_in_out_date
    }
    rooms.append(room)

# Take user input for invoice data
def invoice_func():
    print("\nAdd a new invoice:")
    invoice_status = input("Enter invoice status (e.g., Paid): ")
    invoice_description = input("Enter invoice description (e.g., Room booking): ")

    invoice = {
        'InvoiceID': len(invoices) + 1,
        'Status': invoice_status,
        'InvoiceDescription': invoice_description
    }
    invoices.append(invoice)

# Take user input for payment data
def payment_func():
    print("\nAdd a new payment:")
    payment_method = input("Enter payment method (e.g., Credit Card): ")
    payment_date = input("Enter payment date (dd-mm-yyyy) (e.g., 01-05-2024): ")
    invoice_id = int(input("Enter invoice ID (e.g., 1): "))

    payment = {
        'PaymentID': len(payments) + 1,
        'PaymentMethod': payment_method,
        'Date': payment_date,
        'InvoiceID': invoice_id
    }
    payments.append(payment)

# Take user input for bill data
def bill_func():
    print("\nAdd a new bill:")
    bill_name = input("Enter bill name (e.g., Room Charge): ")
    bill_amount = float(input("Enter bill amount (e.g., 150.0): "))
    bill_date = input("Enter bill date (dd-mm-yyyy) (e.g., 01-05-2024): ")
    bill_type = input("Enter bill type (e.g., Room): ")

    bill = {
        'BillID': len(bills) + 1,
        'Name': bill_name,
        'Amount': bill_amount,
        'Date': bill_date,
        'Type': bill_type
    }
    bills.append(bill)

customer_func()
room_cat_func()
today_price_func()
reservation_func()
room_func()
invoice_func()
payment_func()
bill_func()

# Print data
print("\nCustomers:", customers)
print("Rooms Categories:", rooms_categories)
print("Today Prices:", today_prices)
print("Reservations:", reservations)
print("Rooms:", rooms)
print("Invoices:", invoices)
print("Payments:", payments)
print("Bills:", bills)
