#!/usr/bin/env python3

my_list = ["192.168.0.5", 5060, "UP"]
print("IP:" + my_list[0] )
print("Port:" + str (my_list[1]) )
print("State:" + my_list[2] )
new_list = [5060, "80", "55", "10.0.0.1","10.20.30.1", "ssh"]
print(F"Your pizza at {new_list[3]} has {new_list[0]} pounds of cheese and {new_list[1]} pounds of pepperoni.")
print(F"The total cost is {new_list[2]} thousand dollars."+" Please {new_list[5]} into {new_list[4]} to complete your order.")
