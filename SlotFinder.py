#This is a clone and modification of https://github.com/pcomputo/Whole-Foods-Delivery-Slot/blob/master/amazon_fresh_delivery_slot_chrome.py
#Import all required libraries below , this runs on Python 3.4 
#Install ChromeDriver (this is a browser instance that launches and is controlled by the code below
#be sure to fill in the required fields (email etc) before running
#When the chromedriver window launches, login to amazon (make sure cart is already filled) then go to checkout/delivery page 
#it will start to refresh the page now and look for HTML that indicates a slow opens up, i've added code so it emails me, you may want
#to whitelist the email you send from in case your email client puts it to junk. or modify the code to notify you another way.

import bs4
from selenium import webdriver 
import sys
import time
import os
import smtplib
  
def AWS_SlotFinder(checkoutUrl):
   headers = {
       'User-Agent': 'Chrome/41.0.2228.0 Safari/537.36',
   } 
   Webdriver = webdriver.Chrome("ADD CHROMEDRIVER.EXE PATH HERE")
   Webdriver.get(productUrl)          
   html = Webdriver.page_source
   soup = bs4.BeautifulSoup(html,features="lxml")
   time.sleep(60)
   no_open_slots = True
 
   while no_open_slots:
      Webdriver.refresh()
      print("refreshed")
      html = Webdriver.page_source
      soup = bs4.BeautifulSoup(html,features="lxml")
      time.sleep(4) 
      slot_pattern = 'Next available'
      try:
         next_slot_text = soup.find('h4', class_ ='ufss-slotgroup-heading-text a-text-normal').text
         if slot_pattern in next_slot_text:
            print('SLOTS OPEN!')
            os.system('echo "Slots for delivery opened!"')
            s = smtplib.SMTP('smtp.office365.com', 587)
            s.starttls()
            s.login("insert email", "insert password")
            s.sendmail("INSERT SENDER EMAIL", "INSERT DESTINATION EMAIL", "Subject:Open Slot Alert" +"\n\n"+"Found slots!!!!!!!!!!!!!")
            print("sent mail")
            s.quit()
            no_open_slots = False
            time.sleep(1400)
      except AttributeError:
         continue 
         
      try:
         slot_opened_text = "Not available"
         all_dates = soup.findAll("div", {"class": "ufss-date-select-toggle-text-availability"})
         for each_date in all_dates:
            if slot_opened_text not in each_date.text:
               print('SLOTS OPEN!')
               os.system('say "Slots for delivery opened!"')
               no_open_slots = False
               time.sleep(1400)
      except AttributeError:
         continue 
         
      try:
         no_slot_pattern = 'No delivery windows available. New windows are released throughout the day.'
         if no_slot_pattern == soup.find('h4', class_ ='a-alert-heading').text:
            print("NO SLOTS!")
      except AttributeError:
            print('SLOTS OPEN!')
            os.system('say "Slots for delivery opened!"')
            no_open_slots = False
  
AWS_SlotFinder('https://www.amazon.com/gp/buy/shipoptionselect/handlers/display.html?hasWorkingJavascript=1')
