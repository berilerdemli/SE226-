import math

def circle_area(radius):
    if radius <= 0:
        raise ValueError("Radius must be positive.")
    return math.pi * radius ** 2

def circle_perimeter(radius):
    return 2 * math.pi * radius

def rectangle_area(width, height):
    return width * height

def rectangle_perimeter(width, height):
    return 2 * (width + height)

def triangle_area(base, height):
    return 0.5 * base * height




def remove_duplicates(data_list):
    return list(set(data_list))

def strip_whitespaces(string_list):
    return [item.strip() for item in string_list]




def calculate_mean(num_list):
    return sum(num_list) / len(num_list)

def find_maximum(num_list):
    return max(num_list)

def find_minimum(num_list):
    return min(num_list)




def shape_main():
    shape_functions = {
        "circle": circle_area,
        "rectangle": rectangle_area,
        "triangle": triangle_area
    }

    shape = input("Enter shape (circle, rectangle, triangle): ").lower()

    try:
        if shape == "circle":
            r = float(input("Enter radius: "))
            print("Area:", shape_functions[shape](r))

        elif shape == "rectangle":
            w = float(input("Enter width: "))
            h = float(input("Enter height: "))
            print("Area:", shape_functions[shape](w, h))

        elif shape == "triangle":
            b = float(input("Enter base: "))
            h = float(input("Enter height: "))
            print("Area:", shape_functions[shape](b, h))

        else:
            print("Invalid shape!")

    except Exception as e:
        print("Error:", e)




def data_main():
    user_input = input("Enter numbers (comma separated): ")

    try:
        parts = user_input.split(",")
        stripped = strip_whitespaces(parts)
        numbers = [float(x) for x in stripped]

        unique_numbers = remove_duplicates(numbers)

        print("Mean:", calculate_mean(unique_numbers))
        print("Max:", find_maximum(unique_numbers))
        print("Min:", find_minimum(unique_numbers))

    except Exception as e:
        print("Error:", e)




if __name__ == "__main__":
    print("1. Shape Calculator")
    print("2. Data Analyzer")

    choice = input("Choose (1 or 2): ")

    if choice == "1":
        shape_main()
    elif choice == "2":
        data_main()
    else:
        print("Invalid choice")
