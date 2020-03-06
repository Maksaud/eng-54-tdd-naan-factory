# define our function here

# 1
# As a user, i can use the make_dough with water and flour to make dough.

# 2
# As a user, I can use the bake_dough to with dough to get naan.

# 3
# As a user, I can use the run_factory with water and flour and get naan.



def make_dough(water, flour):
    # if argument is water and argument 2 is flour
    if water == 'water' and flour == 'flour':
        return 'dough'
    else:
        return 'not dough'


def bake_dough(dough):
    if dough == 'dough':
        return 'naan'
    else:
        return 'not naan'

def run_factory(water, flour):
    return bake_dough(make_dough(water, flour))






















