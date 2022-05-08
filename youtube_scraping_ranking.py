from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import pandas as pd
import chromedriver_binary
from time import sleep
import random


def get_youtube_trending(url,output_latest,output_music,output_game,output_film):
    options=Options()
    options.add_argument('--incognito') #シークレットモードでChromeを開く

    driver=webdriver.Chrome(options=options)
    driver.get(url)
    driver.implicitly_wait(10)
    
    #最新、音楽、ゲーム、映画それぞれの表形式になっているデータを格納するリスト
    Data_Flame=[]
    
    for i in range(4):
        #急上昇の中で、最新、音楽、ゲーム、映画それぞれのxpathを取得
        xpath='//*[@id="tabsContent"]/tp-yt-paper-tab[{}]'.format(i+1)
        driver.find_element(By.XPATH,xpath).click()
        
        sleep(random.randint(1,10))
        
        ranking_videos=driver.find_elements(By.ID,'video-title')
        
        titles=[]
        urls=[]
        
        for ranking_video in ranking_videos:
            titles.append(ranking_video.text)
            urls.append(ranking_video.get_attribute('href'))
            
            if len(titles)==5:
                break
        
        #取得したデータを表形式にして整理する
        df=pd.DataFrame()
    
        
        df['trending_rank']=range(1,6)
        df['title']=titles
        df['url']=urls
        
        Data_Flame.append(df)
        
    
    #データをcsvで出力
    File_Name=[output_latest,output_music,output_game,output_film]
    for i,j in enumerate(File_Name):
        Data_Flame[i].to_csv(j,encoding='utf-8-sig',index=False)
        
    
    driver.quit()
    

if __name__=='__main__':
    url='https://www.youtube.com/feed/trending'
    
    output_latest='youtube_trending_latest.csv'
    output_music='youtube_trending_music.csv'  
    output_game='youtube_trendnig_game.csv'
    output_film='youtube_trending_film.csv'
    
    get_youtube_trending(url,output_latest,output_music,output_game,output_film)
    
        
        
        
    
    

