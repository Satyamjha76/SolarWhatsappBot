import requests
from flask import Flask, request
import requests
from twilio.twiml.messaging_response import MessagingResponse
import SolarData




#THis is Whatsapp Bot Code
app = Flask(__name__)
 
@app.route("/", methods=["POST"])
def bot():
 
    # user input
    user_msg = request.values.get('Body', '').lower()
 
    # creating object of MessagingResponse
    response = MessagingResponse()
 

 
    # displaying result
    if(user_msg=='hi' or user_msg=='hello'):
     msg = response.message("""Welcome to SolaxPower \n1.Today Yield \n2.Total Yield \n3.Current Power \n4.Total Saving Today \n5.Total Saving Till Now \n""")
    elif(user_msg=='1'):
       Result=SolarData.refresh()
       msg=response.message(f"Today Yield is {Result[0]} Kwh ")
    elif(user_msg=='2'):
       Result=SolarData.refresh()
       msg=response.message(f"Total Yield is {Result[1]} Kwh ")
    elif(user_msg=='3'):
       Result=SolarData.refresh()
       msg=response.message(f"Current Power is {Result[2]} W ")
    elif(user_msg=='4'):
       Result=SolarData.refresh()
       msg=response.message(f"Total Saving Today Rs.{Result[0]*7.2}")
    elif(user_msg=='5'):
       Result=SolarData.refresh()
       msg=response.message(f"Total Saving Till Now Rs.{Result[1]*7.2}")
            
 
    return str(response)
if __name__ == "__main__":
    app.run()
