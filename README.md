# open-university-learning-analytics-app

In my localhost I already have a user gdpr who was created in the previous project. I will contibue using this user to access the database for this project.

```
GRANT pg_read_all_data TO gdpr;
GRANT pg_write_all_data TO gdpr;
```

Here is how the `.env` file looks like
```
HOST=localhost
USER=gdpr
PW=gdpr
DB=open_university
PORT=5432
```