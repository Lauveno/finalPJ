import chardet
import numpy as np
import pandas as pd
from django.http import JsonResponse , HttpResponse
from django.shortcuts import render, redirect
from .models import *

# Login에 이용되는 Module
import csv
from django.contrib.auth.hashers import make_password, check_password #비밀번호 암호화 / 패스워드 체크(db에있는거와 일치성확인)

# Create your views here.

# wwg_place_df = pd.read_csv('wwg_place.csv' , encoding='UTF-8')
# wwg_place_df = wwg_place_df.replace(np.NaN , 0)

zerowaste_df = pd.read_csv('zerowaste_fin_utf8.txt', encoding='UTF-8')
zerowaste_df = zerowaste_df.replace(np.NaN , 0)

vegan_df = pd.read_csv('veganfood_fin.csv', encoding='UTF-8')
vegan_df = vegan_df.replace(np.NaN , 0)

# About page - main page
#[TEST] 로그인 할경우 UserID 뽑아보기
def about(request) :
    print('mapApp about index ~ ')
    myuser = request.session.get('user')
    if myuser:
        user = WwgUser.objects.get(user_id=myuser)
        return render(request, 'map/about.html', {'user_id': user})
    return render(request, 'map/about.html')


# Map page - 완료
# main map
def map(request) :
    print('mapApp map index ~ ')
    return render(request , 'map/map.html')

# zerowaste map
def map_zerowaste(request) :
    print('mapApp map_zerowaste index ~ ')
    return render(request , 'map/map_zerowaste.html')

# vegan map
def map_vegan(request) :
    print('mapApp map_vegan index ~ ')
    return render(request , 'map/map_vegan.html')


# data path
# total data -> 추천 장소 들어갈 예정
def wwg_place_data(request) :
    print('mapApp wwg place index ~ ')
#     wwg_place_df.rename(columns={'설명(판매메뉴)': '설명'}, inplace=True)
#     wwg_place_df.rename(columns={'위도 ' : '위도'}, inplace=True)
#     print(wwg_place_df.columns)
#
#     wwg_placeList = []
#     for idx in wwg_place_df.index :
#         wwg_placeList.append({
#             'id': (wwg_place_df.iloc[idx, :].번호).tolist(),  # numpy
#             'name': wwg_place_df.iloc[idx, :].상호명,
#             'number': wwg_place_df.iloc[idx, :].전화번호,
#             'address': wwg_place_df.iloc[idx, :].소재지,
#             'category': wwg_place_df.iloc[idx, :].업종,
#             'about': wwg_place_df.iloc[idx, :].설명,
#             'imgURL': wwg_place_df.iloc[idx, :].imgURl,
#             'img': wwg_place_df.iloc[idx, :].jpg,
#             'lat': (wwg_place_df.iloc[idx, :].위도 ).tolist(),  # numpy
#             'lng': (wwg_place_df.iloc[idx, :].경도).tolist()  # numpy
#         })
#         # print(wwg_placeList[{'id' : '1' , 'name' : 'asdf'}])
#         print('wwg_placeList complete!!')
#         print(wwg_placeList[0])
#
#         return JsonResponse(wwg_placeList, safe=False)


# zerowaste data - 완료
# 전체
def zerowaste_data_all(request) :
    print('mapApp zerowaste all index ~')
    # print(zerowaste_df.head(5))
    # print(zerowaste_df['상호명'])

    zerowasteList = []
    for idx in zerowaste_df.index :
        zerowasteList.append({
            'id' : (zerowaste_df.iloc[idx ,  : ].번호).tolist() , # numpy
            'name' : zerowaste_df.iloc[idx ,  : ].상호명 ,
            'number' : zerowaste_df.iloc[idx ,  : ].전화번호 ,
            'address' : zerowaste_df.iloc[idx ,  : ].소재지 ,
            'category' : zerowaste_df.iloc[idx ,  : ].업종 ,
            'about' : zerowaste_df.iloc[idx ,  : ].설명 ,
            'imgURL' : zerowaste_df.iloc[idx ,  : ].imgUrl ,
            'img' : zerowaste_df.iloc[idx ,  : ].jpg ,
            'lat' : (zerowaste_df.iloc[idx ,  : ].위도).tolist() , # numpy
            'lng' : (zerowaste_df.iloc[idx ,  : ].경도).tolist() # numpy
        })
    # print(zerowasteList[{'id' : '1' , 'name' : 'asdf'}])
    print('zerowasteList all complete!!')
    print(zerowasteList[0])

    return JsonResponse(zerowasteList, safe=False)

# 제로웨이스트
def zerowaste_data(request) :
    print('mapApp zerowaste index ~')
    # print(zerowaste_df.head(5))
    # print(zerowaste_df['상호명'])
    print(zerowaste_df.iloc[ : , 4])

    zerowasteList = []
    for idx in zerowaste_df.index :
        if zerowaste_df.iloc[idx , 4] == '제로웨이스트샵' or zerowaste_df.iloc[idx , 4] == '리필샵 , 제로웨이스트샵':
            zerowasteList.append({
                'id' : (zerowaste_df.iloc[idx ,  : ].번호).tolist() , # numpy
                'name' : zerowaste_df.iloc[idx ,  : ].상호명 ,
                'number' : zerowaste_df.iloc[idx ,  : ].전화번호 ,
                'address' : zerowaste_df.iloc[idx ,  : ].소재지 ,
                'category' : zerowaste_df.iloc[idx ,  : ].업종 ,
                'about' : zerowaste_df.iloc[idx ,  : ].설명 ,
                'imgURL' : zerowaste_df.iloc[idx ,  : ].imgUrl ,
                'img' : zerowaste_df.iloc[idx ,  : ].jpg ,
                'lat' : (zerowaste_df.iloc[idx ,  : ].위도).tolist() , # numpy
                'lng' : (zerowaste_df.iloc[idx ,  : ].경도).tolist() # numpy
            })
    # print(zerowasteList[{'id' : '1' , 'name' : 'asdf'}])
    print('zerowasteList complete!!')
    print(zerowasteList)

    return JsonResponse(zerowasteList, safe=False)

# 리필샵
def zerowaste_data_refill(request) :
    print('mapApp zerowaste refill index ~')
    # print(zerowaste_df.head(5))
    # print(zerowaste_df['상호명'])

    zerowasteList = []
    for idx in zerowaste_df.index :
        if zerowaste_df.iloc[idx , 4] == '리필샵' or zerowaste_df.iloc[idx , 4] == '리필샵 , 제로웨이스트샵':
            zerowasteList.append({
                'id' : (zerowaste_df.iloc[idx ,  : ].번호).tolist() , # numpy
                'name' : zerowaste_df.iloc[idx ,  : ].상호명 ,
                'number' : zerowaste_df.iloc[idx ,  : ].전화번호 ,
                'address' : zerowaste_df.iloc[idx ,  : ].소재지 ,
                'category' : zerowaste_df.iloc[idx ,  : ].업종 ,
                'about' : zerowaste_df.iloc[idx ,  : ].설명 ,
                'imgURL' : zerowaste_df.iloc[idx ,  : ].imgUrl ,
                'img' : zerowaste_df.iloc[idx ,  : ].jpg ,
                'lat' : (zerowaste_df.iloc[idx ,  : ].위도).tolist() , # numpy
                'lng' : (zerowaste_df.iloc[idx ,  : ].경도).tolist() # numpy
            })
    # print(zerowasteList[{'id' : '1' , 'name' : 'asdf'}])
    print('zerowasteList refill complete!!')
    print(zerowasteList[0])

    return JsonResponse(zerowasteList, safe=False)

# 다회용기
def zerowaste_data_recycle(request) :
    print('mapApp zerowaste recycle index ~')
    # print(zerowaste_df.head(5))
    # print(zerowaste_df['상호명'])

    zerowasteList = []
    for idx in zerowaste_df.index :
        if zerowaste_df.iloc[idx , 4] == '다회용기' :
            zerowasteList.append({
                'id' : (zerowaste_df.iloc[idx ,  : ].번호).tolist() , # numpy
                'name' : zerowaste_df.iloc[idx ,  : ].상호명 ,
                'number' : zerowaste_df.iloc[idx ,  : ].전화번호 ,
                'address' : zerowaste_df.iloc[idx ,  : ].소재지 ,
                'category' : zerowaste_df.iloc[idx ,  : ].업종 ,
                'about' : zerowaste_df.iloc[idx ,  : ].설명 ,
                'imgURL' : zerowaste_df.iloc[idx ,  : ].imgUrl ,
                'img' : zerowaste_df.iloc[idx ,  : ].jpg ,
                'lat' : (zerowaste_df.iloc[idx ,  : ].위도).tolist() , # numpy
                'lng' : (zerowaste_df.iloc[idx ,  : ].경도).tolist() # numpy
            })
    # print(zerowasteList[{'id' : '1' , 'name' : 'asdf'}])
    print('zerowasteList recycle complete!!')
    print(zerowasteList[0])

    return JsonResponse(zerowasteList, safe=False)

# 기타
def zerowaste_data_etc(request) :
    print('mapApp zerowaste etc index ~')
    # print(zerowaste_df.head(5))
    # print(zerowaste_df['상호명'])

    zerowasteList = []
    for idx in zerowaste_df.index :
        if zerowaste_df.iloc[idx , 4] == '기타' or zerowaste_df.iloc[idx , 4] == 0 :
            zerowasteList.append({
                'id' : (zerowaste_df.iloc[idx ,  : ].번호).tolist() , # numpy
                'name' : zerowaste_df.iloc[idx ,  : ].상호명 ,
                'number' : zerowaste_df.iloc[idx ,  : ].전화번호 ,
                'address' : zerowaste_df.iloc[idx ,  : ].소재지 ,
                'category' : zerowaste_df.iloc[idx ,  : ].업종 ,
                'about' : zerowaste_df.iloc[idx ,  : ].설명 ,
                'imgURL' : zerowaste_df.iloc[idx ,  : ].imgUrl ,
                'img' : zerowaste_df.iloc[idx ,  : ].jpg ,
                'lat' : (zerowaste_df.iloc[idx ,  : ].위도).tolist() , # numpy
                'lng' : (zerowaste_df.iloc[idx ,  : ].경도).tolist() # numpy
            })
    # print(zerowasteList[{'id' : '1' , 'name' : 'asdf'}])
    print('zerowasteList etc complete!!')
    print(zerowasteList[0])

    return JsonResponse(zerowasteList, safe=False)


# vegan data - 완료
# 전체
def vegan_data_all(request) :
    print('mapApp vegan index ~')
    # print(vegan_df.head(5))

    veganList = []
    for idx in vegan_df.index:
        veganList.append({
            'id': (vegan_df.iloc[idx, :].번호).tolist(),  # numpy
            'name': vegan_df.iloc[idx, :].상호명,
            'number': vegan_df.iloc[idx, :].전화번호,
            'address': vegan_df.iloc[idx, :].소재지,
            'category': vegan_df.iloc[idx, :].업종,
            'about': vegan_df.iloc[idx, :].설명,
            'imgURL': vegan_df.iloc[idx, :].imgURl,
            'img': vegan_df.iloc[idx, :].jpg,
            'lat': (vegan_df.iloc[idx, :].위도).tolist(),  # numpy
            'lng': (vegan_df.iloc[idx, :].경도).tolist()  # numpy
        })
    # print(zerowasteList[{'id' : '1' , 'name' : 'asdf'}])
    print('veganList all complete!!')
    # print(veganList[0])

    return JsonResponse(veganList, safe=False)

# 한식
def vegan_data_kor(request) :
    print('mapApp vegan kor index ~')
    print(vegan_df.iloc[ : , 7])

    veganList = []
    for idx in vegan_df.index:
        if vegan_df.iloc[idx , 7] == '한식' :
            veganList.append({
                'id': (vegan_df.iloc[idx, :].번호).tolist(),  # numpy
                'name': vegan_df.iloc[idx, :].상호명,
                'number': vegan_df.iloc[idx, :].전화번호,
                'address': vegan_df.iloc[idx, :].소재지,
                'category': vegan_df.iloc[idx, :].업종,
                'about': vegan_df.iloc[idx, :].설명,
                'imgURL': vegan_df.iloc[idx, :].imgURl,
                'img': vegan_df.iloc[idx, :].jpg,
                'lat': (vegan_df.iloc[idx, :].위도).tolist(),  # numpy
                'lng': (vegan_df.iloc[idx, :].경도).tolist()  # numpy
            })
    # print(zerowasteList[{'id' : '1' , 'name' : 'asdf'}])
    print('veganList all complete!!')
    # print(veganList[0])

    return JsonResponse(veganList, safe=False)

# 양식
def vegan_data_wes(request) :
    print('mapApp vegan wes index ~')

    veganList = []
    for idx in vegan_df.index:
        if vegan_df.iloc[idx, 7] == '양식':
            veganList.append({
                'id': (vegan_df.iloc[idx, :].번호).tolist(),  # numpy
                'name': vegan_df.iloc[idx, :].상호명,
                'number': vegan_df.iloc[idx, :].전화번호,
                'address': vegan_df.iloc[idx, :].소재지,
                'category': vegan_df.iloc[idx, :].업종,
                'about': vegan_df.iloc[idx, :].설명,
                'imgURL': vegan_df.iloc[idx, :].imgURl,
                'img': vegan_df.iloc[idx, :].jpg,
                'lat': (vegan_df.iloc[idx, :].위도).tolist(),  # numpy
                'lng': (vegan_df.iloc[idx, :].경도).tolist()  # numpy
            })
    # print(zerowasteList[{'id' : '1' , 'name' : 'asdf'}])
    print('veganList all complete!!')
    # print(veganList[0])

    return JsonResponse(veganList, safe=False)

# 중식
def vegan_data_chi(request) :
    print('mapApp vegan chi index ~')

    veganList = []
    for idx in vegan_df.index:
        if vegan_df.iloc[idx, 7] == '중식':
            veganList.append({
                'id': (vegan_df.iloc[idx, :].번호).tolist(),  # numpy
                'name': vegan_df.iloc[idx, :].상호명,
                'number': vegan_df.iloc[idx, :].전화번호,
                'address': vegan_df.iloc[idx, :].소재지,
                'category': vegan_df.iloc[idx, :].업종,
                'about': vegan_df.iloc[idx, :].설명,
                'imgURL': vegan_df.iloc[idx, :].imgURl,
                'img': vegan_df.iloc[idx, :].jpg,
                'lat': (vegan_df.iloc[idx, :].위도).tolist(),  # numpy
                'lng': (vegan_df.iloc[idx, :].경도).tolist()  # numpy
            })
    # print(zerowasteList[{'id' : '1' , 'name' : 'asdf'}])
    print('veganList all complete!!')
    # print(veganList[0])

    return JsonResponse(veganList, safe=False)

# 일식
def vegan_data_jap(request) :
    print('mapApp vegan jap index ~')

    veganList = []
    for idx in vegan_df.index:
        if vegan_df.iloc[idx, 7] == '일식':
            veganList.append({
                'id': (vegan_df.iloc[idx, :].번호).tolist(),  # numpy
                'name': vegan_df.iloc[idx, :].상호명,
                'number': vegan_df.iloc[idx, :].전화번호,
                'address': vegan_df.iloc[idx, :].소재지,
                'category': vegan_df.iloc[idx, :].업종,
                'about': vegan_df.iloc[idx, :].설명,
                'imgURL': vegan_df.iloc[idx, :].imgURl,
                'img': vegan_df.iloc[idx, :].jpg,
                'lat': (vegan_df.iloc[idx, :].위도).tolist(),  # numpy
                'lng': (vegan_df.iloc[idx, :].경도).tolist()  # numpy
            })
    # print(zerowasteList[{'id' : '1' , 'name' : 'asdf'}])
    print('veganList all complete!!')
    # print(veganList[0])

    return JsonResponse(veganList, safe=False)

# 카페
def vegan_data_cafe(request) :
    print('mapApp vegan cafe index ~')

    veganList = []
    for idx in vegan_df.index:
        if vegan_df.iloc[idx, 7] == '카페':
            veganList.append({
                'id': (vegan_df.iloc[idx, :].번호).tolist(),  # numpy
                'name': vegan_df.iloc[idx, :].상호명,
                'number': vegan_df.iloc[idx, :].전화번호,
                'address': vegan_df.iloc[idx, :].소재지,
                'category': vegan_df.iloc[idx, :].업종,
                'about': vegan_df.iloc[idx, :].설명,
                'imgURL': vegan_df.iloc[idx, :].imgURl,
                'img': vegan_df.iloc[idx, :].jpg,
                'lat': (vegan_df.iloc[idx, :].위도).tolist(),  # numpy
                'lng': (vegan_df.iloc[idx, :].경도).tolist()  # numpy
            })
    # print(zerowasteList[{'id' : '1' , 'name' : 'asdf'}])
    print('veganList all complete!!')
    # print(veganList[0])

    return JsonResponse(veganList, safe=False)

# 베이커리
def vegan_data_bake(request) :
    print('mapApp vegan bake index ~')

    veganList = []
    for idx in vegan_df.index:
        if vegan_df.iloc[idx, 7] == '베이커리':
            veganList.append({
                'id': (vegan_df.iloc[idx, :].번호).tolist(),  # numpy
                'name': vegan_df.iloc[idx, :].상호명,
                'number': vegan_df.iloc[idx, :].전화번호,
                'address': vegan_df.iloc[idx, :].소재지,
                'category': vegan_df.iloc[idx, :].업종,
                'about': vegan_df.iloc[idx, :].설명,
                'imgURL': vegan_df.iloc[idx, :].imgURl,
                'img': vegan_df.iloc[idx, :].jpg,
                'lat': (vegan_df.iloc[idx, :].위도).tolist(),  # numpy
                'lng': (vegan_df.iloc[idx, :].경도).tolist()  # numpy
            })
    # print(zerowasteList[{'id' : '1' , 'name' : 'asdf'}])
    print('veganList all complete!!')
    # print(veganList[0])

    return JsonResponse(veganList, safe=False)

# 분식/술집/뷔페식/기타
def vegan_data_etc(request) :
    print('mapApp vegan etc index ~')

    veganList = []
    for idx in vegan_df.index:
        if vegan_df.iloc[idx, 7] == '분식' or vegan_df.iloc[idx , 7] == '술집' or vegan_df.iloc[idx , 7] == '뷔페식' or vegan_df.iloc[idx , 7] == '기타' :
            veganList.append({
                'id': (vegan_df.iloc[idx, :].번호).tolist(),  # numpy
                'name': vegan_df.iloc[idx, :].상호명,
                'number': vegan_df.iloc[idx, :].전화번호,
                'address': vegan_df.iloc[idx, :].소재지,
                'category': vegan_df.iloc[idx, :].업종,
                'about': vegan_df.iloc[idx, :].설명,
                'imgURL': vegan_df.iloc[idx, :].imgURl,
                'img': vegan_df.iloc[idx, :].jpg,
                'lat': (vegan_df.iloc[idx, :].위도).tolist(),  # numpy
                'lng': (vegan_df.iloc[idx, :].경도).tolist()  # numpy
            })
    # print(zerowasteList[{'id' : '1' , 'name' : 'asdf'}])
    print('veganList all complete!!')
    # print(veganList[0])

    return JsonResponse(veganList, safe=False)


# Login page
# 로그인
def login(request):
    response_data = {}
    if request.method == 'POST':
        login_username = request.POST.get('user_id', None)
        login_password = request.POST.get('user_pwd', None)
        if not (login_username and login_password):
            response_data['error'] = "아이디와 비밀번호를 모두 입력해주세요."
        else:
            myuser = WwgUser.objects.get(user_id=login_username)
            # db에서 꺼내는 명령. Post로 받아온 username으로 , db의 username을 꺼내온다.
            if check_password(login_password, myuser.user_pwd):
                request.session['user'] = myuser.user_id
                print(request.session['user'], '~~~~~~~~~~~')
                # 세션도 딕셔너리 변수 사용과 똑같이 사용하면 된다.
                # 세션 user라는 key에 방금 로그인한 id를 저장한것.
                return redirect('main')
            else:
                response_data['error'] = "비밀번호를 틀렸습니다."
                return render(request, 'map/login.html', response_data)
    return render(request, 'map/login.html')

# 로그아웃
def logout(request):
    return redirect('main')

#
def join(request):
    return redirect('main')

# 회원가입
def registerForm(request):
    if request.method == 'POST':
        print('RegisterForm index ~ ')
        # 딕셔너리 형태
        print('POST~~~~~')
        print(request.POST.get('user_id', None))
        user_id = request.POST.get('user_id', None)
        user_pwd = request.POST.get('user_pwd', None)
        user_birthyear = request.POST.get('user_birthyear', None)
        res_data = {}
        if not (user_id and user_pwd and user_birthyear):
            res_data['error'] = "모든 값을 입력해야 합니다."
        else:
            user = WwgUser(user_id=user_id, user_pwd=make_password(user_pwd), user_birthyear=user_birthyear)
            user.save()
        return render(request, 'map/about.html', res_data)  # register를 요청받으면 registerForm.html 로 응답.
    return render(request, 'map/registerForm.html')


# csv to model
def CsvToModel(request):
    # Zerowaste Shop loading
    path = 'C:/Users/loadt/PycharmProjects/pythonProject1/rootWEB/zerowaste_fin_utf8.txt'
    file = open(path, encoding='utf-8')
    reader = csv.reader(file)
    print('----', reader)
    z_list = [];
    idx = 0
    for row in reader:
        if idx != 0:
            z_list.append(WwgZerowaste(
                index=row[0],
                name=row[1],
                number=row[2],
                address=row[3],
                category=row[4],
                about=row[5],
                imgURL=row[6],
                img=row[7],
                lat=float(row[8]),
                lng=float(row[9]),
            ))
        idx += 1
    # print(z_list)
    WwgZerowaste.objects.bulk_create(z_list)

    # Vegan Food Shop loading
    path = 'C:/Users/loadt/PycharmProjects/pythonProject1/rootWEB/vegan_fin_utf8.txt'
    file = open(path, encoding='utf-8')
    reader = csv.reader(file)
    print('----', reader)
    z_list = [];
    idx = 0
    for row in reader:
        if idx != 0:
            z_list.append(WwgVegan(
                index=row[0],
                name=row[1],
                number=row[2],
                address=row[3],
                category=row[4],
                about=row[5],
                imgURL=row[6],
                img=row[7],
                lat=float(row[8]),
                lng=float(row[9]),
            ))
        idx += 1
    # print(z_list)
    WwgVegan.objects.bulk_create(z_list)
    return HttpResponse('create model~~~~~~')


# Board page
def board(request):
    print('mapApp index ~ ')
    return render(request, 'map/board.html')


# def register(request) :
#     print('mapApp index ~ ')
#     return render(request , 'map/registerForm.html')

