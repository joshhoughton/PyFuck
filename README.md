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
