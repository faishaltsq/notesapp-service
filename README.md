create a virtual env
```bash
virtualenv .venv

```

activate the virtual env
```bash
.venv\Scripts\activate
```


install all package
```bash
pip install flask Flask-Migrate Flask-SQLAlchemy python-dotenv pymysql
```

initial db to create migration folder
```bash
flask db init
```

migrate the database
```bash
flask db migrate -m "create table user and notes"
```

to create table
```bash
flask db upgrade
```

to run apps on debug mode
```bash
flask --debug run

```"# notesapp-service" 
"# notesapp-service" 
