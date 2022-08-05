

## setup

## installation
```bash
pip install sendgrid
```

## go to send grid 
1. create a  single sender identity
2. create a full access api key

## in a setup.sh put the following lines
```bash
echo "export SENDGRID_API_KEY='Your-api-key'" > sendgrid.env
echo "sendgrid.env" >> .gitignore
source ./sendgrid.env
```

## run the line 
* `source setup.sh` 
* run the python file `python send_grid.py`