# Picnic Game

It is not just a game...
so what is the purpose of this tiny python project, you might be asking.

With this picnic_game project, I have been able to:
- write a program that accepts multiple positional arguments
- use if, elif, and else to handle conditional branching with three or more
options
- find and alter items in a list
- format a list into a new string




The program that will correctly format the items we're taking on our picnic.
For one item, it should print the one item:

```
$ ./picnic.py sandwiches
You are bringing sandwiches.
```

For two items, place "and" in between:

```
$ ./picnic.py sandwiches chips
You are bringing sandwiches and chips.
```

For three or more items, use commas and "and":

```
$ ./picnic.py sandwiches chips cake
You are bringing sandwiches, chips, and cake.
```

If the `--sorted` flag is present, the items should first be sorted:

```
$ ./picnic.py sandwiches chips cake --sorted
You are bringing cake, chips, and sandwiches.
```

If no items are given, print a brief usage:

```
$ ./picnic.py
usage: picnic.py [-h] [-s] str [str ...]
picnic.py: error: the following arguments are required: str
```

if the `--comma` flag is present, then the  the Oxford comma is removed:

```
$ ./picnic.py sandwiches chips cake
You are bringing sandwiches, chips and cake.
```

if the `--char` flag is present, the items are seperated by the given character:

```
$ ./picnic.py sandwiches chips cake
You are bringing sandwiches: chips: cake
```

Respond to `-h` and `--help` with a longer usage:

```
$ ./picnic.py -h
usage: picnic.py [-h] [-s] str [str ...]

Picnic game
