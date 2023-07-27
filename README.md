<div align="center">
<h1 align="center">SerpApi Python Library & Package</h1>
  <img src="https://user-images.githubusercontent.com/78694043/233921372-bb57c347-9005-4b59-8f09-993698a87eb6.svg" width="600" alt="serpapi python library logo">

  <!-- <a href="https://badge.fury.io/py/serpapi-python">![Package](https://badge.fury.io/py/serpapi.svg)</a>
  <a href="https://pepy.tech/project/serpapi-python">![Downloads](https://static.pepy.tech/personalized-badge/serpapi?period=month&units=international_system&left_color=grey&right_color=brightgreen&left_text=Downloads)</a>  -->
  [![serpapi-python](https://github.com/serpapi/serpapi-python/actions/workflows/ci.yml/badge.svg)](https://github.com/serpapi/serpapi-python/actions/workflows/ci.yml)
</div>

This repository is the home of the *soon–to–be* official Python API wrapper for SerpApi (https://serpapi.com). This `serpapi` module allows you to access search data in your Python application.

SerpApi supports Google, Google Maps, Google Shopping, Bing, Baidu, Yandex, Yahoo, eBay, App Stores, and more. Check out the [documentation](https://serpapi.com/search-api) for a full list.

## Current Status

This project is under development, and will be released to the public on PyPi soon.

## Installation

To install the `serpapi` package, simply run the following command:

```sh
$ pip install serpapi
```

Please note that this package is separate from the *soon–to–be* legacy `serpapi` module, which is currently available on PyPi as `google-search-results`.

## Usage

Let’s start by searching for Coffee on Google:

    >>> import serpapi
    >>>> s = serpapi.search(q="Coffee", engine="google", location="Austin, Texas", hl="en", gl="us")

The `s` variable now contains a `SerpResults` object, which acts just like a standard dictionary, with some convenient functions added on top.

Let’s print the first result:

    >>> print(s["organic_results"][0]["link"])
    https://en.wikipedia.org/wiki/Coffee

Let’s print the title of the first result, but in a more Pythonic way:

    >>> print(s["organic_results"][0].get("title"))
    Coffee - Wikipedia

The [SerpApi.com API Documentation](https://serpapi.com/search-api) contains a list of all the possible parameters that can be passed to the API.

## Documentation

Documentation is [available on Read the Docs](https://serpapi-python.readthedocs.io/en/latest/).

## License

MIT

## Contributing

Bug reports and pull requests are welcome on GitHub. Once dependencies are installed, you can run the tests with `pytest`.
