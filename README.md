# S-expression Calculator

Evaluates simplified s-expressions from the command line using python.

 Supported functions: `add`, `multiply`

Expression Syntax: `({function} {expression|integer} {expression|integer})`

#### Examples:
```
> python calc.py "123"
123

> python calc.py "(add 1 2)"
3

> python calc.py "(multiply 3 (add 1 2))"
9
```

#### How it works:

* **My first thought was recursion. This problem seems perfect for it, as you can recursively
evaluate expressions, right?** Well sure, but the problem is that in order to evaluate a nested 
expression, you need to match opening and closing parenthesis of outer functions without
evaluating inner functions.

* **Instead, I was able to loop through each inner function, starting with the first to close.** 
This way I could simply find the first instance of `)` and find the nearest `(` before it to put
together an inner function that contained no nested functions, which was easy to evaluate. Keep 
doing that until all functions are evaluated, and you end up with the final value.