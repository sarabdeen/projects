# Sarah Abdeen
# Lab 4
# Question 4
# October 13, 2023

def draw_triangle(baseLength, identation =9, symbol=1):
    if baseLength == 0:
        return

    else:
        print(' ' * identation + '*' * symbol)
        draw_triangle(baseLength - 2, identation - 1, symbol + 2)

baseLength = int(input("Provide a number for the base length"))
draw_triangle(baseLength)
