x=float(input("Enter no. of 'Introduction to python programming' books:"))*499
y=float(input("Enter no. of 'Python libraries Cookbook' books:"))*855
z=float(input("Enter no. of 'Data Science in Python' books:"))*645
total=x+y+z
GST=float(total*0.012)
Delivery_charges=250
Total_amount=total+GST+Delivery_charges
print(Total_amount)