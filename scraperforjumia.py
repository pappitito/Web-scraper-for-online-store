import requests
from bs4 import BeautifulSoup
import smtplib

def sendMailwPrice(pageLink, recipientMail, price):
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        
        #input your own username and password like so - server.login('username','password)
        server.login('example@gmail.com', 'examplepassword')
        subject = 'System has found the iphone 13 buy now'
        body = 'The page with the price of iPhone 13 of ' + str(price) + ' has been found click this link ' + pageLink
        message = f"Subject: {subject}\n\n{body}"

        server.sendmail(
        'example@gmail.com', recipientMail, message
        )
        print('email has been sent to ' + recipientMail)
    
        server.quit()
    except:
        print('could not send mail')

def itemFound(thePrice, pageLink):
    print("the item with price " + str(thePrice) + " has been found in the link " + pageLink)






#setup for obtaining website info
#replace the user agent property with your unique user agent
headers = {
    'User-Agent': 'user agent can be obtained by searching on web browser- my user agent'
}







#to find prices throughout the page
#to never end this loop until we find our item
loopEnd = 0
while loopEnd < 1 :
 
    print('checking for item...')
    i = 0  
    while i < 55:

        #dynamic url
        my_url = 'https://www.jumia.com.ng/catalog/?q=iphone+13&page='+ str(i) + '#catalog-listing'
        page = requests.get(my_url, headers=headers)

        soup = BeautifulSoup(page.content, 'html.parser')
        price_array = []
        price = soup.find_all(attrs={"class":"prc"})

        for item in price:
            str_item = str(item)
            filtered_item = str_item[19:-6]
            symb = '₦'
            if filtered_item != '' and symb not in filtered_item:
                price_array.append(filtered_item)
    

        #to check the prices for the price we are looking for
        for item in price_array:
            new_item = item.replace(",","")
            priceCheck = 5445
            if int(new_item) == priceCheck:
                theLink = my_url
                itemFound(priceCheck, theLink)
                sendMailwPrice(theLink,'exampletwo@yahoo.com',priceCheck)
                sendMailwPrice(theLink, 'examplethree@gmail.com',priceCheck)
                loopEnd += 2
            
        i += 1
    i = 0
 
print('the loop has ended')


