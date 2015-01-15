#!/usr/bin/env python

import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

#create firefox profile for auto download and save
def get_firefox_profile():

    fp = webdriver.FirefoxProfile()

    fp.set_preference("browser.download.folderList",2)
    fp.set_preference("browser.download.manager.showWhenStarting",False)
    fp.set_preference("browser.download.dir", os.getcwd())
    fp.set_preference("browser.helperApps.neverAsk.saveToDisk", 
        "application/zip")
    return fp

def run_driver(prof, uname, pword):
    #get to the initial page
    #chrome was causing issues for iFrames
    driver = webdriver.Firefox(firefox_profile=prof)
    driver.get("https://courseworks.columbia.edu/portal/login")

    #type username into correct field
    usern = driver.find_element_by_name("username")
    usern.send_keys(uname)

    #type password into correct field
    passw = driver.find_element_by_name("password")
    passw.send_keys(pword)

    #click submit
    submit = driver.find_element_by_name("submit")
    submit.click()

    #open to assignments page
    ds_cw_path = "https://courseworks.columbia.edu/portal/site/COMSW3134_001_2014_3/"
    assignments_path = "page/af109703-a9a8-4808-a580-277555af3252"
    driver.get(ds_cw_path)
    driver.get(ds_cw_path + assignments_path)

    #switch into iframe
    #open to homework 4 grades
    driver.switch_to.frame("Mainbf3d7569xad7fx43efx858bxc3fbf2fae0a3")
    grade_button = driver.find_element_by_xpath("//form[@name='listAssignmentsForm']/table/tbody/tr[2]/td[2]/div/a[3]")
    grade_button.click()

    #download all link
    download_all = driver.find_element_by_xpath("//form[@name='viewForm']/div[@class='listNav']/a[1]")
    download_all.click()

    #download grade file (maybe more later on?)
    grade_cbox = driver.find_element_by_xpath("//input[@id='gradeFile']")
    grade_cbox.click()
    download_button = driver.find_element_by_xpath("//input[@name='downloadButton']")
    download_button.click()
    real_download_button = driver.find_element_by_xpath("//div[@class='messageInformation']/p[1]/a[1]")
    real_download_button.click()

    driver.close()

def main():
    
    username = raw_input('UNI: ')
    password = raw_input('Password: ')

    profile = get_firefox_profile()

    run_driver(profile, username, password)

if __name__ == '__main__':
    main()