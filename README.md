# AirBnB clone - The console

## description of the project
The AirBnB Clone project is an exciting endeavor aimed at developing a comprehensive web application resembling the functionality of the renowned AirBnB platform. The project's first crucial step involves the creation of a command interpreter to manage various AirBnB objects.
## description of the command interpreter:
The command interpreter in the AirBnB Clone project is a fundamental component that enables users to interact with and manage various objects within the application. It operates similarly to a command-line shell but is tailored for a specific use-case, which is managing AirBnB-related entities.
### how to start it and use it

* Start the console in interactive mode:

```bash
$ ./console.py
(hbnb)
```

* Use help to see the available commands:

```bash
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  count  create  destroy  help  quit  show  update

(hbnb)
```

* Quit the console:

```bash
(hbnb) quit
$
```

### Examples

Interactive mode

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
Non Interactive mode
```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```