import yaml

# Specify the path to your YAML file
yaml_file_path = '/mnt/c/Users/Public/github/python-hacks/examples/first.yaml'

# Open the YAML file and load its content
with open(yaml_file_path, 'r') as yaml_file:
    yaml_content = yaml.safe_load(yaml_file)
    
# Now you can work with the loaded YAML content as a Python data structure
print(yaml_content)
