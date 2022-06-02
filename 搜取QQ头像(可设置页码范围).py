import requests, bs4
def judge(num):
    list_web = ["qinglv", "nan", "nv", "katong", "fengjing", "weixin"]
    if num == 1:
        return(f"https://www.woyaogexing.com/touxiang/{list_web[0]}/hot/index.html")
    if num == 2:
        return(f"https://www.woyaogexing.com/touxiang/{list_web[1]}/hot/index.html")
    if num == 3:
        return(f"https://www.woyaogexing.com/touxiang/{list_web[2]}/hot/index.html")
    if num == 4:
        return(f"https://www.woyaogexing.com/touxiang/{list_web[3]}/hot/index.html")
    if num == 5:
        return(f"https://www.woyaogexing.com/touxiang/{list_web[4]}/hot/index.html")
    if num == 6:
        return(f"https://www.woyaogexing.com/touxiang/{list_web[5]}/hot/index.html")
def resp(url,headers):
    # requests获取主页面源代码的数据
    url_resp = requests.get(url, headers=headers)
    url_resp.encoding = "utf-8"
    # 解析源代码
    main_page = bs4.BeautifulSoup(url_resp.text, "html.parser")
    main_as = main_page.find_all("a", class_="img")
    for main_a in main_as:
        main_a_get = main_a.get("href")  # 获取属性href中的值
        href = f"https://www.woyaogexing.com{main_a_get}"  # 获取子页面的网址
        # requests获取子页面源代码的数据
        href_resp = requests.get(href, headers=headers)
        href_resp.encoding = "utf-8"
        # 解析源代码
        href_page = bs4.BeautifulSoup(href_resp.text, "html.parser")
        href_page_imgs = href_page.find_all("img", class_="lazy")
        for href_page_img in href_page_imgs:
            img_src = href_page_img.get("src")
            img_url = f"http:{img_src}"
            img_url_resp = requests.get(img_url, headers=headers)
            img_name = img_url.split("/")[-1]
            print(img_name, " 已完成！")
            with open("img/" + img_name, mode="wb") as f:
                f.write(img_url_resp.content)
            img_url_resp.close()
def judge_page(num,i):
    list_web = ["qinglv", "nan", "nv", "katong", "fengjing", "weixin"]
    if num == 1:
        return(f"https://www.woyaogexing.com/touxiang/{list_web[0]}/hot/index_{i}.html")
    if num == 2:
        return(f"https://www.woyaogexing.com/touxiang/{list_web[1]}/hot/index_{i}.html")
    if num == 3:
        return(f"https://www.woyaogexing.com/touxiang/{list_web[2]}/hot/index_{i}.html")
    if num == 4:
        return(f"https://www.woyaogexing.com/touxiang/{list_web[3]}/hot/index_{i}.html")
    if num == 5:
        return(f"https://www.woyaogexing.com/touxiang/{list_web[4]}/hot/index_{i}.html")
    if num == 6:
        return(f"https://www.woyaogexing.com/touxiang/{list_web[5]}/hot/index_{i}.html")
print("请一次只能输入一个编号!")
str_ = input("请输入你查询的头像种类的编号(1.情侣、2.男生、3.女生、4.卡通动漫、5.风景静物、6.微信):")
page = input('请输入你搜索的页码:')
num_page = int(page)
num_ = int(str_)
i = 0
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0"
}
url = judge(num_)
if i == 0:
    print(f"=====================正在抓取第{i + 1}页=====================")
    url = judge(num_)
    resp(url,headers)
    print(f"=====================第{i+1}页已完成！！=====================")
for i in range(2,num_page+1):
    if i < (num_page+1) :
        print(f"=====================正在抓取第{i}页=====================")
        url = judge_page(num_,i)
        resp(url,headers)
        print(f"=====================第{i}页已完成！！=====================")

print("已全部完成！并且创建好“img”名称的文件夹，请查看(^_^)!！")