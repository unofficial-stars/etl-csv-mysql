# ETL CSV to MySQL
This repository provides a simple ETL (Extract, Transform, Load) script that reads a CSV file, transforms the data, and loads it into a MySQL database. Follow the steps below to set up and run the ETL process.

## Setup

1. Clone this repository:
```bash
git clone https://github.com/your-username/etl-csv-mysql.git
```

2. Install the required Python packages:
```bash
pip install -r requirements.txt
```

## MySQL Database Setup
Ensure that you have Docker installed. You can set up a MySQL 8 container by running the following commands:
```bash
docker run --name mysql \
    -e MYSQL_ROOT_PASSWORD=root \
    -d -p 3306:3306 \
    --network="myhost" \
    -v MYSQL8:/var/lib/mysql \
    mysql:8.0.27 \
    mysqld --default-authentication-plugin=mysql_native_password
```

## Build and Run Docker Image
1. Build the Docker image for the ETL process:
```bash
docker build -t etl-csv-mysql:latest .
```

2. Run the Docker image with the ETL command:
```bash
docker run -it --rm --name etl-csv-mysql \
    --link mysql \
    --network="myhost" \
    -v "$(pwd)":/application \
    -p 1270:1270 \
    etl-csv-mysql:latest \
    python etl_csv_msql.py input.csv mysql testing_traffic
```
Replace `input.csv`, `mysql`, and `testing_traffic` with your actual `input file`, `database host`, `database name`, and `table name`.

## Metabase Integration
To visualize your data using Metabase, follow these steps:

1. Create a MySQL database named "metabase" using the Docker command below:
```bash
docker run -d -p 3000:3000 --network="myhost" \
    -e "MB_DB_TYPE=mysql" \
    -e "MB_DB_DBNAME=metabase" \
    -e "MB_DB_PORT=3306" \
    -e "MB_DB_USER=root" \
    -e "MB_DB_PASS=root" \
    -e "MB_DB_HOST=mysql" \
    --name metabase metabase/metabase
```

2. Access Metabase at http://localhost:3000, and set up your account using the provided credentials.

Now, you can use Metabase to explore and visualize the data in your MySQL database.

Note: The default Metabase username is `admin` and the password is `secret12345`. Make sure to change the password for security reasons.

Feel free to customize the configuration according to your needs. Happy data processing!