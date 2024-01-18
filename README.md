# Intermediate-sql package

Run an SQL query for the "Intermediate SQL Course" using sql_course package.

## Install

You can install the package by running:

```
pip install git+https://github.com/uplimit/course-intermediate-sql.git
```

Then you can run a SQL query like:

```Python
from sql_course import run, check

### Question: q1_1_1
query = "SELECT * FROM courses"

run(query)
check(q1_1_1 = query)
```

The database and its content is locally constructed from the data contained in this package.
