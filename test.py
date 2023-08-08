from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def do_claim():
    url = "https://hello.hashkey.com/api/user/kyc/claim"
    headers = {"Authorization": "bearer 2ff6cc423a1b48e888ef61c8badba76f",
             "Content-Type": "application/json",
             "User-Agent": "Mozilla",
             "Accept-Encoding": "gzip, deflate"}

    post_body = '{}'
    try:
        r = requests.post(url, data=post_body, headers=headers, verify=False)
        print(r.text)
    except Exception as e:
        print(e)


if __name__ == '__main__':
    with ThreadPoolExecutor(max_workers=1000) as executor:  
        futures = as_completed([executor.submit(do_claim,) for i in range(1000)])
