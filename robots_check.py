import urllib.robotparser
from urllib.parse import urlparse

def can_fetch(url, user_agent='*'):
    """
    URL에 대해 robots.txt 규칙을 기반으로 user_agent가 액세스할 수 있는지 확인한다.
    
    Args:
    - url (str): 액세스하려는 URL.
    - user_agent (str): 확인하려는 user agent의 이름으로, 기반값은 '*'로, 모든 user agent에 대해 검사한다.
    
    Returns:
    - bool: user agent가 해당 URL에 액세스할 수 있으면 True, 그렇지 않으면 False를 반환한다.
    """
    # robots.txt 파일의 URL을 구성
    parsed_url = urlparse(url)
    robots_url = f"{parsed_url.scheme}://{parsed_url.netloc}/robots.txt"
    
    # RobotFileParser 객체를 생성하고 robots.txt를 파싱
    rp = urllib.robotparser.RobotFileParser()
    rp.set_url(robots_url)
    rp.read()
    
    # 주어진 URL에 대해 user_agent가 액세스할 수 있는지 확인
    return rp.can_fetch(user_agent, url)

def main():
    # 사용자로부터 URL 입력 받기
    url_to_check = input("액세스하려는 URL을 입력하세요: ")
    user_agent = 'MyCrawler'
    
    can_access = can_fetch(url_to_check, user_agent)
    if can_access:
        print(f"{user_agent} can access {url_to_check}")
    else:
        print(f"{user_agent} cannot access {url_to_check}")

# 프로그램 실행
if __name__ == '__main__':
    main()
