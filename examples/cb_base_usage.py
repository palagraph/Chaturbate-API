from enum import Enum
from chaturbate_api import ChaturbateSearch, ChatrubateCam, Type, Tag
import re
import webbrowser

webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("C://Program Files (x86)//Google//Chrome//Application//chrome.exe"))
f = open('boys.html','wt', encoding="utf-8")

#pattern = re.compile("[Mm]edel|[Aa]ntioq")


if __name__ == '__main__':
    #MyTag = Enum('MyTag', {'CUSTOM': 'asian/'})

    cams = ChaturbateSearch().search(
        
        gender=Type.MALE,
        nr_pages=25
    ).filter_by(
        # age=lambda age: True if 18 <= age <= 30 else False,
        loc_string='[Mm]edel|[Aa]ntioq'
        # uptime_min=lambda uptime_min: True if 50 <= uptime_min <= 300 else False,
        # spectators=lambda spectators: True if 1 <= spectators <= 20 else False,
    )

    f.write('<html><head><meta http-equiv="refresh" content="60"><meta charset="UTF-8"></head><body>')
    f.write('<h1 align="center">Antioquia Boys</h1>')
    paragraph = '<p style="float: left; font-size: 12pt; text-align: center; width: 20%; margin-left: 2%; margin-bottom: 1em;">\n'

    if cams.filtered_results:
        for cam in cams.filtered_results:
            cam: ChatrubateCam
            #webbrowser.get('chrome').open(cam.url)
            #print(
            #   cam.gender.name.title(),
            #   cam.age,
            #    cam.url,
            #    'location:"{}" img:"{}"'.format(cam.location, cam.imgsrc)
            #)
            f.write(paragraph)
            boy = ('<a href="' + cam.url + '"><img src="' + cam.imgsrc + '" style="width:100%"></a>' +
                '<b>' + cam.url.split('/')[3].upper().replace('_',' ') + ('&nbsp;&nbsp;' + str(cam.age) if (cam.age>0) else '') + '</b><br>' + cam.location + ' <b>'  +
                str(cam.spectators) + '</b></p>\n')
            f.write(boy)

                  
    else:
        print('No Results')
    f.write('</body></html>')
    f.close()
    
