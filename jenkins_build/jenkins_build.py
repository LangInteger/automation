# -*- coding: utf-8 -*-

from selenium import webdriver
import requests
import time
import json
from collections import OrderedDict
import argparse

import logging

# set up logging to file - see previous section for more details
logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(name)-12s %(levelname)-8s %(message)s',
                    datefmt='%m-%d %H:%M',
                    filename='tmp_jenkins_build.log',
                    filemode='w')
# define a Handler which writes INFO messages or higher to the sys.stderr
console = logging.StreamHandler()
console.setLevel(logging.INFO)
# set a format which is simpler for console use
formatter = logging.Formatter('%(name)-12s: %(levelname)-8s %(message)s')
# tell the handler to use this format
console.setFormatter(formatter)
# add the handler to the root logger
logging.getLogger('').addHandler(console)

DOMAIN_URL_PATTERN = "https://{env}-jenkins.teyixing.com/"
JOB_URL_PATH = "view/{env}-tyx-env-{seq}/job/{env}-{name}-env-{seq}"
CONFIG_URL_PATH = JOB_URL_PATH + "/config"


def check_and_get_params():
    text = 'python3 jenkins_build.py'
    parser = argparse.ArgumentParser(text)
    parser.add_argument(
        "-e", "--env", choices=['dev', 'test'], required=True, help="environment, dev/test")
    parser.add_argument(
        "-s", "--seq", choices=['1', '2', '3', '4', '5'], required=True, help="namespace sequence, 1/2/3/4")
    parser.add_argument("-n", "--name", required=True,
                        help="service name, tmc-services")
    parser.add_argument("-b", "--branch", required=False,
                        help="branch name, master")
    args = parser.parse_args()
    return args


def build_url_base(args, pattern):
    return pattern.format(env=args.env, seq=args.seq, name=args.name)


def build_login_url(args):
    return build_url_base(args, DOMAIN_URL_PATTERN)


def build_url(args):
    return build_url_base(args, DOMAIN_URL_PATTERN + JOB_URL_PATH)


def build_config_url(args):
    return build_url_base(args, CONFIG_URL_PATH)


def test_connection(build, args, cookies):
    url = build(args)
    logging.info("Build url: {0}".format(url))

    session = requests.Session()
    if (cookies != None):
        for cookie in cookies:
            session.cookies.set(cookie['name'], cookie['value'])
    response = session.get(url)
    logging.info("Access jenkins with status: {0}".format(
        response.status_code))

    if response.status_code != 200 and response.status_code != 403:
        logging.error(
            "{0} is not accessible, check you params and run again.".format(url))
        exit(2)


def login(args, driver):
    url = build_login_url(args)
    driver.get(url)

    driver.find_element_by_name("j_username").send_keys("admin")
    driver.find_element_by_name("j_password").send_keys("111111")
    driver.find_element_by_name("Submit").click()
    return driver.get_cookies()


def change_git_branch(args, driver):
    if args.branch:
        logging.info("Change build branch to {0}".format(args.branch))
        do_change_git_branch(args, driver)


def do_change_git_branch(args, driver):
    url = build_config_url(args)
    driver.get(url)
    driver.find_element_by_xpath(
        '//*[*name="branches"]/table/tbody/tr[1]/td[2]/input').send_keys(args.branch)

    driver.find_element_by_name("branches").i


def do_build(args, driver):
    url = build_url(args)
    driver.get(url)

    driver.find_element_by_link_text("Build Now").click()
    logging.info("Build started...")


def build():
    args = check_and_get_params()

    test_connection(build_login_url, args, None)
    driver = webdriver.Chrome()
    cookies = login(args, driver)

    test_connection(build_url, args, cookies)
    change_git_branch(args, driver)
    do_build(args, driver)


build()
