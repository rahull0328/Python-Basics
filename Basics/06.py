from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

first_name = input("Enter First Name: ")
last_name = input("Enter Last Name: ")
city = input("Enter City: ")
mobile = input("Enter Mobile Number: ")
email = input("Enter Email ID: ")

pdf_file = "User_Details.pdf"
c = canvas.Canvas(pdf_file, pagesize=letter)
c.setFont("Helvetica", 14)

c.drawString(200, 750, "User Details Report")
c.line(200, 745, 400, 745) 

c.drawString(100, 700, f"First Name     : {first_name}")
c.drawString(100, 675, f"Last Name      : {last_name}")
c.drawString(100, 650, f"City           : {city}")
c.drawString(100, 625, f"Mobile Number  : {mobile}")
c.drawString(100, 600, f"Email ID       : {email}")

c.save()

print(f"PDF file '{pdf_file}' created successfully!")
