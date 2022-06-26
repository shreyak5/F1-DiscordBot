from requests_html import AsyncHTMLSession
import discord

async def full_schedule(url):

    session = AsyncHTMLSession()
    r = await session.get(url)
    try:
        await r.html.arender(sleep = 1)
    except:
        await full_schedule(url)

    schedule = []
    events = r.html.find(".f1-race-hub--timetable-listings > div")

    for event in events:
        item = {}
        item["title"] = event.find(".f1-timetable--title", first = True).text
        item["date"] = (event.find(".f1-timetable--day", first = True).text) + " " + (event.find(".f1-timetable--month", first = True).text)
        item["time"] = (event.find(".start-time", first = True).text) + "-" + (event.find(".end-time", first = True).text)
        schedule.append(item)
    
    return schedule

async def next_race():
    
    main_page = "https://www.formula1.com/en/racing/2022.html"
    session = AsyncHTMLSession()

    r = await session.get(main_page)
    try:
        await r.html.arender(sleep = 1)
    except:
        await next_race()

    race = ""

    hero_event = r.html.find(".hero-event:not(.d-none)", first = True)
    race_status = (hero_event.find("span", first = True)).text

    if("NEXT" in race_status.upper()):
        race = hero_event
    else:
        race = r.html.find(".event-below-hero > div", first = True)

    title = race.find(".event-title", first = True).text
    place = race.find(".event-place", first = True).text
    img_url = race.find(".event-image img", first = True).attrs['data-src']

    event_page = list(race.absolute_links)[0]

    schedule = await full_schedule(event_page)

    nextrace_embed = discord.Embed(
        colour = discord.Color.dark_red(),
        title = title + " - " + place
    )

    f1_logo = "https://i.ibb.co/QXL69Nq/logo.png"
    nextrace_embed.set_author(name = "Next race", icon_url = f1_logo)
    nextrace_embed.set_image(url = img_url)
    for event in schedule[::-1]:
        nextrace_embed.add_field(name = event["title"] + ": " + event["date"], value = event["time"], inline = True)

    return nextrace_embed
