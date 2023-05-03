# python bolt 
APIの学習のためにAWSも併せて実装してみる。  
TODO
  - CloudWatchで定期メッセージ送信  
  - ChatGPT APIをつないでSlackでつかう

## publishing message
### ch-name2ch-id.py
チャンネル名を入力とし、チャンネルIDを取得する  

### publish_message.py
チャンネルIDで投稿先チャンネルを指定し、メッセージを投稿できる  

## AWS Lambda + CloudWatch Events
定期実行を行う実装



参考  
---
<publishing message>
https://api.slack.com/messaging/sending
