# 機能

* [ ] 時間
* [ ] 先生
* [ ] 温度・湿度
* [ ] 電車
* [ ] 天気
* [ ] メッセージ

# URLリスト

* webの表示
* web表示用API
* 研究室Raspberryからの受信
* 教授Raspberryからの受信

# web表示APIサーバーの仕様

```
{
   time : {},
   teacher_status : "",
   lab : {
     temperature: "",
     humidity: ""
   },
   outside: {
     weather: "",
     temperature: "",
     humidity: ""
   },
   trains: [
     {
         "name": "",
         "state": ""
     },
   ],
   messages: {
   }
}
```
