class Height:
    def __init__(self, feet, inches):
        self.feet = feet
        self.inches = inches

    def __sub__(self, other):
        total_inches_self = self.feet * 12 + self.inches
        total_inches_other = other.feet * 12 + other.inches

        total_inches_result = total_inches_self - total_inches_other

        feet_result = total_inches_result // 12
        inches_result = total_inches_result % 12

        return Height(feet_result, inches_result)

    def __str__(self):
        return "{} feet {} inches".format(self.feet, self.inches)
height1 = Height(5, 10)  # 5 feet 10 inches
height2 = Height(3, 9)   # 3 feet 9 inches

result = height1 - height2
print("Result:", result)
