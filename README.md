# DPDA (Deterministic Pushdown Automaton) Implementation in Python

This repository contains a Python implementation of a Deterministic Pushdown Automaton (DPDA). A DPDA is a type of automaton used in formal language theory, capable of recognizing context-free languages.

## Overview

The DPDA implementation includes the following components:

- **DPDA Class**: Represents the deterministic pushdown automaton with methods for initialization, state transition, acceptance checking, and string processing.
- **parse_input Function**: Parses an input file to extract alphabet, states, transitions, acceptance states, and test strings.
- **main Function**: Entry point that reads an input file, initializes a DPDA, processes test strings, and prints results.

## DPDA Class

### Methods

- **`__init__(self, transitions, initial_state, acceptance_states)`**
  - Initializes the DPDA with transition rules, initial state, and acceptance states.
  
- **`reset(self)`**
  - Resets the stack to its initial state ('Z').

- **`transition(self, state, symbol, stack_top)`**
  - Retrieves the next state and stack symbols to push based on current state, input symbol, and top of the stack.

- **`is_accepting(self, state)`**
  - Checks if a given state is an acceptance state.

- **`process_string(self, string)`**
  - Processes an input string to determine if it is accepted by the DPDA.

## parse_input Function

- **`parse_input(file_path)`**
  - Reads an input file and extracts alphabet symbols, states, transitions, acceptance states, and test strings.

## main Function

- **`main(file_path)`**
  - Entry point of the script. It reads an input file, initializes a DPDA, processes each test string, and prints the acceptance result.

## Input File Format

The input file format is structured as follows:

1. Number of symbols in the alphabet.
2. Alphabet symbols (space-separated).
3. Number of states.
4. Number of transitions.
5. Transition rules in the format: `current_state, input_symbol, stack_top -> next_state, stack_push`.
6. Number of acceptance states.
7. Acceptance states (space-separated).
8. Test strings (one per line), terminated by a line containing only `$`.

### Example Input File (`test.txt`)

```
2
a b
3
5
0, a, Z -> 1, AZ
1, a, A -> 1, AA
1, b, A -> 2, @
2, b, A -> 2, @
2, @, Z -> 2, @
1
2
aaabbb
aabb
$
```

## Usage

To use the DPDA implementation:

1. Ensure Python 3.x is installed.
2. Clone the repository or download the `dpda.py` file.
3. Create an input file following the specified format (like `test.txt`).
4. Run the script with the command:

   ```bash
   python dpda.py test.txt
   ```

5. View the results for each test string printed to the console.

## Output

The output displays each test string followed by whether it was accepted or rejected by the DPDA.

### Example Output

```
aab: Accepted
abb: Rejected
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.