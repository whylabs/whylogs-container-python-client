This package is the auto generated python client for the [whylogs container](https://github.com/whylabs/whylogs-container/).

- [Swagger API](https://whylabs.github.io/whylogs-container-docs/whylogs-container)
- [Docs](https://docs.whylabs.ai/docs/integrations-whylogs-container/)
- [whylogs container](https://github.com/whylabs/whylogs-container/)

## Usage

Install with

```bash
pip install whylogs-container-client
```

## Examples

This example shows how you can bulk upload data from a pandas dataframe.

```python
import pandas
from whylogs_container_client.api import WhylogsApi
from whylogs_container_client import Configuration, ApiClient

config = Configuration()
config.host = 'http://localhost:8080'
client = ApiClient(config)

whylogs_api = WhylogsApi(client)

df = pandas.read_csv('./data.csv')

multiple = df.to_dict(orient="split")
del multiple['index'] # get rid of this to min/max payload size

payload = {
  'datasetId': 'model-1',
  'tags': { # Optional segment tags
    'city': 'seattle'
  },
  'multiple': multiple
}

whylogs_api.track(body=payload ,x_api_key='password')
```

