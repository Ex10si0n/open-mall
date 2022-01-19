# ISI - webapi

Python backend of ISI project (Group 8)

## Deployment

Deployed by Docker:

```bash
docker run --name mariadb-isi -e MYSQL_ROOT_PASSWORD=<password> -p 3306:3306 -d mariadb:10.3 --log-bin --binlog-format=MIXED
```

Tables initalization:

```bash
schema.sql
```
