# AmazonFresh_Delivery_Finder
This Script will refresh Amazon Fresh Delivery Page and notify you if a Slot opens. 


This is a clone and modification of https://github.com/pcomputo/Whole-Foods-Delivery-Slot/blob/master/amazon_fresh_delivery_slot_chrome.py

Import all required libraries below , this runs on Python 3.4 
Install ChromeDriver (this is a browser instance that launches a chrome window and is controlled by the code below.

In the code be sure to fill in the required fields (email username/password/provider etc) before running
Feel free to change that try clause to whatever notification method you would like (text , popup, alarm) 

When the chromedriver window launches, login to amazon (make sure your Amazon Fresh cart is already filled),
then go to checkout/delivery page. 

Tt will start to refresh the page now and look for HTML that indicates a slot opens up, my version sends an email on a slot match,

You may want to whitelist the email you send from in case your email client puts it to junk if you choose email. 

** Please also pick one slot so there is enough for all of us. For example, if you are a group of roomates, consolidate into one order **

Thanks! 
