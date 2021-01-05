# [求人情報検索アプリ](http://takuyaee.cc/)
## webフォームに条件を入力し、求人サイトから求人をスクレイピングしてくるアプリです。

実務未経験から他の求職者との差別化を図るため、リアリティのあるポートフォリオを目指して作成いたしました。

受講中の職業訓練校のクラスメイトをターゲットに設定し、フィードバックを受けながら機能を追加していきたいと思っております。







- Python
    - webフレームワーク             flask
    - ブラウザ操作＆スクレイピング   selenium, BeautifulSoup4
    - データ処理                    pandas
    - LineMessageAPI               linebot
    - モジュール分割                Blueprints
    - ユニークID生成                uuid
- フロントエンド
    - CSS,JavaScriptフレームワーク  bootstrap, jQuery
- インフラ
    - heroku(12/26~1/5)
        - 30秒でリクエストがタイムアウトする仕様がアプリと合わなかったため
    - AWS Elastic Beanstalk(1/5~)
    - AWS ECS + CircleCI(予定)
        - docker化してCircleCIでの自動テスト・デプロイを実装予定
  
- ディレクトリ構成  
search-app  
│  app.py ルーティング設定  
│  app_inquiry.py　問い合わせフォームの処理  
│  app_search_hellowork.py　フォームから値を受け取り、検索・データ処理  
│  chromedriver  自動操作用のブラウザ  
│  Procfile  初めに開くファイル（app.py）を設定  
│  README.md  
│  requirements.txt 使用ライブラリ情報  
│  runtime.txt pythonのバージョン情報を記載  
│  
├─docker  
│  
├─documment  
│  
├─output  
│  
├─static  
│  ├─css　スタイルシート  
│  └─js　スクリプトファイル  
│  
└─templates  
│  ├─base.html  
│  ├─hellowork.html　検索条件設定ページのhtml  
│  ├─index.html ルートhtml  
│  ├─inquiry.html 問い合わせフォームhtml  
│  ├─inquiry_send.html 問い合わせ完了ページのhtml  
│  ├─no_result.html　検索結果なしhtml  
│  ├─results.html　検索結果表示html  
│  ├─search.html  検索条件送信先のhtml  
│  └─technology.html 技術選定についてhtml  

