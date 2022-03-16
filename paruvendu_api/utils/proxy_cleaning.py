import pandas as pd

df = pd.read_csv('C:/Users/Pontiff/Desktop/testerino/SIMPLON_PARUVENDU_API/paruvendu_api/paruvendu_api/outputs/Free_Proxy_List.txt')
ip_list = df[['ip','port']]
loop_length = len(ip_list)
f = open('C:/Users/Pontiff/Desktop/testerino/SIMPLON_PARUVENDU_API/paruvendu_api/paruvendu_api/outputs/proxy_list.txt', 'a')
for i in range(0,loop_length):
    value = ip_list.iloc[i]
    line = str(value['ip'])+":"+str(value["port"])+'\n'
    f.write(line)
f.close()
    

