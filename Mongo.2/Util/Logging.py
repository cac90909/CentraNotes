import yaml

#For pretty printing user data
def PrettyPrintData(data):
    print("Util.Logging.PrettyPrintData")
    print(yaml.dump(data, default_flow_style=False))