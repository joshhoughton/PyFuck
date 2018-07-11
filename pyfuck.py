import re
import argparse

MAPPINGS = {
    '+': 'add',
    '-': 'subtract',
    '>': 'increment_pointer',
    '<': 'decrement_pointer',
    '.': 'output',
    ',': 'input',
    '[': 'skip_open',
    ']': 'skip_close'
}


class Brainfuck:
    """Provides methods to interface with the data array.
    Each method corresponds to a Brainfuck instruction.
    """

    def __init__(self, file_name, show_array=False):
        """Creates 30,000 cells, initialised to 0."""

        self.data = [0 for i in range(30000)]
        self.data_pointer = 0
        self.instruction_pointer = 0
        self.program = ''
        self.show_array = show_array

        with open(file_name, 'r') as f:
            program = f.read()
            self.program = re.sub('[^\+\-<>.,\[\]]', '', program)

        self.parens = self.find_pairs(self.program)
        self.invparens = {v: k for k, v in self.parens.items()}

    def run(self):
        """Main loop translating each instruction character"""

        while self.instruction_pointer < len(self.program):
            func = getattr(self,
                           MAPPINGS.get(self.program[self.instruction_pointer]))
            if func:
                func()
            self.instruction_pointer += 1

        if self.show_array:
            print("Array:", self.data[:self.program.count('>')])

    def find_pairs(self, program):
        """Returns a dict object containing the start and ends
        of each set of square brackets.
        """
        pairs = {}
        stack = []

        for i, c in enumerate(program):
            if c == '[':
                stack.append(i)
            elif c == ']':
                if len(stack) == 0:
                    raise IndexError("No matching closing bracket for %i" % i)
                pairs[stack.pop()] = i

        if len(stack) > 0:
            raise IndexError("No matching opening bracket for %i" % i)

        return pairs

    def add(self):
        """Increments the current cell by 1."""
        self.data[self.data_pointer] += 1

    def subtract(self):
        """Decrements the current cell by 1."""
        self.data[self.data_pointer] -= 1

    def increment_pointer(self):
        """Moves pointer to the next cell."""
        if self.data_pointer < 30000:
            self.data_pointer += 1

    def decrement_pointer(self):
        """Moves pointer to the previous cell."""
        if self.data_pointer > 0:
            self.data_pointer -= 1

    def output(self):
        """Outputs the ASCII representation of the value in the current cell.
        """
        print(chr(self.data[self.data_pointer]), end='')

    def input(self):
        """Allows for integer input."""
        valid = False

        while True:
            data = int(input("> "))
            if 0 <= data <= 127:
                break
            print("Input must be an integer less than 127.")

        self.data[self.data_pointer] = data

    def skip_open(self):
        """Skips to the corresponding closing square bracket if the current
        cell is 0."""
        if self.data[self.data_pointer] == 0:
            self.instruction_pointer = self.parens[self.instruction_pointer]

    def skip_close(self):
        """Skips to the corresponding open square bracket if the current cell
        is not 0."""
        if self.data[self.data_pointer] != 0:
            self.instruction_pointer = self.invparens[self.instruction_pointer]


parser = argparse.ArgumentParser('Execute a Brainfuck program.')
parser.add_argument('file_name', metavar='file', type=str,
                    help='Name of Brainfuck program.')
parser.add_argument('-d', dest='show_array', action='store_true',
                    help='Show data array at the end of execution.')

if __name__ == "__main__":
    args = parser.parse_args()

    bf = Brainfuck(args.file_name, show_array=args.show_array)
    bf.run()
