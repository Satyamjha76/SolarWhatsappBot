import requests
def refresh():
    response = requests.get("https://eu.solaxcloud.com/proxyApp/proxy/api/getRealtimeInfo.do?tokenId=20240624145224679951552&sn=SRGBFJVYX3") 
    # print(response.status_code)
    data = response.json()
    result=data['result']
    TodayYield=result['yieldtoday']
    TotalYield=result['yieldtotal']
    CurrentPower=result['powerdc1']
    return TodayYield,TotalYield,CurrentPower

if __name__ == "__main__":
    refresh.run()