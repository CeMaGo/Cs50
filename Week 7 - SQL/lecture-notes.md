# CS50 Week 7 lecture Notes on SQL


## Code snippets

// look up: flat file database (.csv files / excel)
// sqlite3 in use


CRUD,  
 - [ ]CREATE, INSERT
 - [ ]SELECT
 - [ ]UPDATE
 - [ ]DELETE, DROP
 - [ ]...
 
```sql
CREATE TABLE table (column type,...);
```

### set up file

this is a onetime operation to create the data, now you have the database going and can just enter it the next time you want to use it

```bash
$ sqlite3 favorites.db  #<!-- creates a new database, binary file in sqlite format, named favorites.db, in the sqlite version 3, --> //Enter
Are you sure you want to create favorites.db? [y/N] y
#  <!-- sqilte> not the dollar sign prompt but the sqlite-propmt -->
sqlite> .mode csv                 # <!-- sets the db up for the right code format (in this case excel .csv) -->
 sqlite> .import favorites.csv favorites       <!-- (dot)Commant + fileWeWishToAdd + nameOfTheTabel-->
 sqlite> .quit     #<!-- to exit database and return to terminal -->
 $ ls favorites.csv favorites.db
favorites.csv favorites.db
$ #<!-- `ctrl` + `l` to clear the terminal -->
```

... entering the database the next time/day/whenever:

```bash
$ sqlite3 favorites.db # note that we call sqlite3 and give it the file we want to run
sqlite> .schema # /Enter  --> this gives you the schema of this database table
CREATE TABLE IF NOT EXISTS "favorites"(
    "Timestamp" TEXT, "language" TEXT, "problem" TEXT);
sqlite>
```

```bash
SELECT columns FROM table;
...
```





> Command list
> - WHERE
> - LIKE
> - ORDER BY
> - LIMIT
> - GROUP BY


> Command list
> - WHERE
> - LIKE
> - ORDER BY
> - LIMIT
> - GROUP BY
