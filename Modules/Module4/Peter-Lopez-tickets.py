print("Welcome to Bad bunny Concert")
print("The cost of each seat is as follow: Arena standing = $125, Reserved seating 1 = $50, Reserved seating 2 = $40")

Arena_standing = int(input("How many tickets sold for Arena_standing ="))
Reserved_seating_1 = int(input("How many tickets sold for Reserved_seating_1 ="))
Reserved_seating_2 = int(input("How many tickets sold for Reserved_seating_2 ="))

def SectionSales(Arena_standing, Reserved_seating_1, Reserved_seating_2):
    print(f"The cost for Arena_standing tickets is: {int(Arena_standing) * 125}")
    print(f"The cost for Reserved_seating 1 tickets is: {int(Reserved_seating_1) * 50}")
    print(f"The cost for Reserved_seating 2 tickets is: {int(Reserved_seating_2) * 40}")
print()
SectionSales(Arena_standing, Reserved_seating_1, Reserved_seating_2)
Sales_As = Arena_standing * 125
Sales_Rs1 = Reserved_seating_1 * 50
Sales_Rs2 = Reserved_seating_2 * 40
def TicketsTotal(Sales_As, Sales_Rs1, Sales_Rs2):
    print(f"The total of tickets sales is: ${int(Sales_As) + int(Sales_Rs1) + int(Sales_Rs2)}")
print()
TicketsTotal(Sales_As, Sales_Rs1, Sales_Rs2)
