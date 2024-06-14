class DPDA:
    def __init__(self, transitions, initial_state, acceptance_states):
        self.transitions = transitions
        self.initial_state = initial_state
        self.acceptance_states = set(acceptance_states)
        self.stack = []

    def reset(self):
        self.stack = ['Z']  # Initial stack symbol is Z

    def transition(self, state, symbol, stack_top):
        if (state, symbol, stack_top) in self.transitions:
            next_state, stack_push = self.transitions[(state, symbol, stack_top)]
            return next_state, stack_push
        return None, None

    def is_accepting(self, state):
        return state in self.acceptance_states

    def process_string(self, string):
        current_state = self.initial_state
        self.reset()

        index = 0
        while index <= len(string):
            symbol = string[index] if index < len(string) else '@'
            stack_top = self.stack.pop() if self.stack else '@'
            print(f"Current State: {current_state}, Read Symbol: {symbol}, Stack Top: {stack_top}")
            next_state, stack_push = self.transition(current_state, symbol, stack_top)
            if next_state is None:
                if symbol == '@':
                    break  # No more lambda transitions possible
                print(f"Transition not found for ({current_state}, {symbol}, {stack_top})")
                return False
            print(f"Next State: {next_state}, Push to Stack: {stack_push}")
            current_state = next_state
            if stack_push != '@':  # '@' represents no push
                for item in reversed(stack_push):
                    self.stack.append(item)
            print(f"Stack after push: {self.stack}")

            if symbol != '@':
                index += 1

        result = self.is_accepting(current_state)
        print(
            f"Final State: {current_state}, Final Stack: {self.stack}, Result: {'Accepted' if result else 'Rejected'}")
        return result


def parse_input(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.read().strip().split('\n')

    alphabet_count = int(lines[0])
    alphabet = lines[1].split()
    state_count = int(lines[2])
    transition_count = int(lines[3])

    transitions = {}
    line_index = 4
    for _ in range(transition_count):
        parts = lines[line_index].split()
        I = parts[0].rstrip(',')
        a = parts[1].rstrip(',')
        A = parts[2]
        J = parts[4].rstrip(',')
        B = parts[5] if len(parts) > 5 else '@'
        transitions[(I, a, A)] = (J, B)
        line_index += 1

    acceptance_state_count = int(lines[line_index])
    acceptance_states = lines[line_index + 1].split()

    test_strings = []
    for line in lines[line_index + 2:]:
        if line.strip() == '$':
            break
        test_strings.append(line.strip())

    return alphabet, state_count, transitions, acceptance_states, test_strings


def main(file_path):
    alphabet, state_count, transitions, acceptance_states, test_strings = parse_input(file_path)
    initial_state = '0'
    dpda = DPDA(transitions, initial_state, acceptance_states)

    results = []
    for test_string in test_strings:
        result = dpda.process_string(test_string)
        results.append((test_string, result))

    for test_string, result in results:
        print(f"{test_string}: {'Accepted' if result else 'Rejected'}")


# Usage example:
file_path = 'test.txt'
main(file_path)
