# Automation

## 1 Prerequisite

### 1.1 Python

[这里](https://www.python.org/downloads/)下载, `python` and `pip` usually got installed together.

### 1.2 [Selenium WebDriver](https://www.selenium.dev/projects/)

Selenium WebDriver drives a browser natively, as a real user would, either locally or on remote machines.

- [这里](https://chromedriver.chromium.org/downloads)下载 - WebDriver for Chrome，注意选择与自己 chrome 兼容的版本
- 下载解压后放到脚本文件旁边

### 1.3 Selenium

通过 pip3 下载：`pip3 install selenium`

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

通过 pip3 下载：`pip3 install requests`.

## 2 Usage

- python3 jenkins_build.py -e dev -s 2 -n tmc-services

or

- python jenkins_build.py -e dev -s 2 -n tmc-services
