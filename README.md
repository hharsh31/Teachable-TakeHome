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

## Running Tests on your Local Machine

cd into Tests directory : cd ~/Teachable-TakeHome/Tests
Run command : pytest test_login.py --html=report.html

Example: 
2019-11-11 13:09:51 ⌚  Harshs-Air in ~/Teachable-TakeHome/Tests
± |master S:1 U:4 ?:6 ✗| → pytest test_login.py --html=report.html

