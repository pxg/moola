#Moola

Track finances in a Google spreadsheet. Project was created as dealing with logic in a spreadsheet was coming fiddly.

Has been developed using Python 3.4.3.

#Installation:
```
pip install requirements.txt
pip install -e .
```
To run (some of these steps will be automated as future tasks):
 - Create a Google Spreadsheet calls "Money" or "Money dev"
 - Use the Google APIs to create a `credentials.json` file and place in the `moola` director
 - Give the `client_email` in `credentials.json` access to the Google Spreadsheet
 - Create a worksheet calls transactions

To run the application type `moola` on the terminal then follow the prompts.

##Testing

To run the tests:
```
py.test
```
