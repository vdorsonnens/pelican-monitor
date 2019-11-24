# Pelican Monitoring System

## Repository description

| File/Directory                      | Description                                                                    |
|-------------------------------------|--------------------------------------------------------------------------------|
| docker-compose.yml                  |  docker-compose file to easily launch all the required containers              |
| setup/                              | contains all the files and scripts needed for setting up the monitoring system |
| setup/setup.sh                      | script to setup the monitoring system                                          |
| experiment/                         | contains the script for the monitoring experiment                              |
| experiment/generate-fake-traffic.py | monitoring experiment script                                                   |

## Execute the monitoring system

### Prerequesites
- docker
- docker-compose
- python 3
- pip
- virtualenv

### 1. Launch docker-compose
- Run `docker-compose up` in this directory to start the containers

### 2. Create a virtual environment for python
- Start a new shell in this directory
- Create a virtual environment in this directory using `virtualenv env`
- Activate your virtual environment with `source env/bin/activate`

### 3. Setup the database and grafana
- `cd setup`
- `./setup.sh`

### 4. Open Grafana
- In your browser of choice, navigate to [localhost:3000](http://localhost:3000) to open Grafana
- Enter "admin" as username and "admin" as password
- Click on Skip
- In the "Starred dashboards" section, select "Status codes"

### 5. Open the apps
- In your browser of choice, navigate to [localhost:8000](http://localhost:8000) to open the app with the version 4.20.0
- In your browser of choice, navigate to [localhost:8001](http://localhost:8001) to open the app with the version 4.20.1
- Both apps are identical, except for their version number (which you don't see)

### 6. Explore
- Navigate in both apps and look at the Grafana dashboard from time to time. You should see some data points appearing.
- It won't be really interesting yet though, since it's just you, browsing alone.

### 7. Experiment (generate a fake deployment)
- Use the same shell you used from step 2 and 3 (it's important that the virtualenv is still active)
- Navigate to the `experiment/` directory using `cd ../experiment`
- Run `./generate-fake-traffic.py`
- Look at the Grafana dashboard, can you spot the bad release ?

### 8. Cleanup
- In the shell where you launched step 1, do `ctrl+c` to kill the containers.
- Run `docker-compose rm` if you want to remove the containers from your system.
- In the shell were you did step 2, 3, and 7, run `deactivate` to, you guessed it, deactivate the virtual environment
- Delete this repository from your system
