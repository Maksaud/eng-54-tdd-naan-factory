# TDD Naan Factory Exercise

This exercise is going to bring together lots of concepts

Learning outcomes include:
- git
- github
- functions
- TDD
- separation of concerns
- DRY code
- DOD


## Installing and running
to run the naan factory do the following

```python
import naan_factory
run_factory()
```



### Test driven development

1. write the test
2. run it, and read the error
3. code make it pass

this helps:
- stops over engineering
- maintainable code
- reduce technical debt
- working code(working code)
- can guide you
- errors can be your guide in complex systems

how it works is that we write unit tests.


#### Unit Tests

Test single pieces of code. Like a function.

••base of a test••

usually has 3 phases
- setup phase (know variables)
- calling of the function/ piece of code with know variables
- asserting for expected output


### User stories for naan Factory

```
#1
As a user, I can use the make_dought with water and flour to make dough.

I have writen a code while testing 

#2
As a user, I can use the bake_dough to with dough to get naan.

#3
As a user, I can use the run_factory with water and flour and get naan.

```