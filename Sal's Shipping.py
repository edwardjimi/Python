weight = 41.5

#Ground Shipping
ground_flat_shipping = 20.00

if weight <= 2:
  cost_ground = weight * 1.5
elif weight <= 6:
  cost_ground = weight * 3.00
elif weight <= 10:
  cost_ground = weight * 4.00
else: 
  cost_ground = weight * 4.75
  
print("Price of Ground Shipping:",ground_flat_shipping + cost_ground)

#Ground Shippig PREMIUM
ground_shipping_premium = 125.00
print("Price of Premium Ground Shipping:",ground_shipping_premium)

#Drone Shipping 
if weight <= 2:
  cost_drone = weight * 4.50
elif weight <= 6:
  cost_drone = weight * 9.00
elif weight <= 10:
  cost_drone = weight * 12.00
else:
  cost_drone = weight * 14.25

print("Price of Drone Shipping:",cost_drone)