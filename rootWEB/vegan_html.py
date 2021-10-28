# csv 열기
import pandas as pd
import folium
import numpy as np

#불러올 csv파일
from folium import LayerControl
from folium import plugins
from folium.plugins import Search
from requests import head

df1 = pd.read_csv('veganfood_fin.csv' , encoding = 'UTF-8')
print(df1.columns)

#맵 설정
s_map = folium.Map(location=[df1['위도 '].mean(), df1['경도'].mean()], zoom_start=12)

#그룹화
fg = folium.FeatureGroup(name = 'WWG')
s_map.add_child(fg)

group_0 = plugins.FeatureGroupSubGroup(fg, 'Total Place')
s_map.add_child(group_0)

# total place 출력
for n in df1.index :
 #팝업에 들어갈 텍스트를 지정해줍니다.
    popup_1 = df1['상호명'][n]
    popup_2 = df1['업종'][n]
    popup_3 = df1['전화번호'][n]
    popup_4 = df1['소재지'][n]

    if df1['업종'][n] == '한식' :
        icon_color = 'blue'
        popup = folium.Popup("업종" + '   -    ' + str(popup_2) + '<br>'
                             + "전화번호" + '   -    ' + str(popup_3) + '<br>'
                             + "소재지" + '<br>'
                             + str(popup_4), min_width=200, max_width=500)
        folium.Marker([df1['위도 '][n], df1['경도'][n]],
                      popup=popup,
                      tooltip=popup_1,
                      icon=folium.Icon(icon='thumbs-up', color=icon_color)).add_to(group_0)

    elif df1['업종'][n] == '양식' :
        icon_color = 'green'
        popup = folium.Popup("업종" + '   -    ' + str(popup_2) + '<br>'
                             + "전화번호" + '   -    ' + str(popup_3) + '<br>'
                             + "소재지" + '<br>'
                             + str(popup_4), min_width=200, max_width=500)
        folium.Marker([df1['위도 '][n], df1['경도'][n]],
                      popup=popup,
                      tooltip=popup_1,
                      icon=folium.Icon(icon='leaf', color=icon_color)).add_to(group_0)

    elif df1['업종'][n] == '중식' :
        icon_color = 'pink'
        popup = folium.Popup("업종" + '   -    ' + str(popup_2) + '<br>'
                             + "전화번호" + '   -    ' + str(popup_3) + '<br>'
                             + "소재지" + '<br>'
                             + str(popup_4), min_width=200, max_width=500)
        folium.Marker([df1['위도 '][n], df1['경도'][n]],
                      popup=popup,
                      tooltip=popup_1,
                      icon=folium.Icon(icon='shopping-cart', color=icon_color)).add_to(group_0)
    else :
        icon_color = 'beige'
        popup = folium.Popup("업종" + '   -    ' + str(popup_2) + '<br>'
                             + "전화번호" + '   -    ' + str(popup_3) + '<br>'
                             + "소재지" + '<br>'
                             + str(popup_4), min_width=200, max_width=500)
        folium.Marker([df1['위도 '][n], df1['경도'][n]],
                      popup=popup,
                      tooltip=popup_1,
                      icon=folium.Icon(icon='play', color=icon_color)).add_to(group_0)


folium.LayerControl(collapsed=False).add_to(s_map)
folium.Popup(min_width=500, max_width=500).add_to(s_map)

#저장할 html
s_map.save('./seoul.html')

# add
# https://stackoverflow.com/questions/55936595/how-can-i-highlight-multiple-search-results-in-python-folium-leaflet
# https://suho413.tistory.com/entry/Folium-API-%ED%99%9C%EC%9A%A9%EA%B7%B8%EB%A3%B9-%EC%84%A4%EC%A0%95-%EB%A7%88%ED%81%AC-%EC%BB%A4%EC%8A%A4%ED%85%80-%EC%84%9C%ED%81%B4-%EB%A7%88%EC%BB%A4-html-%EC%A0%80%EC%9E%A5
# https://dailyheumsi.tistory.com/85
# https://stackoverflow.com/questions/63152298/updating-folium-changed-the-popup-box-width