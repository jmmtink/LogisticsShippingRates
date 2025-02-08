## Shipping Cost Calculator

## Input package weight and shipping rate
weight = float(input("Enter the package weight in kg: "))
rate = float(input("enter the shipping rate per kg: "))

## Calculate the shipping cost
shipping_cost = weight * rate

## Display the result
print(f"Shipping Cost: {shipping_cost} USD")
