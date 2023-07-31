## Alpha Script Interpreter

The Alpha Script Interpreter is a Python-based script interpreter that reads and executes code from a file with the extension ".alpha". The interpreter provides basic functionality for working with variables, conditionals, loops, functions, and classes. The script includes utility functions for reading and writing files and also enables importing external modules.

### Usage

To use the Alpha Script Interpreter, save your script in a file with the ".alpha" extension. Then, run the interpreter from the command line, passing the path to the ".alpha" file as a command-line argument. For example:


### Functions

#### 1. `add(array, item)`

- Description: Appends an item to the end of the specified array.
- Parameters:
  - `array` (list): The target array.
  - `item` (any): The item to be added to the array.
- Returns: The updated array with the new item added at the end.

#### 2. `remove(array, index)`

- Description: Removes an item from the specified array at the given index.
- Parameters:
  - `array` (list): The target array.
  - `index` (int): The index of the item to be removed.
- Returns: The updated array with the item removed.

#### 3. `find(array, item)`

- Description: Finds the index of the specified item in the array.
- Parameters:
  - `array` (list): The target array.
  - `item` (any): The item to find in the array.
- Returns: The index of the item in the array.

#### 4. File Handling Functions

- `writeFile(filename, content)`: Writes the given content to a file specified by the filename.
- `readFile(filename)`: Reads the content of the file specified by the filename and returns it.
- `appendFile(filename, content)`: Appends the given content to a file specified by the filename.

### Alpha Script Language Features

#### 1. Variable Declaration

- The script supports variable declaration with type annotations. Available types are:
  - `:str=`: String
  - `:int=`: Integer
  - `:dec=`: Decimal (float)
  - `:bool=`: Boolean
  - `:array=`: List
  - `:dict=`: Dictionary

#### 2. Printing

- `log`: Prints the output of the given expression to the console.
- `tlog`: Prints the type of the given expression to the console.

#### 3. Control Flow

- `if`: Starts an if statement block.
- `for`: Starts a for loop block.
- `iterate <-`: Starts a for loop to iterate a specified number of times.
- `while`: Starts a while loop block.
- `else if`: Used within an if statement to add additional conditions.
- `else`: Used within an if statement to provide an alternative block of code.

#### 4. Functions

- `func`: Declares a function.
- `endfunc <-`: Specifies a return statement for a function.

#### 5. Classes

- `class`: Declares a class.

### Syntax Modifications

The Alpha Script Interpreter modifies some Python syntax to make it more user-friendly. The following modifications are applied during the interpretation:

- `userInput`: Replaces `userInput` with `input` for accepting user input.
- `:exit:`: Replaces `:exit:` with `break` to exit loops.
- `private::`: Replaces `private::` with `__` to emulate private variables.
- `??`: Replaces `??` with `self` to represent the class instance.

### Example

Suppose you have a script named "example.alpha":

```alpha
# Example script
name :str= "Alice"
log "Hello, " + name + "!"
```

When executed with the interpreter:

```
python alpha_interpreter.py example.alpha
The output will be:
Hello, Alice!
```
