# PyFuck
Command-line brainfuck interpreter written in Python 3
If you have any suggestions or improvements, please go ahead! 

Any program executed may access up to 30,000 cells.

## Usage
```
python3 brainfuck.py [-d] file_name

-d       Display the data array once execution is complete.
```

## Example
```
$ python3 brainfuck.py -d helloworld.bf
Hello World!
Array: [0, 0, 72, 100, 87, 33, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
```
## Brainfuck Instructions
**>**	increment the data pointer (to point to the next cell to the right).

**<**	decrement the data pointer (to point to the next cell to the left).

**+**	increment (increase by one) the byte at the data pointer.

**-**	decrement (decrease by one) the byte at the data pointer.

**.**	output the byte at the data pointer.

**,**	accept one byte of input, storing its value in the byte at the data pointer.

**\[** if the byte at the data pointer is zero, then instead of moving the instruction pointer forward to the next command, jump it forward to the command after the matching ] command.

**]**	if the byte at the data pointer is nonzero, then instead of moving the instruction pointer forward to the next command, jump it back to the command after the matching \[ command.
