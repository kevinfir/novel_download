#本程式為爬取網路小說網站，自行下載並編譯章節
import ssl #匯入SSL取得網路憑證
import urllib.request as req #匯入REQUEST請求伺服器允許進入網站
import bs4 #解析網頁的module
n = 169 #爬取最後一章網路小說的章節
for i in range(123,n+1): #一個FOR迴圈從第123章開始抓取網路小說
    url = "https://www.bg3.co/novel/pagea/lingjingxingzhe-maibaoxiaolangjun_%d.html"%i 
    #欲爬取網頁的網址
    ssl._create_default_https_context = ssl._create_unverified_context
    #使用ssl連線模組，因為欲爬的網站為https開頭，需要認證
    request1 = req.Request(url)
    #讓REQUEST1物件化
    response =  req.urlopen(request1)
    #定義response為req.urlopen請求伺服器進入網站，把response定義為請求伺服器回應這動作的變數
    data = response.read().decode("utf-8")#定義data變數為讀取網站數據，解碼方式為utf-8
    root = bs4.BeautifulSoup(data,"lxml")#定義root變數為beautifulsoup解析data方式為lxml
    data_content = root.find_all("p")#找尋所有P標籤
    with open("chapter%d.html"%(i),mode="w",encoding="utf-8") as file:#自行建立檔案
        file.writelines(str(data_content))#把BS4的物件轉為STRING並且寫入資料
    



#https://www.xpiaotian.com/zh_hant/book/89763/    