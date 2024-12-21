# ChenkFan
用途：仅限于查询B站用户粉丝牌  
注：在其他大佬的代码上进行修改，如有雷同，不是巧合  

## 使用说明
### cookie获取
进入网址：~~（先查下站长成分）~~ https://api.live.bilibili.com/xlive/web-ucenter/user/MedalWall?target_id=2  
按下F12进入控制台，找到网络，点击全部。刷新网页后找到MedalWall，点进去右侧找到cookie，全部复制下来备用  
<img src=".\说明.png">   

### 使用流程
打开FindPaiZi.exe  
输入获取的cookie  
选择是否仅查询舰长牌子：yes-->仅显示有这些主播的舰长牌子 no-->显示所有粉丝牌 
输入uid进行查询  
选择是否结束  

### 可能错误说明:
如果没给出结果直接闪退。以下给出一些解决参考：  
1.注意cookie是否复制完全  
2.如cookie没错，登录网页版的bilibili后重新获取cookie  




