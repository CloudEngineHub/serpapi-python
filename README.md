# User guide
Scrape Google and other search engines from our fast, easy, and complete API using SerpApi.com
This ruby library is meant to scrape and parse results from all major search engine available world wide including Google, Bing, Baidu, Yandex, Yahoo, Ebay, Apple and more using [SerpApi](https://serpapi.com).
SerpApi.com provides a [script builder](https://serpapi.com/demo) to get you started quickly.

## Installation
serpapi can be installed with pip.

```sh
$ python -m pip install serpapi
```

## Quick start
First things first, import the serpapi module:

```python
>>> import serpapi
```
You’ll need a Client instance to make search. This object handles all of the details of connection pooling and thread safety so that you don’t have to:

```python
>>> client = serpapi.Client()
```
To make a search using SerpApi.com client.

```python
>>> parameter = {
      api_key: "secret_api_key", # from serpapi.com
      engine: "google",     # search engine
      q: "coffee",          # search topic
      location: "Austin,TX" # location
    }
    results = searpapi.search(parameter)
```
Putting everything together.
```python
import serpapi

parameter = {
  api_key: "secret_api_key", # from serpapi.com
  engine: "google",     # search engine
  q: "coffee",          # search topic
  location: "Austin,TX" # location
}
results = searpapi.search(parameter)
print(results)
```

### Advanced settings
SerpApi Client uses urllib3 under the hood.
The HTTP connection be tuned by setting the following client specific setting.
  - retries : attempt to reconnect if the connection failed by default: False 
  - timeout : connection timeout by default 60s
for more details:  https://urllib3.readthedocs.io/en/stable/user-guide.html

For example:
parameter = {
  retries: 5,
  timeout: 4.0
}

## Developer's note
### Key goals
 - Brand centric instead of search engine based
   - No hard coded logic per search engine
 - Simple HTTP client (lightweight, reduced dependency)
   - No magic default values
   - Thread safe
 - Easy to extends
 - Defensive code style (raise cutsom exception)
 - TDD
 - Best API coding pratice per platform

### Design
The API design was inpired by the most popular Python packages.
 - urllib3 - https://github.com/urllib3/urllib3
 - Boto3 - https://github.com/boto/boto3

### Quality expectation
 - 0 lint issues using pylint `make lint`
 - 99% code coverage running `make test`

### TODO
 - Add more test
 - Release flow