# Highest Odd Number

A beginner-friendly Python program that asks the user to enter 10 integers and identifies the highest odd number among them.

## Description

This project demonstrates how to use:

* `while` loops
* `if` statements
* User input with `input()`
* Integer conversion with `int()`
* Modulo `%` for checking whether a number is odd
* Counters for controlling the number of inputs
* Variables for tracking the highest value
* Conditional output

The program processes exactly **10 numbers** entered by the user.

## How It Works

1. The program starts with `num` set to `0`. This variable stores the highest odd number found so far.
2. A `counter` variable keeps track of how many numbers have been entered.
3. A `while` loop runs until the user has entered 10 numbers.
4. For each input:

   * The user enters an integer.
   * The program checks whether the number is odd using the modulo operator (`%`).
   * If the number is odd and greater than the current highest odd number, `num` is updated.
5. After 10 numbers have been entered:

   * If no odd number was entered, the program displays `No Odd Number was added`.
   * Otherwise, it displays the highest odd number entered.

## Example

### Input

```text
Please enter your 1 digit out of 10: 12
Please enter your 2 digit out of 10: 7
Please enter your 3 digit out of 10: 25
Please enter your 4 digit out of 10: 10
Please enter your 5 digit out of 10: 19
Please enter your 6 digit out of 10: 4
Please enter your 7 digit out of 10: 31
Please enter your 8 digit out of 10: 8
Please enter your 9 digit out of 10: 15
Please enter your 10 digit out of 10: 20
```

### Output

```text
The Highest Odd Number entered was 31
```

## If No Odd Number Is Entered

If all 10 inputs are even numbers:

```text
Please enter your 1 digit out of 10: 2
Please enter your 2 digit out of 10: 4
...
Please enter your 10 digit out of 10: 20

No Odd Number was added
```

## Key Concept

The program uses the modulo operator to determine whether a number is odd:

```python
user_inpt % 2 != 0
```

When an integer is divided by `2`:

* An even number has a remainder of `0`.
* An odd number has a remainder of `1`.

Therefore:

```python
number % 2 != 0
```

means that the number is odd.

## Requirements

* Python 3.x

No external libraries are required.

## Running the Program

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project directory:

```bash
cd highest-odd-number
```

Run the Python program:

```bash
python main.py
```

## Learning Objectives

After completing this exercise, you should understand how to:

* Control repetition with a `while` loop.
* Track iterations using a counter.
* Accept and convert user input.
* Determine whether a number is odd or even.
* Compare values to find the maximum.
* Handle a situation where no qualifying value was entered.

## License

This project is intended for educational purposes and is under MIT License.
