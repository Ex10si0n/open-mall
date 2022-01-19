# ISI - webapi

Python backend of ISI project (Group 8)

## Deployment

### Database - MariaBD:

Docker deployment:

```bash
docker run --name mariadb-isi -e MYSQL_ROOT_PASSWORD=<password> -p 3306:3306 -d mariadb:10.3 --log-bin --binlog-format=MIXED
```

Tables initalization:

```bash
schema.sql
```

### API Python environment

```bash
conda env create -f environment.yml
```
