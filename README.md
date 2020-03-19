# Automation

## 1 Utilities

### 1.1 Python

Install with homebrew

- brew install python

### 1.2 [Selenium WebDriver](https://www.selenium.dev/projects/)

Selenium WebDriver drives a browser natively, as a real user would, either locally or on remote machines.

- Download from [ChromeDriver](https://chromedriver.chromium.org/downloads) - WebDriver for Chrome

### 1.3 Selenium

Install with `pip3 install selenium`

### 1.4 PhantomJS

PhantomJS is a headless web browser scriptable with JavaScript.

- Download from [PhantomJS](https://phantomjs.org/download.html)

Add to path virable. Add folowwing lines to `~/.bash_profile`:

```text
PHANTOM_JS_HOME=/your/path/to/phantomjs
export PATH=$PATH:$PHANTOM_JS_HOME/bin
```

then `source ~/.bash_profile` to valid the change.

## 2 Run

> python3 dev-jenkins-tmc-services-env-2.py
