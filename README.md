# S-expression Calculator

Evaluates simplified s-expressions from the command line using python.

Supported functions: `add`, `multiply`

Expression Syntax: `({function} {expression|integer} {expression|integer})`

Examples:
```
> python calc.py "123"
123

> python calc.py "(add 1 2)"
3

> python calc.py "(multiply 3 (add 1 2))"
9
```
