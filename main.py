import os
import wget

headers = {"User-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36 Edg/109.0.1518.61"};

if __name__ == "__main__":
    while (True):
        url = input ("请输入网址\n")
        if url == "-1":
            break
        head = url.rfind ("/")
        tail = url.rfind ("@")
        if head == -1 or tail == -1:
            print ("网址不合法!")
            continue
        head += 1
        RealUrl = url [0:tail]
        fileName = url [head:tail]
        filePath = "Download/" + fileName
        if not os.path.exists ("Download/"):
            os.mkdir ("Download/")
        wget.download (RealUrl, filePath)
        print ("\n")