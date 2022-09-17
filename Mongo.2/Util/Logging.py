import yaml

#For pretty printing user data
def PrettyPrintData(data):
    print(yaml.dump(data, default_flow_style=False))