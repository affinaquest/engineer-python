imdb.py is a Python program that reads input from STDIN line by line and executes the following database functions:

SET [name] [value]: Sets the value associated with the given name in the database.
GET [name]: Retrieves and prints the value for the specified name. If the name is not in the database, print "NULL."
DELETE [name]: Deletes the value associated with the specified name from the database.
COUNT [value]: Returns the count of names that have the given value assigned to them. If the value is not assigned to any name, print "0."
BEGIN: Starts a new transaction.
ROLLBACK: Rolls back the most recent transaction. If there is no transaction to rollback, print "TRANSACTION NOT FOUND."
COMMIT: Commits all open transactions and makes changes permanent.
END: Exits the database.

To run it locally, you can use VS Code. Kindly follow the steps below:
1. Install a supported version of Python on your system (note: that the system install of Python on macOS is not supported).
2. Install the Python extension for Visual Studio Code.
3. Select your Python interpreter by clicking on the status bar.
4. Open the Terminal then run the Python script using Python.exe e.g.
   & C:/python.exe C:/imdb.py
5. Run the following commands (press enter to execute each command): <br>
    **GET a** <br>
    GET a => NULL <br>
    **SET a foo** <br>
    SET a => foo <br>
    **SET b foo** <br>
    SET b => foo <br>
    **COUNT foo** <br>
    COUNT foo => 2 <br>
    **COUNT bar** <br>
    COUNT bar => 0 <br>
    **DELETE a** <br>
    DELETE a <br>
    **COUNT foo** <br>
    COUNT foo => 1 <br>
    **SET b baz** <br>
    SET b => baz <br>
    **COUNT foo** <br>
    COUNT foo => 0 <br>
    **GET b** <br>
    GET b => baz <br>
    **GET B** <br>
    GET B => NULL <br>
    **END** <br>
    END
