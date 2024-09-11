import requests
from bs4 import BeautifulSoup as bs

def test(process_url):
    # 요청할 때 User-Agent를 추가하여 브라우저처럼 보이게 만듦
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(process_url, headers=headers)

    # 상태 코드 확인
    print(f"Status Code: {response.status_code}")

if __name__ == "__main__":

    url = 'https://search.shopping.naver.com/search/all?bt=-1&frm=NVSCPRO&query=%EC%9D%B4%EC%A7%80%ED%99%88+%ED%96%89%EA%B1%B0'
    exrental = '&exrental=true' # 렌탈제외
    exused = '&exused=true' # 중고제외
    exagency = '&exagency=true' # 해외직구제외
    pagingindex = '&pagingIndex=1' # 페이지 넘버
    pagingsize = '&pagingSize=80' # 한 페이지 보이는 상품
    process_url = f"{url}{exrental}{exused}{exagency}{pagingindex}{pagingsize}"

    process_url_test = 'https://www.naver.com'

    test(process_url_test)