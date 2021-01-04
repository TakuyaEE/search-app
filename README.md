# [求人情報検索アプリ](takuyaee.cc)
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
