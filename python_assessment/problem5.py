import json

filename = 'jsonfile.txt'

with open(filename, 'r') as file:
    json_content = json.loads(file.read())

print("type of json_content is {}".format(type(json_content)))

print("arn is {}".format(json_content['Records'][0]['s3']['bucket']['arn']))
