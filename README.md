# COVID_data_exploration

To install dependencies:

```
sudo apt-get install python3-venv
sudo apt install gdal-bin python3-gdal --quiet
sudo apt install python3-rtree --quiet

python3 -m venv env
source env/bin/activate
pip3 install -r requirements.txt
pip3 install git+git://github.com/geopandas/geopandas.git
```


## Ubermedia Cell Phone Mobility

To prep data:
```
code/data_prep/ubermedia_data_prep.sh
```

To run data exploration:
```
python3 code/data_exploration/unique_devices.py
```




