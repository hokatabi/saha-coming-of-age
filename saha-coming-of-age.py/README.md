# coming-of-age

生年月日を設定すると、二十歳になるまであと何日かをツイートするLambdaのスクリプト。

* Python 8.3で動作確認。
* うるう年の2月29日生まれには対応していないです。

以下のコマンドでfunction packageを作成し、Lambdaにuploadする必要があります。
```
$ pip install requests requests-oauthlib -t .
$ zip -r upload.zip *
```
