import turtle

# Global constants for initial settings
INITIAL_BRANCH_LENGTH = 100
BRANCH_SHRINK_FACTOR = 0.7
ANGLE = 45
WIDTH = 2
SPEED = 15
COLOR = "lightgreen"
BG_COLOR = "white"


def draw_pythagorean_tree(branch_length, turtle_obj, angle, level):
    """
    Draws a Pythagorean tree using recursive method.

    :param branch_length: The initial length of the branch.
    :param turtle_obj: The turtle object used for drawing.
    :param angle: The angle at which branches are drawn.
    :param level: The recursion depth representing the level of the tree.
    """
    if level == 0:
        return

    turtle_obj.forward(branch_length)
    turtle_obj.right(angle)
    draw_pythagorean_tree(
        BRANCH_SHRINK_FACTOR * branch_length, turtle_obj, angle, level - 1
    )
    turtle_obj.left(2 * angle)
    draw_pythagorean_tree(
        BRANCH_SHRINK_FACTOR * branch_length, turtle_obj, angle, level - 1
    )
    turtle_obj.right(angle)
    turtle_obj.backward(branch_length)


def main():
    try:
        level = int(input("Enter the level of the tree: "))
    except ValueError:
        print("Please enter a valid number for the level.")
        return

    screen = turtle.Screen()
    screen.bgcolor(BG_COLOR)

    t = turtle.Turtle()
    t.speed(SPEED)
    t.color(COLOR)
    t.width(WIDTH)

    t.left(90)

    draw_pythagorean_tree(INITIAL_BRANCH_LENGTH, t, ANGLE, level)

    screen.exitonclick()


if __name__ == "__main__":
    main()
