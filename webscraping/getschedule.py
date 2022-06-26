from requests_html import HTMLSession
import json

def get_schedule():
    url = "https://www.formula1.com/en/racing/2022.html"
    session = HTMLSession()
    r = session.get(url)
    try:
        r.html.render(sleep = 1)
    except:
        get_schedule()

    completed = r.html.find(".completed-events > div")
    current = r.html.find(".hero-event:not(.d-none)", first = True)
    upcoming = r.html.find(".event-below-hero > div")

    all_events = []
    for event in completed:
        round = event.find(".card-title", first = True)
        if(round == None):
            continue
        item = {}
        item["round"] = round.text
        item["start-date"] = event.find(".start-date", first = True).text
        item["end-date"] = event.find(".end-date", first = True).text
        item["title"] = event.find(".event-title", first = True).text
        item["place"] = event.find(".event-place", first = True).text
        month = event.find(".month-wrapper", first = True).text
        if("-" in month):
            item["start-month"] = month.split("-")[0]
            item["end-month"] = month.split("-")[1]
        else:
            item["start-month"] = month
            item["end-month"] = month
        all_events.append(item)

    round = current.find(".card-title", first = True)
    if(round != None):
        item = {}
        item["round"] = round.text
        item["start-date"] = current.find(".start-date", first = True).text
        item["end-date"] = current.find(".end-date", first = True).text
        item["title"] = current.find(".event-title", first = True).text
        item["place"] = current.find(".event-place", first = True).text
        month = current.find(".month-wrapper", first = True).text
        if("-" in month):
            item["start-month"] = month.split("-")[0]
            item["end-month"] = month.split("-")[1]
        else:
            item["start-month"] = month
            item["end-month"] = month
        all_events.append(item)
    
    for event in upcoming:
        round = event.find(".card-title", first = True)
        if(round == None):
            continue
        item = {}
        item["round"] = round.text
        item["start-date"] = event.find(".start-date", first = True).text
        item["end-date"] = event.find(".end-date", first = True).text
        item["title"] = event.find(".event-title", first = True).text
        item["place"] = event.find(".event-place", first = True).text
        month = event.find(".month-wrapper", first = True).text
        if("-" in month):
            item["start-month"] = month.split("-")[0]
            item["end-month"] = month.split("-")[1]
        else:
            item["start-month"] = month
            item["end-month"] = month
        all_events.append(item)

    with open("data\schedule.json", "w") as f:
        json.dump(all_events, f, indent = 2)
    
get_schedule()
