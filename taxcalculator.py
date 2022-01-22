def calc_tax (price, tax_rate):
    val = (tax_rate/100 * price)
    return val

def calc_item_price( price, tax_rate):
    val = calc_tax(price, tax_rate)

    item_price = price + val
    return item_price

def calc_total_price(price, tax_rate, quantity):
    total_price = (price * quantity)
    return total_price

def main():

    price = int(input("enter price of item "))
    tax_rate = int(input("enter value of tax "))
    quantity = int(input("enter number of items "))

    newtax = calc_tax(price, tax_rate)
    newprice= calc_item_price(price,tax_rate)
    Final_cost = calc_total_price(newprice,newtax,quantity)
    print("calculated tax= ", Final_cost)

main()
