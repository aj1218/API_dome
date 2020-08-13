import requests
url='http://172.16.22.120:8089/benchmarking/getBenchmarking'
data={
    "pids": ["TR-SX-DH06|4","TR-PR-P-CINTURATO-P1|37","TR-PR-P-CINTURATO-P1|4","123"]
}
res=requests.post(url,json=data)
print(res.json())
