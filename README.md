# Dromedary Lang

<div align="center">
    <img src="https://github.com/VideoCarp/dromedary-lang/blob/main/files/1498B073-7C4E-48E5-BC42-1B3968053214.jpeg" width=250 height=250><br>
  <a href="https://discord.gg/PhES3kc">Join the discord!</a>    <a href="https://github.com/VideoCarp/dromedary-lang/blob/main/CONTRIBUTING.md">Contribute!</a>
  
</div>
                                                                                                                                      
In-progress compiled language.<br>
This language is aimed at mostly performance, but also simplicity.

Currently read-only unless contributing or testing, completely unready.
Do not use any of the files in this repository elsewhere.

Both the lexer and syntax analyzer are unfinished.

Notices:<br>
* The language is a work in progress.
Currently does not run.
* The language works on a 'word' system.
This means it's whitespace sensitive.<br>
Anything more than 1 character, including symbols needs to be separated by whitespace.<br>
```drom
# example
int x = 2
if (x>=1) { # Error!
   println("x is greater than or equal to 1")
}
# instead, use
if (x >= 1) {...}
```

# Features
Here are some features that will be implemented in this lang:<br>
* Easy interoperation with C by typing `#interop` in the line.
Example:
```drom
int main() {
    char msg[] = "Hello World!"; #interop
    printf("%s", msg); #interop
}
```
* Syntactic aliasing, this means users can define global substitutes using a config format.
Example:
```drom
int main() stack
    string hello = "Hello World!"
    if (true) do
       println(hello)
    end
end
```
would be done by using the syntax alias sheet:
```json
{
  " stack\n": " {",
  " do\n": " {",
  "end\n": "}"
}
```
* Standard libraries
Planning to include standard libraries, i.e one of them is 'graphics'.<br>
Example:
```drom
import <graphics>
int main() {
   graphics.draw(x,y,color)
}
```
# Progression
- [x] Lexer
- [ ] Error Handling 
- [ ] Syntax analysis (being worked on)
- [ ] Code generation
