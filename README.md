# krustofsky

Convert the social security popular baby names dataset to SQLite for fun queries.

## Status

Hacked together in 10m. Use at your own risk!

## Dataset

https://www.ssa.gov/oact/babynames/limits.html

## Usage

**Download the dataset**

```bash
$ wget -O names.zip https://www.ssa.gov/oact/babynames/names.zip
$ unzip names.zip -d data/
```

**Creating the database**

```bash
$ git clone git@github.com:ahawker/krustofsky.git
$ cd krustofsky
$ python import.py names.db
```

**Running queries**

```bash
$ sqlite3 names.db
SQLite version 3.16.0 2016-11-04 19:09:39
Enter ".help" for usage hints.
sqlite> select sum(occurrences) from names;
sum(occurrences)
----------------
348120517
```

```bash
sqlite> .schema
CREATE TABLE names (
    year integer,
    name text,
    sex text,
    occurrences integer
);
CREATE INDEX names_year_idx ON names (year);
CREATE INDEX names_name_idx ON names (name);
CREATE INDEX names_sex_idx ON names (sex);
CREATE INDEX names_occurrences_idx ON names (occurrences);
```

## License

[Apache 2.0](LICENSE)
