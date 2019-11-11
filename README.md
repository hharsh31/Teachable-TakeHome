# Teachable-TakeHome

## Environment Setup for Run

- Please install brew using command

```sh
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```

- Install python using homebrew: brew install python3
- Install pip3: python3 get-pip.py
- Install selenium using pip: pip3 install selenium
- Install pytest using pip: pip3 install -U pytest
- Install Faker using pip: pip3 install Faker
- Install HTML-reports using pip: pip3 install pytest-html
- Install pytest distributed testing plugin using pip: pip3 install pytest-xdist

## Running Tests on your Local Machine

### Example: 

- For sequential run:

```sh
± |master S:1 U:4 ?:6 ✗| → pytest test_login.py --html=report.html
```

- For parallel run:

```sh
± |master S:1 U:4 ?:6 ✗| → pytest -n 4 test_login.py
```
-n <num> runs the tests by using multiple workers, here it is 4.

