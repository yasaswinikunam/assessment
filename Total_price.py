#Question 1 - 
#Description - Create a small command-line program in Python to calculate the total invoice amount for the below purchases - 
#Book - Introduction to Python Programming : Rs 499.00
#Book - Python Libraries Cookbook : Rs. 855.00
#Book - Data Science in Python : Rs. 645.00
#Taxes and additional charges are described as details - 
#GST : 12%
#Delivery Charges : Rs. 250.00


x=float(input("Enter no. of 'Introduction to python programming' books:"))*499
y=float(input("Enter no. of 'Python libraries Cookbook' books:"))*855
z=float(input("Enter no. of 'Data Science in Python' books:"))*645
total=x+y+z
GST=float(total*0.012)
Delivery_charges=250
Total_amount=total+GST+Delivery_charges
print(Total_amount)
