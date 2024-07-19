import matplotlib.pyplot as plt
import numpy as np

def draw_recursive_tree(ax, depth, x, y, branch_length, angle, branch_angle):
    if depth == 0:
        return

    # Calculate the end point of the branch
    x_end = x + branch_length * np.cos(np.radians(angle))
    y_end = y + branch_length * np.sin(np.radians(angle))

    # Draw the branch
    ax.plot([x, x_end], [y, y_end], color='brown', linewidth=depth)

    # Recursively draw the left and right subtrees
    draw_recursive_tree(ax, depth - 1, x_end, y_end, branch_length * 0.7, angle + branch_angle, branch_angle)
    draw_recursive_tree(ax, depth - 1, x_end, y_end, branch_length * 0.7, angle - branch_angle, branch_angle)

def main():
    # Set up the figure and axis
    fig, ax = plt.subplots()
    ax.set_aspect('equal')
    ax.axis('off')  # Turn off the axis

    # Initial parameters
    initial_depth = 10
    initial_x = 0
    initial_y = 0
    initial_branch_length = 100
    initial_angle = 90  # Pointing upwards
    branch_angle = 30

    # Profundidad 3
    #draw_recursive_tree(ax, 3, initial_x, initial_y, initial_branch_length, initial_angle, branch_angle)
    # Profundidad 5
    #draw_recursive_tree(ax, 5, initial_x, initial_y, initial_branch_length, initial_angle, branch_angle)
    # Profundidad 7
    #draw_recursive_tree(ax, 7, initial_x, initial_y, initial_branch_length, initial_angle, branch_angle)
    # Profundidad 10
    draw_recursive_tree(ax, 10, initial_x, initial_y, initial_branch_length, initial_angle, branch_angle)

    # Show the plot
    plt.show()

if __name__ == "__main__":
    main()
