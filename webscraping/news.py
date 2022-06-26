from requests_html import AsyncHTMLSession
import datetime

async def update_list(ctx):
    session = AsyncHTMLSession()
    url = "https://news.google.com/search?q=f1&hl=en-IN&gl=IN&ceid=IN%3Aen"

    r = await session.get(url)
    try:
        await r.html.arender(sleep = 1, scrolldown = 0, timeout = 8)
    except:
        await update_list(ctx)

    articles = r.html.find("div div article")
    data =[]
    for article in articles:
        empty = {}
        h3 = article.find("h3", first = True)
        time = article.find("div div time", first = True)
        if(time ==  None):
            continue
        if(h3 == None):
            continue
        # filtering out old headlines
        if("days ago" in time.text):
            continue
        empty["headline"] = h3.text
        empty["link"] = list(h3.absolute_links)[0]
        data.append(empty)
    
    return data

async def latest_news(ctx, update_hour, newslist):
    current_hour = datetime.datetime.now().hour

    message = None
    if(current_hour == update_hour):
        update_hour = (current_hour + 2) % 24
        newslist.clear()
        message = await ctx.send("```Fetching latest F1 news...```")
        newslist = await update_list(ctx)
    
    if(len(newslist) == 0):
        update_hour = (current_hour + 2) % 24
        message = await ctx.send("```Fetching latest F1 news...```")
        newslist = await update_list(ctx)
        
    return update_hour, newslist, message
