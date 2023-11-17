
```bash
docker run --name mysql \
    -e MYSQL_ROOT_PASSWORD=root \
    -d -p 3306:3306 \
    --network="myhost" \
    -v MYSQL8:/var/lib/mysql \
    mysql:8.0.27 \
    mysqld --default-authentication-plugin=mysql_native_password
```

```bash
docker run --name mysql \
    -e MYSQL_ROOT_PASSWORD=root \
    -d -p 3306:3306 \
    --network="myhost" \
    -v MYSQL8:/var/lib/mysql \
    mysql:8.0.27 \
    mysqld --default-authentication-plugin=mysql_native_password
```


## create db on mysql naming "metabase"

docker run -d -p 3000:3000 --network="myhost" -e "MB_DB_TYPE=mysql" -e "MB_DB_DBNAME=metabase" -e "MB_DB_PORT=3306" -e "MB_DB_USER=root" -e "MB_DB_PASS=root" -e "MB_DB_HOST=mysql" --name metabase metabase/metabase

secret12345