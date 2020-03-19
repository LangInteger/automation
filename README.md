# Automation

## 1 Utilities

### 1.1 Python

You know how to install, `python` and `pip` usually got installed together.

### 1.2 [Selenium WebDriver](https://www.selenium.dev/projects/)

Selenium WebDriver drives a browser natively, as a real user would, either locally or on remote machines.

- Download from [ChromeDriver](https://chromedriver.chromium.org/downloads) - WebDriver for Chrome
- Add to `PATH` system envirables

### 1.3 Selenium

Install with `pip3 install selenium`

### ~~1.4 PhantomJS~~

PhantomJS is a headless web browser scriptable with JavaScript.

- Download from [PhantomJS](https://phantomjs.org/download.html)

Add to path virable. Add folowwing lines to `~/.bash_profile`:

```text
PHANTOM_JS_HOME=/your/path/to/phantomjs
export PATH=$PATH:$PHANTOM_JS_HOME/bin
```

then `source ~/.bash_profile` to valid the change.

### 1.5 requests

An alternative for PhantomJS, to get http response code.

Install with `pip3 install requests`.

## 2 Run

> python3 jenkins_build.py -e dev -s 2 -n tmc-services
