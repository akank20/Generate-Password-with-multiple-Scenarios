## Generate-Password-with-multiple-Scenarios

#### 1. Define a function that creates random passwords with a given length and complexity. 
``` 
Generate a random password with given length and complexity

    Complexity levels:
        Complexity == 1: return a password with only lowercase chars
        Complexity ==  2: Previous level plus at least 1 digit
        Complexity ==  3: Previous levels plus at least 1 uppercase char
        Complexity ==  4: Previous levels plus at least 1 punctuation char

    parameter 1 length: number of characters
    parameter 2 complexity: complexity level
    return: generated password with given length and complexity
```
#### 2. Define a function that asserts that the complexity levels. 
```
Return the password complexity level for a given password

    Complexity levels:
        Return complexity 1: If password has only lowercase chars
        Return complexity 2: Previous level condition and at least 1 digit
        Return complexity 3: Previous levels condition and at least 1 uppercase char
        Return complexity 4: Previous levels condition and at least 1 punctuation

    Complexity level exceptions (override previous results):
        Return complexity 2: password has length >= 8 chars and only lowercase chars
        Return complexity 3: password has length >= 8 chars and only lowercase and digits

    parameter password: password
    return: complexity level of the given password
```
#### 3. Create a script that generates passwords (with multiple scenarios) and tests them using the assertion function you created in step 2. Them output the result (success or fail).

#### 4. Define a function that retrieves a random user and persist the user into an SQLite database (full name and email). This SQLite database must be persistent (not in memory). 
```
Retrieve a random user from https://randomuser.me/api/ and persist the user (full name and email) into the given SQLite db

    parameter db_path: path of the SQLite db file (to do: sqlite3.connect(db_path))
    return: Success(None)
```

#### 5. Finally, create a script that retrieves few users using the function created on the last step and for each one: create a new password using the password generator function with random length (between 6 and 12) and random complexity level; persist this password into the SQLite database associated with the correspondent user.

