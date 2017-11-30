# Moola

Track finances in a Google spreadsheet. Project was created as dealing with logic in a spreadsheet was becoming fiddly. Developed using Python 3.6.2.

# Installation

I recommend first creating a python3 virtual environment:
```
mkvirtualenv --python=`which python3` moola
```

Then install requirements and the package:
```
pip install -r requirements.txt
pip install -e .
```
To run (some of these steps will be automated as future tasks):
 - Create a Google Spreadsheet called "Money" or "Money dev"
 - Use the Google APIs to create a `credentials.json` file and place in the `moola` director
 - Give the `client_email` in `credentials.json` access to the Google Spreadsheet
 - Create a worksheet calls transactions

To run the application type `moola` on the terminal then follow the prompts.

## Testing

To run the tests:
```
py.test
```

## To run

From the root of the repo run `moola` and follow the instructions.
