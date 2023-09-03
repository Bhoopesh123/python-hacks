# python-hacks for uploading data to mysql Database using Python

# 1. Install Python3 in your Ubuntu Box as below:  

    brew install python3
    or
    sudo apt update
    sudo apt -y upgrade
    python3 -V
    sudo apt install -y python3-pip
    pip3 install pyyaml

# 2. Install below package for installing yaml package for reading yaml files  

    pip3 install mysql-connector-python

# 3. Run below upload code to load data to database below:  

    cd examples
    python3 mysql_upload.py
