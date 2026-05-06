[https://github.com/tna0y/Python-random-module-cracker](https://github.com/tna0y/Python-random-module-cracker)

`mt19937` treats int seed `s` and `-s` the same.

Check function `static int random_seed(RandomObject *self, PyObject *arg)`
Of `Modules/_randommodule.c`
Because class `Random` inherit from `_random` which is the `c` module.