import requests, time, getopt, sys

proxy_list = [line.rstrip('\n') for line in open('us.txt')]
while True:
    for http_proxy in proxy_list:
        try:
            proxyDict = { 
                      "http"  : http_proxy, 
                        }

            cookie={"__cfduid":"dc316f74e22f9e63278b4773663af578c1463108320",
            "Permanent.CookieTest":"1",
            "bknx_fa":"1463108319346",
            "bknx_ss":"1463108319346",
            "__gads:ID":"6316595d2b0ab898:T:1463108322:S:ALNI_Maace1-WF_089fay2QjKVnffZZtkA",
            "Auth.TimeLock":"1", 
            "Auth.SessionLock":"1",
            "Auth.NetworkSession":"GNFH9B1L9Y9JYLEDLIX1QFMIN7AXJTKMG5JM3FQ69LVTBM5E",
            "OX_plg":"swf|shk|pm",
            "__qca":"P0-964655518-1463109746600",
            "cdmtlk":"576:341:465:0:341:0:848:342:313",
            "cdmgeo":"us",
            "cdmbaserate":"2.5",
            "cdmbaseraterow":"1.5",
            "cdmint":"0",
            "_gat_UA-37896755-37":"1",
            "_ga":"GA1.2.1433184982.1463108319",
            "_gat_spTracker2":"1",
            "_ceg.s":"o73j5k",
            "_ceg.u":"o73j5k",
            "cdmua":"1463110328719",
            "cdmblk2":"1.2:0.6:0:0:0:0:1.1:0.8:0,0:0:0:0:0:0:0:0:0,0.9:0.4:0:0:0:0:0.5:0.5:0,0:0:0:0:0:0:0:0:0,0:0:0:0:0:0:0:0:0,0:0:0:0:0:0:0:0:0",
            "cdmblk":"1.9:0.7:0:0:0:0:0:0.5:0,0:0:0:0:0:0:0:0:0,1:0.7:0:0:0:0:0.2:0.5:0,0:0:0:0:0:0:0:0:0,0:0:0:0:0:0:0:0:0,0:0:0:0:0:0:0:0:0"}


            request_url="http://www.strawpoll.me/10197397"
            post_security_token='security-token'
            f8e3a9b92dbcb1af7401c8abdbbfab0eb="f8e3a9b92dbcb1af7401c8abdbbfab0eb"
            options="options"
            post_data={options:"110815041", f8e3a9b92dbcb1af7401c8abdbbfab0eb:"", post_security_token:"d9dd3ea6a188085b7b53c0549d64ec6c"}
            headers_data={"Server": "cloudflare-nginx","CF-RAY": "2a22c227dc57225e-LAX"}
            with requests.Session() as c:
                c.post(request_url,data=post_data,cookies=cookie,headers=headers_data,proxies=proxyDict)
            print ("[+] Sent and received data: "+http_proxy)
        except:
            print("[-] Failed: "+http_proxy)
            pass;






    
