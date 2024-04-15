# Draw a Triangle
# *
# **
# ***
# ****
# *****

def triangle(rows):
    for i in range(rows):
        print("*" * (i + 1))


if __name__ == '__main__':
    triangle(10)
