
1. Export Development Environment
```shell
export FLASK_ENVIRONMENT=development
export FLASK_DEBUG=1
export FLASK_APP=server.py
```
2. Run Flask
```
flask run
```

3. Working with database

* Init database for the first time
```
flask db init
flask db migrate  # make sure 'flask-migrate can detect models directory'
flask db upgrade
```

* Useful commands
```
# View History
flask db history

# Check current migration
flask db current

```
