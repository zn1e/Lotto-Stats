"""
    A simple program for displaying information and calculations from
Lotto New Zealand
"""

"""
    - Function for creating a matplotlib graph of all lotto numbers
    - Function for graphs of all bonus ball
    - Function for graphs of power ball
    - Function for statistics of occurences of each ball 
    - Function for each range (0-9, 10-19, 20-29, 30-40)
    - Create a math for probability of the next number based
    from given data    
"""
MENU = """Options:
    [l] Distributed graph of all winning lotto numbers
    [p] Distribted graph of all power ball
    [q] Quit the program 
    """
VALID_INSTRUCTIONS = {'l', 'b', 'p', 'q'}
LOTTO_COUNTS = 'counts.txt'
POWER_BALL_COUNTS = 'power ball counts.txt'
TOTAL_DRAWS_LOTTO = 2298
TOTAL_DRAWS_POWERBALL = 1588
import matplotlib.pyplot as plt
import numpy as np


def main():
    """Ask for an instructions. Calculates the graph of winning lotto
    numbers, bonus ball, and power ball.
    """
    print(MENU)
    instruction = ''
    
    while instruction != 'q':
        instruction = read_instruction()
        if instruction == 'l':
            lotto_numbers_graph(lotto_percentages(LOTTO_COUNTS))
        elif instruction == 'p':
            power_ball_graph(power_ball_percentages(POWER_BALL_COUNTS))


def read_instruction():
    """Read the instruction."""
    instruction = read_valid_instruction(VALID_INSTRUCTIONS, str.lower)
    return instruction


def read_valid_instruction(valids, transformer=None):
    """Check if instruction is valid."""
    instruction = input('Select option: ')

    if transformer:
        instruction = transformer(instruction)
    while instruction not in valids:
        print('Please select a valid option.')
        instruction = input('Select option: ')
    return instruction


def lotto_numbers_graph(lotto_dictionary):
    """Create a graph of distribution of lotto numbers."""
    percentages_list = [percentage for key, percentage in lotto_dictionary.items()]

    ys = np.array(percentages_list)
    xs = np.linspace(1, 40, 40)

    axes = plt.axes()
    bars = axes.bar(xs, ys)
    axes.set_xticks(xs)
    axes.set_xticklabels([int(x) for x in xs])
    axes.set_xlabel('Lotto Number', fontweight='bold')
    axes.set_ylabel('Percentage (%)', fontweight='bold')
    axes.set_title('Distribution of Lotto Numbers', fontweight='bold')

    for bar in bars:
        height = bar.get_height()
        percentage = height / float(TOTAL_DRAWS_LOTTO) * 100
        axes.text(bar.get_x() + bar.get_width() / 2, height, f'{percentage:.3f}', ha='center', va='bottom')

    plt.yticks(np.arange(0, 101, 10))
    plt.tight_layout()
    plt.show()



def power_ball_graph(power_ball_dictionary):
    """Create a graph of distribution of power ball."""
    percentages_list = [percentage for key, percentage in power_ball_dictionary.items()]

    ys = np.array(percentages_list)
    xs = np.linspace(1, 10, 10)

    axes = plt.axes()
    bars = axes.bar(xs, ys)
    axes.set_xticks(xs)
    axes.set_xticklabels([int(x) for x in xs])
    axes.set_xlabel('Power Ball Number', fontweight='bold')
    axes.set_ylabel('Percentage (%)', fontweight='bold')
    axes.set_title('Distribution of Power Ball Numbers', fontweight='bold')

    for bar in bars:
        height = bar.get_height()
        percentage = height / float(TOTAL_DRAWS_POWERBALL) * 100
        axes.text(bar.get_x() + bar.get_width() / 2, height, f'{percentage:.3f}', ha='center', va='bottom')

    plt.yticks(np.arange(0, 101, 5))
    plt.tight_layout()
    plt.show()


def lotto_percentages(filename):
    """Return a dictionary of percentages of each lotto number.
    """
    with open(filename) as file:
        contents = file.read().splitlines()
        
        percentages_dict = {}
        for line in contents:
            line = list(map(int, line.split(',')))
            key = line[0]
            percentages_dict[key] = (line[1] / float(TOTAL_DRAWS_LOTTO)) * 100
        return percentages_dict


def power_ball_percentages(filename):
    """Return a dictionary of percentages of each bonus ball.
    """
    with open(filename) as file:
        contents = file.read().splitlines()
        
        percentages_dict = {}
        for line in contents:
            line = list(map(int, line.split(',')))
            key = line[0]
            percentages_dict[key] = (line[1] / float(TOTAL_DRAWS_POWERBALL)) * 100
        return percentages_dict


if __name__ == '__main__':
    main()

