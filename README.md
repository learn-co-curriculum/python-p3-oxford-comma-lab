# Oxford Comma Lab

## Learning Goals

- Convert data types
- Practice iterating through lists
- Use various methods to manipulate lists and strings

***

## Key Vocab

- **Interpreter**: a program that executes other programs. Python programs
require the Python interpreter to be installed on your computer so that they
can be run.
- **Python Shell**: an interactive interpreter that can be accessed from the
command line.
- **Data Type**: a specific kind of data. The Python interpreter uses these
types to determine which actions can be performed on different data items.
- **Exception**: a type of error that can be predicted and handled without
causing a program to crash.
- **Code Block**: a collection of code that is interpreted together. Python
groups code blocks by indentation level.
- **Function**: a named code block that performs a sequence of actions when it
is called.
- **Scope**: the area in your program where a specific variable can be called.

***

## Converting Types

In Python, there are a few methods available to us for converting data types.
For example, it is possible to convert an integer into a float, a string that
represents a number into a number type, and a string into a list or a list into
a string, among other conversions. In this lesson we'll learn about converting
between lists and strings, but you can learn about more of them in [this
tutorial on converting data types in Python][type-conversion].

### String to List

To convert a string into a list, we can use the [`.split`][split] method:

```py
"Hello World!".split()
# => ["Hello", "World!"]
```

The `.split` method uses whitespace as the separator by default. If we want to
use a different separator, we can pass it as an argument:

```py
"hippo,giraffe,monkey,horse".split(",")
# => ["hippo", "giraffe", "monkey", "horse"]
```

### List to String

We can use Python's [`.join`][join] method to convert a list to a string. The
syntax for the command is:

```py
separator.join(items-to-join)
```

The method is called on a string which represents the separator you want to be
inserted between each of the items in the list. If you want to join the items
into a single string without any separators, you would call the method on an
empty string:

```py
''.join(["a", "b", "c"])
# => "abc"
```

On the other hand, if we want to separate each item in our list with a `" :-) "`
("smiley face"), we would do this:

```py
" :-) ".join(["a", "b", "c"])
# => "a :-) b :-) c"
```

## Instructions

To get started, run `pipenv install` to create your virtual environment and
`pipenv shell` to enter the virtual environment. Then run `pytest -x` to run
your tests. Use these instructions and `pytest`'s error messages to complete
your work in the `lib/` folder.

Write a function `oxford_comma()` in the `lib/oxford_comma.py` file that takes an
array of string elements as an argument and converts it into a string using the
[Oxford comma](http://en.wikipedia.org/wiki/Serial_comma).

```py
oxford_comma(["fiddleheads", "okra", "kohlrabi"])
# => "fiddleheads, okra, and kohlrabi"
```

**Hint:** You will need to refer to the section above about converting lists
into strings, but note that coding this function will involve a couple of extra
challenges.

This might be a challenging lab, so take your time using Google and playing
around with your code. Good luck and have fun!

***

## Resources

- [Wikipedia: Serial Comma](http://en.wikipedia.org/wiki/Serial_comma)
- [DigitalOcean: How to Convert Data Types in Python 3][type-conversion]

[type-conversion]: https://www.digitalocean.com/community/tutorials/how-to-convert-data-types-in-python-3
[split]: https://www.w3schools.com/python/ref_string_split.asp
[join]: https://www.w3schools.com/python/ref_string_join.asp
