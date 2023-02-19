# Python with postgres container (the basic)

I) Creating a virtual environment and install dependencies

> This is a naive way to do, I haven't figured out how to add all of this to Makefile

Installing virtual environment at the project directory named `virtual-env`
```
python3 -m venv virtual-env
```

Activate the virtual environment `virtual-env` with:
```
source virtual-env/bin/activate
```

Install all dependencies in requirements.txt using Makefile command
```
make install
```

II) Build app and run

Build and start services
```
make docker-up
```

Run the app to create student table and add records
```
make run
```

III) Check database

A) Using `adminer` container
`adminer` is available at [http://localhost:8080](http://localhost:8080)
Using info from docker-compose.yml to login

B) Using `pgadmin` container
`pgadmin` is available at [http://localhost:5050/](http://localhost:5050)

Using email and pass from docker-compose.yml to login

C) Using `pg_container` container

IV) Shutdown app (bring down docker)
```
make docker-down
```