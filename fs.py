'''
This code will scrape the sidebar recommended videos from a saved
youtube page.  You will need to right click on the page you want to
scrape and choose "save as..." (take note of the full path name to
your file - you will need to enter it when you run the program).

The page is rendered via the Render Class from render_page.py.  
Video link, title, and thumbnail link will be output to a file
in csv format.
'''


from bs4 import BeautifulSoup
from PyQt4 import QtCore, QtGui, QtWebKit
from lxml import html
import sys


def write_to_csv(videos):
    ''' Write data to csv formatted file'''    
    
    outputfile = input("What do you want to call your data file?\n")
    print('Writing to "%s"...' % outputfile)
    csv = open(outputfile, "w")
        
    for video in videos:
        try:     
            row = '"' + video['mainvideo'] + '", ' \
                  '"' + video['title'] + '", ' \
                + '"' + video['href'] + '", ' \
                + '"' + video['thumbnail'] + '"\n'
            csv.write(row)
        except:
            print("invalid record")
    csv.close()
    
    print('Success!  File closed.')
    
def loadPage(url):
      page = QtWebKit.QWebPage()
      loop = QtCore.QEventLoop() # Create event loop
      page.mainFrame().loadFinished.connect(loop.quit) # Connect loadFinished to loop quit
      page.mainFrame().load(QtCore.QUrl(url))
      loop.exec_() # Run event loop, it will end on loadFinished
      return page.mainFrame().toHtml()


def get_page_results(url):

    videos = []
    page = loadPage(url)
    soup = BeautifulSoup(page, "lxml")
    main_vid = soup.find("h1", {"class":"title style-scope ytd-video-primary-info-renderer"})
    mainvideo = main_vid.text

    for rec_video in soup.find_all("a", {"class":"yt-simple-endpoint style-scope ytd-compact-video-renderer"}):
    
        rec_video = BeautifulSoup(str(rec_video), "lxml")
    
        link = rec_video.find('a')
        href = link.get('href')
        span = rec_video.find('span')
        title = span.get('title')
        thumbnail = 'https://i.ytimg.com/vi/' + href[-11:] + '/hqdefault.jpg' 
    
        videos.append({ 'mainvideo': mainvideo,
                                    'title': title,
                                    'href': href,
                                    'thumbnail': thumbnail })

    print("Found", len(videos), "videos.")
    return videos

app = QtGui.QApplication(sys.argv)

if __name__ == "__main__":
    
    # Your html filename should be in a format similar to:
    # file:///home/jason/workspace/youtubescrape/0.html
    # do not forget: the files must be named as 0.html, 1.html and so on
    #url = input("Enter the full path to your saved html file:\n") bye :)
    
    num = input("How many files do u have?\n")
    recommended_videos = []    

    for i in range(int(num)):
        url = "file:///home/daniel/ytscrape/videos/" + str(i) + ".html"
        print("url:", url)
        result = get_page_results(url)
        recommended_videos += result

        print("Found so far: ", len(recommended_videos), "videos.")
    
    write_to_csv(recommended_videos)

app.exit()
