#https://detail.tmall.hk/hk/item.htm?id=592801855548&spm=a211oj.20767644/ssrn.5673248570.d_tab1_item1.117841a8I3Ho5f&scm=1007.12144.81309.12722998_0_0&pvid=f9f984b6-b534-45b3-ab60-d6d18e96a4be&utparam=%7B%22x_hestia_source%22:%22gul_pc%22,%22x_object_type%22:%22item%22,%22x_hestia_subsource%22:%22gul_221696%22,%22x_mt%22:0,%22x_src%22:%22gul_pc%22,%22x_pos%22:1,%22wh_pid%22:221696,%22x_pvid%22:%22f9f984b6-b534-45b3-ab60-d6d18e96a4be%22,%22scm%22:%221007.12144.81309.12722998_0_0%22,%22x_object_id%22:592801855548,%22tpp_buckets%22:%222144
#这个商品的评论内容
import requests
import re
import time
#保存数据
import pandas as pd
headers={
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36',
    'referer':'https://detail.tmall.hk/hk/item.htm?id=592801855548&spm=a211oj.20767644/ssrn.5673248570.d_tab1_item1.117841a8I3Ho5f&scm=1007.12144.81309.12722998_0_0&pvid=f9f984b6-b534-45b3-ab60-d6d18e96a4be&utparam=%7B%22x_hestia_source%22:%22gul_pc%22,%22x_object_type%22:%22item%22,%22x_hestia_subsource%22:%22gul_221696%22,%22x_mt%22:0,%22x_src%22:%22gul_pc%22,%22x_pos%22:1,%22wh_pid%22:221696,%22x_pvid%22:%22f9f984b6-b534-45b3-ab60-d6d18e96a4be%22,%22scm%22:%221007.12144.81309.12722998_0_0%22,%22x_object_id%22:592801855548,%22tpp_buckets%22:%222144',
    #记得用自己的cookie去爬，最好延时时间越长越好，因为爬的快了会封ip
    'cookie':'cna=sn8pGPljhTkCAWcrwF7ZpNhi; xlly_s=1; login=true; cookie2=19a021f7cd7a042b90dc13c49bd522d9; t=0f788266c03bfc19209fff381344a62c; _tb_token_=ee3eebb83babb; _m_h5_tk=395cbf8d1758482da0d5481fe86e3e92_1604659560022; _m_h5_tk_enc=83f1c7c092b6f082b5af4876835338f6; dnk=%5Cu7B1B%5Cu54E5wudi1205692955; uc1=existShop=false&cookie16=VT5L2FSpNgq6fDudInPRgavC%2BQ%3D%3D&pas=0&cookie14=Uoe0abRp%2BNkh7Q%3D%3D&cookie15=VT5L2FSpMGV7TQ%3D%3D&cookie21=WqG3DMC9Fb5mPLIQo9kR; uc3=id2=UUGq2QCLsBBMLg%3D%3D&vt3=F8dCufOGCvLrV96eAQI%3D&nk2=1p5O%2FF0swbAE8zhT4OaT04Gl&lg2=VT5L2FSpMGV7TQ%3D%3D; tracknick=%5Cu7B1B%5Cu54E5wudi1205692955; lid=%E7%AC%9B%E5%93%A5wudi1205692955; uc4=id4=0%40U2OdLQ3GfM3cc1vcJ42wnUb5La95&nk4=0%401C9mHOrX55%2FjNxwvJhLdBL2oXyNdp0jC1enYYA0%3D; _l_g_=Ug%3D%3D; unb=2988158160; lgc=%5Cu7B1B%5Cu54E5wudi1205692955; cookie1=B0E3JfOkAyZQf48jClVyq31E5B4zrJWjK2QFOKSgurc%3D; cookie17=UUGq2QCLsBBMLg%3D%3D; _nk_=%5Cu7B1B%5Cu54E5wudi1205692955; sgcookie=E100c0VbSCMjivQ%2FdVcOznJm3ne00CZ%2FibMjICX%2F6hlTkmRrSwIT6q1367tlHz10HAp9GDxf6DeMwwY4QuT6oHbvYA%3D%3D; sg=505; csg=594738b2; enc=jy%2F%2F%2BchU%2BotYBcMnUgCvc2sXETOGYd3wmCloqxARsiVgjgoHzfGi5TRlw4mpux4r%2Boc10jShp89tU0Ay%2BqsLfg%3D%3D'
}
texts=[]
for n in range(1,33):
    url = 'https://rate.tmall.com/list_detail_rate.htm?itemId=592801855548&spuId=0&sellerId=2200657724895&order=3&currentPage='+str(n)+'&append=0&content=1&tagId=&posi=&picture=&groupId=&ua=098%23E1hvSpv8vWyvUvCkvvvvvjiWP2FO6j1bPFMUljivPmPZljYRnLzyQjYVRFc9tjDWdvhvmpvCI8osvvm2bL9CvvpvvhCv29hvCvvvMMGvvpvVvUCvpvvvmvhvLvvKV1%2BaA464d3ODN%2BFWdigqrADn9Wv7%2Bu6XwAq6D46X58t%2Bm7zU58TJ%2B3%2BI1jZ7%2Bu0OwkM6D40Xeut%2Bm7zhVuTJ%2B3%2BIsjZ7%2Bu6wjomgvpvIvvCvpvvvvvvvvhnCvvvC4pvvByOvvUhQvvCVB9vv9BQvvhXVvvmCj89Cvv9vvhh6wrZpJI9CvvOCvhE2gWAevpvhvvCCBUOCvvpv9hCv&needFold=0&_ksTS=1604647728169_1125&callback=jsonp1126'
    data = requests.get(url, headers=headers).text
    #设置延时，怕发现是爬虫，不容易触发反爬
    time.sleep(30)
    #请求
    data = requests.get(url, headers=headers).text
    #正则提取
    pat = re.compile('"rateContent":"(.*?)","fromMall"')
    # 按匹配规则找出评论来
    #extend函数是合并，findall匹配后的数据
    texts.extend(pat.findall(data))
    print('爬完了第'+str(n)+'页')
    print(pat.findall(data))
# print(texts)
#创建一个空的数据表
df=pd.DataFrame()
#标题评论
df['评论']=texts
#保存成excel格式
df.to_excel('韩国吕氏洗发水.xlsx')
print(df)
