# import naan factory functions
# define and run tests

from naan_factory_functions import *

#1
# As a user, i can use the make_dough with water and flour to make dough.
print("calling make_dough with water and flour, expect 'dough' as a result")
print(make_dough('water', 'flour') == 'dough')
print('got:', make_dough('water', 'flour'))

# 2
# As a user, I can use the bake_dough to with dough to get naan.

print("Calling bake_dough should take in the result of make_dough if it is dough and return naan")
print(bake_dough(make_dough('water', 'flour')) == 'naan')
print('got:', bake_dough(make_dough('water', 'flour')))




print("Call run_factory it should take the result of bake which should take result of make dough return naan")
print(run_factory(bake_dough(make_dough('water', 'flour'))) == 'naan')