# ^_^ coding: utf-8
import urllib.request
import urllib.parse
# Python3中把http连接集成为一个库urllib。
# URL_PREX = "http://httpbin.org"
URL_BASE = "http://www.5566.net"


def use_simple_way(name="ip"):
    t_url = "/".join([URL_BASE, name])
    values = {"name": "rocky", "className": "红旗Linux"}
    def_head = {"age": "1"}
    u_data = urllib.parse.urlencode(values).encode(encoding="ascii")

    req = urllib.request.Request(t_url, headers=def_head, data=u_data)

    try:
        response = urllib.request.urlopen(req)
    except urllib.request.HTTPError as e:
        print("the http error {}, code {}".format(e.reason, e.code))
    except urllib.request.URLError as e:
        if hasattr(e, "reason"):
            print("the url error {}".format(e.reason))
    else:
        print(">>>>>>>>>>>>>>>>>")
        print(dir(response))
        print(response.headers["Content-Type"])
    return True

if __name__ == "__main__":
    use_simple_way()

