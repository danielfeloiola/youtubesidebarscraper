from advanced_link_crawler import download
from bs4 import BeautifulSoup

def fetch_youtube_url(watch_id):
    if watch_id == "": watch_id = '0uUoqD8a0V4'
    url = "https://www.youtube.com/watch?v=" + watch_id
    return download(url)

if __name__ == "__main__":
    #watch_id = input('video watch id: ')
    page = fetch_youtube_url('')
    #page = fetch_youtube_url(watch_id)
    
    soup = BeautifulSoup(page, "html.parser")
    '''
    ytd = soup.find_all('ytd-app')
    print('ytd-app:', len(ytd))

    recommended_vids = soup.find_all("div", \
        id_ = "dismissable", \
    #    class_="ytd-compact-video-renderer" \
    )
    print(type(recommended_vids))

    print(len(recommended_vids))
    for video in recommended_vids:
        print(video)
    
    thumbnails = soup.find_all("img") #, \
        #class_ = "style-scope yt-img-shadow")
    print(len(thumbnails))
    for tnail in thumbnails:
        print(tnail.get('src'))
    '''
    print(soup.prettify())
