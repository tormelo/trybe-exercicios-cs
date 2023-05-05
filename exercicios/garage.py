from stack import Stack

"""
Complexidade O(1) ao adicionar e O(n) ao remover por conta da iteração na pilha
"""

garage = Stack()

while True:
    print("Operations: ")
    print("1. Add car")
    print("2. Remove a car")
    print("3. List cars")
    print("4. Close")
    option = int(input("Option: "))

    if option == 1:
        license_plate = input("License plate: ")
        garage.push(license_plate)
        print("Car " + license_plate + " parked")
    elif option == 2:
        car_to_remove = input("Car to remove (license plate): ")
        street = Stack()
        removed = False

        while not garage.is_empty():
            current_car = garage.pop()

            if current_car == car_to_remove:
                print("Car " + car_to_remove + " removed")
                removed = True
                break

            street.push(current_car)

        while not street.is_empty():
            garage.push(street.pop())

        if not removed:
            print("There is no car parked with this plate")
    elif option == 3:
        print("Parked vehicles: " + str(garage))
    else:
        break
