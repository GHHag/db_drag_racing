import requests
import json
# Läser in och formaterar datan som skickas sedan till Redis server
# Detta kan bli en Locust fil!
with open('generated_data.json', 'r') as file:
    json_data = json.loads(file.read())
    for i in json_data:
        print(i)
        print(type(i))
        retail_unit = i.get('retailUnit')
        id = i.get('id')
        data = {k: v for k, v in i.items() if k not in ['retailUnit', 'id']}
        data_str = json.dumps(data)
        requests.post(
            f"http://localhost:8080/redis/hset?hash={retail_unit}&key={id}&value={data_str}"
        )
