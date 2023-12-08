# Data Processing and Storage Assignment

## Running the Code
This code is intended to be run directly from the console. To execute the code from the console, clone the repository and navigate to it in the terminal, then start python by running `python` or `python3`, depending on your installation of Python. The following example code implements Figure 2, and can be directly copy and pasted into the console.

### Example Code
```
from database import DB
db = DB()
db.get('A')
db.put('A', 5)
db.begin_transaction()
db.put('A', 5)
db.get('A')
db.put('A', 6)
db.commit()
db.get('A')
db.commit()
db.rollback()
db.get('B')
db.begin_transaction()
db.put('B', 10)
db.rollback()
db.get('B')

```

## Future Assignment Changes
I think the instructions for the assignment are pretty straightforward and make sense. One method that could be added is a way to delete from the database to emulate how when a user closes a credit account or a similar situation, the database should raise errors when accessing that user in the future. Two ways I could think of to expand upon the assignment would be to make the database accounts rather than key-value pairs and to implement an additional database that allows dirty writes. I think this could better illustrate the importance of "all or nothing" updates to students, since students would see how allowing illegal transactions can create problems in a real-life scenario.
