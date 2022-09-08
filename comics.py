import urllib.request
import requests
import urllib3
from bs4 import BeautifulSoup
import time
import os

def main():
    file = open("links.txt","r")
    
    all_lines = (file.readlines())
    
    file.close()

    headers = {}
    headers['User-Agent'] = "Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:48.0) Gecko/20100101 Firefox/48.0"
    comic_link = []
    comic_link2 = []
    comic_link3 = []
    comic_image = []
    
    for url in all_lines:
        time.sleep(1)
        req = urllib.request.Request(url, headers = headers)
        html = urllib.request.urlopen(req).read()
        soup = BeautifulSoup(html,'html.parser')

        for a in soup.find_all('a', href=True):
            #print(a['href'])
            comic_link.append(a['href'])
##        print(comic_link)
        for pop in range(0,16):     #usually 17, but some may need 16
            comic_link.pop(0)
        for pop2 in range(0,8):
            comic_link.pop()
        #print(comic_link)

        for link in comic_link:
            # find length
            image_name = 1
            for  counter in range(1,500):
                
                link_page = link + "/" + str(counter)
##                print(link_page)
                response = requests.get(link_page)
                print(response.status_code)
                    
                if response.status_code != 200:
                    break
                else:
                    print(link.split("/"))
##                    print(link.split("/")[-1])
##                    print(link.split("/")[-2])
                    newpath = ''

                    if "%20" in link.split("/")[-1]:
                        temp = link.split("/")[-1]
                        temp2=temp.replace("%20", " ")
                        print("here")
##                        print(temp2)
                        newpath = r'E:\BackupD1\PyCharm Projects\Comics download' + '\\' + link.split("/")[-2] + "\\" + temp2
                    else:
                        newpath = r'E:\BackupD1\PyCharm Projects\Comics download' + '\\' + link.split("/")[-2] + "\\" + link.split("/")[-1]
                    print("newpath " +newpath)

                    newfolderpath = r'E:\BackupD1\PyCharm Projects\Comics download' + '\\' + link.split("/")[-2]
                    #newpath = r'C:\Users\borshs\Documents\PyCharm Projects\Comics download' + '\\' + link.split("/")[-2] + "\\" + link.split("/")[-1]
                    
                    if not os.path.exists(newfolderpath):
                        os.makedirs(newfolderpath)
##                    else:
##                        print("exist",newfolderpath)
##                        break
                    if not os.path.exists(newpath):
                        os.makedirs(newpath)
##                    else:
##                        print("exist",newpath)
##                        break

                    time.sleep(1)

                    req2 = urllib.request.Request(link_page, headers = headers)
                    html2 = urllib.request.urlopen(req2).read()
                    soup2 = BeautifulSoup(html2,'html.parser')


                    image_tags = soup2.find_all('img')
                    len_tags = len(image_tags)
##                    print(len_tags)
                    temp_url = image_tags[-1].get('src')
                    print("yeet",temp_url)
                    print("file ext "+temp_url.split("/")[-1].split(".")[1])
                    fileExt = temp_url.split("/")[-1].split(".")[1]
                    
                    array2 =""
                    if " " in temp_url.split("/")[-2]:
                        temp_url2 = temp_url.split("/")[-2]
                        temp_url3=temp_url2.replace(" " ,"%20")
                        print("cheese", temp_url,temp_url2,temp_url3)
                        chap_temp = temp_url.split("/")[-1]
                        array = temp_url.split("/")
                        array[-2] = temp_url3
                        #print("arry 1" + array)
                        
                        array2 = '/'.join(array)
                        print(array2)
                            
                   
                    temp = image_name
                    image_name = str(image_name) + "." + fileExt
                    print("AAAAHH "+image_name)

                    last_image = str(len_tags-2) + "." + fileExt
                    
                    fullfilename = os.path.join(newpath,image_name)
##                    print("file" , fullfilename,image_name)

                    full_last_image = os.path.join(newpath,last_image)


                    if os.path.exists(full_last_image):
                        #print('here')
                        break
                    else:

                        if not os.path.exists(fullfilename):
                            print(image_tags[-1].get('src'))
                            #put array2 inplace of image_tags[-1].get('src') if breaking
                            req3 = urllib.request.Request(image_tags[-1].get('src'), headers={'User-Agent': 'Mozilla/5.0'})
                            with open(fullfilename, "wb") as f:
                                with urllib.request.urlopen(req3) as r:
                                    f.write(r.read())
                                    r.close()
                        else:
                            pass
                                            
                    image_name = temp
                    image_name += 1

        image_name = 1

        comic_link = []

if __name__ == "__main__":
    main()

