Hashtime is a quick to implement method that you can use fast in python 2.7+ to allow you to debug remote processes and to get instant notification of crash, errors  or whatever else. Even completed tasks.

Enter your details & save.

Then run:
```
$ python
from support import hashtime
```

Then you will find a file named "support.pyc" put this next to any file you plan on using hashtime with and done.

Just implement:
```
$ python
from support import hashtime
try:
    what?
except Exception,e:
    hashtime(str(e),"subject goes here but is not required")
```
