import requests


def test_FixedToCurrentApply():
    url = "http://182.188.3.62:4900/mock/101/mca/mrpay/FixedToCurrentApply.htm"
    data = {
        "acNo": "100000004003"
    }
    res = requests.post(url, json=data)
    print(res.text)
