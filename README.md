# 機能

* [ ] 時間
* [ ] 先生
* [ ] 温度・湿度
* [ ] 電車
* [ ] 天気
* [ ] メッセージ

# APIサーバーの仕様

```
{
   time : "",
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
