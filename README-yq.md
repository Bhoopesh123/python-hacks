# YAML Parsing and Templating using yq

It is a lightweight and portable command-line YAML, JSON and XML processor. yq uses jq like syntax but works with yaml files as well as json, xml, properties, csv and tsv. It doesn't yet support everything jq does - but it does support the most common operations and functions, and more is being added continuously.

yq is written in go - so you can download a dependency free binary for your platform and you are good to go! If you prefer there are a variety of package managers that can be used as well as Docker and Podman, all listed below.

# 1. Install yq your Ubuntu Box :  

    brew install yq  
    OR
    snap install yq
    OR
    wget https://github.com/mikefarah/yq/releases/latest/download/yq_linux_amd64 -O /usr/bin/yq &&\
    chmod +x /usr/bin/yq


# 2. Download the latest binary for Windows system as below:  

    https://github.com/mikefarah/yq/releases/download/v4.35.1/yq_windows_amd64.exe
    OR
    https://github.com/mikefarah/yq/releases/download/v4.35.1/yq_windows_amd64.zip
