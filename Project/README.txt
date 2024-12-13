To work with postgres CLI inside the contianer following are the things:

1. psql -U <username> -d <database_name>
2. \l => to list all DBs
3. \dt => to list all tables in given DB
4. select * from "table_name"; => because it automatically, converts Uppercase to lowercase in command, so we use "".