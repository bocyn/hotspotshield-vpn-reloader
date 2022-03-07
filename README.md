
## TLDR: Hotspotshield VPN automatic reloader

### Requirements
* Hotspotshield [account](https://hotspotshield.aura.com/sign-in)
* tested only on Linux system (debian based)
* python >= 3.8
* pip
* virtualenv (optional)

### Setup 
* [install](https://www.hotspotshield.com/vpn/vpn-for-linux/) hotspotshield client
* `hotspotshield account signin`
* clone this [repository](https://github.com/bocyn/hotspotshield-vpn-reloader)
* setup virtualenv (optional)
* install required packages from requirements.txt `pip install -r /path/to/requirements.txt`


### Run
* `cd` to cloned repo
* run `python3 app/main.py`

### Environment variables descriptions and default values

* interval in `seconds` in which connection is checked to be alive
```shell script
KEEP_ALIVE_INTERVAL=5
```

* interval in `seconds` to publish log message about current status of VPN connection
```shell script
PRINT_STATUS_INTERVAL=5
```

* interval in `seconds` in which re-connection to other location should be made
```shell script
DISCONNECT_INTERVAL=180
```

* interval in `seconds` to wait stop command
```shell script
STOP_INTERVAL=5
```
