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

> 💡 in CAPITAL are all the SQL specific keywords, in lowercase by convention the "placeholder" for the columns

```bash
sqilte> SELECT * FROM favorites; # star * is a wild-card not a pointer in SQL
```

```bash
sqlite> SELECT language FROM favorites; # give you a specific column you selected
>
sqilte> SELECT language FROM favourites LIMIT 10; #give you only 10 duh!
```

### *Commandlist*
 
 -[ ] AVG  <!-- average -->
 -[ ] COUNT
 -[ ] LOWER
 -[ ] MAX
 -[ ] MIN
 -[ ]UPPER
 ...

 ```bash
 sqlite> SELECT COUNT(*) FROM favorites;
# in Havard example prints:
# +----------+
# | COUNT(*) |
# +----------+
# | 398      |
# +----------+
 sqlite> 
```

```bash
 sqlite> SELECT COUNT(language) FROM favorites;
# in Havard example prints:
# +-----------------+
# | COUNT(language) |
# +-----------------+
# | 398             |
# +-----------------+
 sqlite> 
 ```

```bash
 sqlite> SELECT COUNT(problem) FROM favorites;
# in Havard example prints:
# +----------------+
# | COUNT(problem) |
# +----------------+
# | 398            |
# +----------------+
 sqlite> 
 ```

```bash
 sqlite> SELECT DISTINCT(languages) FROM favorites;
# in Havard example prints:
# +-----------+
# | languages |
# +-----------+
# | Python    |
# | Scratch   |
# | C         |
# +-----------+
 sqlite> 
 ```

```bash
 sqlite> SELECT COUNT(DISTINCT(languages)) FROM favorites;
# in Havard example prints:
# +-----------+
# | languages |
# +-----------+
# | 3         |
# +-----------+
 sqlite> 
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
