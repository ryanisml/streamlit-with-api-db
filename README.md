# STREAMLIT connection with API and postgresql DB
This project is based on python and streamlit library for UI.

# Configuration
Before using this application make sure to:
- install requirements from txt file with terminal.
```
  pip install -r requirements.txt
```
- After install requirements, add new file `secrets.toml` at `.streamlit` folder.
- If you don't have `.streamlit` folder. Create new folder first at root folder.
- Setting new configuration at `secrets.toml` file like :
```
password = "{your password here}"
latitude_sgt = "{add your latitude here}"
longitude_sgt = "{add your longitude here}"
location_name = "{add name of location}"
log_url = '{add api url to get pagination data}'
auth_url = '{add auth url to authentication login}'
tbl_hp = "{add table related to this data}"
tbl_hs = "{add table related to this data}"
tbl_lp = "{add table related to this data}"
tbl_ls = "{add table related to this data}"
db_connection_string = "{add configuration for database connection like host, port, username, password, and database name}"
```

## Documentation
If you have any question related to this project, feel free to contact me at my github <br/>
[My Github Profile](https://github.com/ryanisml)