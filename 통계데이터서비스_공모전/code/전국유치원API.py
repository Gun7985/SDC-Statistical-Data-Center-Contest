import requests
import csv
from datetime import datetime

# API 키와 기본 URL 설정
API_KEY = "f81f09226bd640728e903a0c98ef6dd6"
BASE_URL = "https://e-childschoolinfo.moe.go.kr/api/notice/basicInfo2.do"

# 요청할 시군구 목록
regions = [
    {"sido": "41", "sgg": "41390", "name": "경기도 시흥시"},
    {"sido": "41", "sgg": "41173", "name": "경기도 안양시 동안구"},
    {"sido": "41", "sgg": "41450", "name": "경기도 하남시"},
    {"sido": "41", "sgg": "41610", "name": "경기도 광주시"},
    {"sido": "41", "sgg": "41465", "name": "경기도 용인시 수지구"},
    {"sido": "29", "sgg": "29170", "name": "광주광역시 북구"},
    {"sido": "29", "sgg": "29140", "name": "광주광역시 서구"},
    {"sido": "28", "sgg": "28237", "name": "인천광역시 부평구"},
    {"sido": "31", "sgg": "31200", "name": "울산광역시 북구"},
    {"sido": "47", "sgg": "47190", "name": "경상북도 구미시"}
]

# 현재 년도와 차수 설정 (예: 20241)
current_year = datetime.now().year
timing = f"{current_year}1"

# CSV 파일 생성
csv_filename = f"kindergarten_info_{current_year}.csv"
csv_headers = ["지역", "유치원명", "주소", "전화번호", "정원", "현원"]

with open(csv_filename, 'w', newline='', encoding='utf-8-sig') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=csv_headers)
    writer.writeheader()

    # 각 지역별로 API 요청 및 데이터 저장
    for region in regions:
        params = {
            "key": API_KEY,
            "sidoCode": region["sido"],
            "sggCode": region["sgg"],
        }

        response = requests.get(BASE_URL, params=params)
        
        if response.status_code == 200:
            data = response.json()
            kindergartens = data.get("cpmsapi030", {}).get("kinderInfo", [])
            
            for kinder in kindergartens:
                writer.writerow({
                    "지역": region["name"],
                    "유치원명": kinder.get("kindername", ""),
                    "주소": kinder.get("addr", ""),
                    "전화번호": kinder.get("telno", "")
                })
            
            print(f"{region['name']} 데이터 저장 완료")
        else:
            print(f"{region['name']} 데이터 요청 실패: {response.status_code}")

print(f"모든 데이터가 {csv_filename}에 저장되었습니다.")