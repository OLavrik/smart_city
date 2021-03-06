# How to setup development environment
 - python 3.6 or higher is required
### Create virtual environment
```
python3 -m venv ./venv
```
### Install requirements
```
source ./venv/bin/activate
python -m pip install ./backend/requirements.txt
```
### Install the package itself in the develop mode
```
# skip if venv is already activated
source ./venv/bin/activate

cd backend
python -m pip install -e ./
```

### Run the backend server

```
# skip if venv is already activated
source ./venv/bin/activate

cd backend
./run.sh
```

### Build docker

```bash
docker build -t "smartcity" ./
```

### Run docker for production

```bash
docker run -d -p 8080:8080 smartcity
```


### Run docker for development (attach to tty)

```bash
docker run -it -p 8080:8080 smartcity
```

#### Developing with PyCharm notes:
- All dependencies stuff can be done via PyCharm menus
- Mark `backend` directory as a *Sources root* - it will become blue
- Create start target at `backend\smartcity\app.py`


## Start mongo
```
docker run --name some-mongo -d -p 27017:27017 mongo
mongo
#> next commands are from Mongo shell
show dbs
# create new database named "smartcity_deb"
use smartcity_deb
#> pause mongo shell
cd json_data
# this will enter data
python ./add_stats_to_db.py
# 




```