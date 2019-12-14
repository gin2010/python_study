import urllib
import requests


def invoiceQuery(appcode):
    datas = {
            "appcode":appcode,
            "data":{
                "nsrsbh":"91110000710927388B",
                "fpdm":"011001900211",
                "fphm":"32362680",
                "kprq":"20190430",
                "je":"52.21",
                "jym":"718779"
                }
            }
    url = "https://51fpin.aisino.com:8443/Aisinojxpf/fpcy/fpcy.action"

    r= requests.post(url,data=datas)

    print(datas["appcode"])
    # print(r.json)
    print(r.text)

def companyInfoQuery():
    # url = "http://192.168.15.252:28986/service/qnsr/sfrz-nsrxx-913702008636074141"
    url = "http://192.168.15.252:28986/service/qnsr/sfrz-nsrxx-123456789012199"

    res = requests.get(url)
    print(res.status_code)

if __name__=="__main__":
    # for i in range(1,9999):
    #     invoiceQuery(str(i))
    companyInfoQuery()