# Python with postgres container (the basic)

I) Creating a virtual environment and install dependancies

> This is a naive way to do, I haven't figured out how to add all of this to Makefile

Installing virtual environment at the project directory named `virtual-env`
```
python3 -m venv virtual-env
```

Activate the virtual environment `virtual-env` with:
```
source virtual-env/bin/activate
```

Install all dependancies in requirements.txt using Makefile command
```
make install
```