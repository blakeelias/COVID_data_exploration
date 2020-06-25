# Extract subset of rows for a particular date.

DATA_DIR="./data"

echo "Running from directory:"
echo $(pwd)
echo

tail ${DATA_DIR}/newcastle.csv -n 1000000 > ${DATA_DIR}newcastle_1000000.csv
cat ${DATA_DIR}/newcastle_1000000.csv | grep 20200320 > ${DATA_DIR}/newcastle_date_20200320.csv
