# Jenkins Build

Trigger your jenkins build via commandline.

## 1 Prerequisite

### 1.1 Python

Download [here](https://www.python.org/downloads/), `python` and `pip` usually got installed together.

### 1.2 [Selenium WebDriver](https://www.selenium.dev/projects/)

Selenium WebDriver drives a browser natively, as a real user would, either locally or on remote machines.

- Download [here](https://chromedriver.chromium.org/downloads) - WebDriver for Chrome，chose version compatible with your local chrome version
- Place to folder of script after download

### 1.3 Selenium

Download via pip3：`pip3 install selenium`

### 1.4 requests

An alternative for PhantomJS, to get http response code.

Download via pip3：`pip3 install requests`.

## 2 Usage

- python jenkins_build.py -e dev -s 2 -n tmc-services
  - -e/--env: of which kind of environment
  - -s/--seq: of which sequence of this kind of environment
  - -n/--name: of which service 

In some situation, may only this works:

- python3 jenkins_build.py -e dev -s 2 -n tmc-services
