1.  install psql (16)
2.  start the server with `sudo service postgresql start`
3.  switch to postgresql user with `sudo -iu  postgres`
4.  access psql `psql`
5.  create a new database (no hyphens) `CREATE DATABASE your_database_name;`
6.  create a new user (preferably same name as your machine's user) `CREATE USER your_username WITH PASSWORD 'your_password';`
7.  grant priviliges to the new user on the new database `GRANT ALL PRIVILEGES ON DATABASE your_database_name TO your_username;`
8.  exit postgresql prompt `\q`
9.  exit from postgresql user `exit`
10. connect to the database with the following shell command `psql -U your_username -d your_database_name -h localhost`
