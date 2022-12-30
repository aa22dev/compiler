# Compiler in Python
In this project, I’ll implement different phases of compiler. 
For now, I have completed the implementation of lexical analysis 
and syntax analysis using libraries in python. This project is 
divided into different modules. Module 1 is used for lexical 
analysis phase of compiler and Module 2 is used for syntax 
analysis phase. For now, this implementation works only for expression.

## Module 1
In first module of this project, I achieved lexical analysis phase of compiler by making tokens of an expression entered by user using regex. 

This project first takes the expression as input from user and then output the list of tokens (operands, operators, and parenthesis in one group). This step is achieved by using python library “**re**” in which I made use of regex with split function. The regex that I used is “**(\W)**” which tells the program to split all those characters which are not words into one group and those which are words into one separate group. This splits the whole expression into list of tokens containing operators, operands and parenthesis. 

I also used the filter function to remove the group of spaces and empty strings from the list of tokens.

## Module 2
In second module of this project, I achieved syntax analysis phase of compiler by making a syntax tree of an expression entered by user using “**ast**” library. This library takes expression as input and give abstract syntax tree as output. 

## How to use it?
1. Run the program
2. Enter expression
3. Output will be printed on console

## Code Explanation
### Libraries
|Libraries|Description|
|:----|:----|
|re|Used for creating tokens from expression using regular expressions (regex)|
|ast|Used for making syntax tree from expression|

### Classes
|Class|Purpose|
|:----|:----|
|compiler|To handle every module of this project|

### Variables
|Variables|Data Type|Scope|Description|
|:----|:----|:----|:----|
|c|object|local|Used for initializing class and performing all the actions of modules by taking expression as input|
|exp|string|private (class)|Used for storing input expression|
|token[]|string (list)|public (class)|Used for storing list of tokens generated from the expression|
|syntaxTree|string|public (class)|Used for storing syntax tree generated from the expression|

### Funtions & Methods `(Custom)`
|Functions|Parameters|Type|Description|
|:----|:----|:----|:----|
|__init__|self|constructor|Called when an object for class “compiler” is declared and take expression as input, after that call functions to generate tokens and syntax tree.|
|__str__|self|method (default)|Prints tokens and syntax tree when the object of class is passed to print statement.|
|tokenization|self|method|Used for generating tokens using regular expression|
|syntaxTree|self|method|Used for generating syntax tree from the expression|


### Funtions & Methods `(Default or Library)`
|Functions|Parameters|Type|Description|
|:----|:----|:----|:----|
|input|string|default|Used for taking input from user|
|re.split()|regex, exp|method (library)|This function takes regular expression and user inputted expression as arguments and split the user inputted expression based on regex to generate tokens|
|filter|function, list|default|Takes list as input and filter out the list based on the function passed. In this project, I passed str.strip to remove any spaces or empty items from list.|
|str.strip()|char | None|default|Used to remove whitespaces or specific characters from the beginning and end of the string.|
|list()|iterable | None|default|Generates list from the argument passed or else create empty list.|
|ast.dump()|node, attributes|method (library)|Used for creating a syntax tree from the node passed as argument.|
|ast.parse()|str, method (optional)|method (library)|Used for making a syntax tree from the expression passed as argument and return a node which then passed to ast.dump() for making syntax tree.|

### Working
![Flow Chart](https://github.com/aa22dev/compiler/blob/main/img/diagram.png?raw=true)
