user_left=True
dict={}

def highest_bidder(dict):
    winner=""
    highest_bid=0
    for bidder in dict:
        bid_amount=dict[bidder]
        if bid_amount>highest_bid:
            highest_bid=bid_amount
            winner=bidder
    print(f"Winner is {winner} with bid amount :{highest_bid}")


while user_left:
    name=input("Enter your name :")
    bid_price=int(input("Enter your bid :"))
    dict[name]=bid_price
    # print(dict)
    user_left_to_bid=input("User left to bid ?").lower() #yes or None
    if user_left_to_bid=="no":
        user_left=False
        highest_bidder(dict)
    else:
        user_left_to_bid="yes"
 
