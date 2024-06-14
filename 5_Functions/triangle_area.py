
def calc_triangle_area(width, height):
    area = (width*height)/2
    return area

def main():
    print("Calculate area of triangle")
    width = int(input("Enter width of triangle: "))
    height = int(input("Enter height of triangle: "))
    area = calc_triangle_area(width, height)
    print("Area of triangle is", area)

main()