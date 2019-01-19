"""
    import.py
    ~~~~~~~~~

    Run this script to convert social security popular baby names dataset to SQLite.
"""
import glob
import io
import os
import sqlite3
import sys


SCHEMA = """
CREATE TABLE IF NOT EXISTS names (
    year integer,
    name text,
    sex text,
    occurrences integer
);

CREATE INDEX IF NOT EXISTS names_year_idx ON names (year);
CREATE INDEX IF NOT EXISTS names_name_idx ON names (name);
CREATE INDEX IF NOT EXISTS names_sex_idx ON names (sex);
CREATE INDEX IF NOT EXISTS names_occurrences_idx ON names (occurrences);
"""


INSERT = """
INSERT OR IGNORE INTO names (
    year,
    name,
    sex,
    occurrences
) VALUES (
    :year,
    :name,
    :sex,
    :occurrences
);
"""


def data_generator():
    """Generator function that yields dicts for each line in each data file"""
    for path in glob.glob('data/*.txt'):
        with io.open(path, 'r') as f:
            print('Processing file {}'.format(path))
            year = os.path.splitext(os.path.basename(path))[0].strip('yob')
            for line in f:
                line = line.strip()
                name, sex, occurrences = line.split(',')
                yield {
                    'year': int(year.lower()),
                    'name': name.lower(),
                    'sex': sex.lower(),
                    'occurrences': int(occurrences)
                }


def create_db(name):
    """Create Sqlite DB using SCHEMA"""
    db = sqlite3.connect(name, check_same_thread=False, detect_types=sqlite3.PARSE_COLNAMES)
    db.executescript(SCHEMA)
    return db


def main(argv):
    """Convert directory of text files to SQLite database"""
    db = create_db(argv[0])
    db.executemany(INSERT, data_generator())
    db.commit()
    db.close()


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
