# Extract subset of rows for a particular date.

tail newcastle.csv -n 1000000 > newcastle_1000000.csv
cat newcastle_1000000.csv | grep 20200320 > newcastle_date_20200320.csv
