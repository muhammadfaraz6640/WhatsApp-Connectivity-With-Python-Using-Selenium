# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 11:37:36 2020

@author: Haroon Traders
"""
#importing webdriver from selenium
from selenium import webdriver

#running chrome using ChromeDriver Path stored in your PC
driver=webdriver.Chrome(executable_path=r"C:/Users/Haroon Traders/Desktop/random/chromedriver.exe")

#Running Whatsapp using running chrome driver
driver.get('https://web.whatsapp.com/')

#getting name of the recipient
name=(str(input("enter the name of the Recipient")))

#getting message to deliver
message =(str(input("enter your message here")))

#Waiting for QR code to scan
input('Press anything after QR scan to hold the window')

#sending our recipient name to whatsapp and button click to enter the recipient window
User = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
User.click()

#writing the message to message box of whatsapp
MessageBox = driver.find_element_by_class_name('_2WovP"')  #selectable-text
MessageBox[1].send_keys(message)

#clicking send button
Button = driver.find_elements_by_class_name('_35EW6')
Button.click()