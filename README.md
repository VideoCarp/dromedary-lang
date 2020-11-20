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
* Macros. This language features macros, which are loaded right after the lexer.

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
- [ ] Lexer (will be rewritten COMPLETELY to speed up, no regex nor splits will be used.)
- [ ] Error Handling 
- [ ] Syntax analysis (being worked on)
- [ ] Code generation
