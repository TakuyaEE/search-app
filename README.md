# [求人情報検索アプリ](http://takuyaee.cc/)
## webフォームに条件を入力し、求人サイトから求人をスクレイピングしてくるアプリです。

実務未経験から他の求職者との差別化を図るため、リアリティのあるポートフォリオを目指して作成いたしました。

受講中の職業訓練校のクラスメイトをターゲットに設定し、フィードバックを受けながら機能を追加していきたいと思っております。


## 使用言語等
- Python 3.8.6
    - webフレームワーク             flask
    - ブラウザ操作＆スクレイピング   selenium, BeautifulSoup4
    - データ処理                    pandas
    - LineMessageAPI               linebot
    - モジュール分割                Blueprints
    - ユニークID生成                uuid
- Firebase
    - ユーザー認証、ストレージ、DBを使用
- フロントエンド
    - CSS,JavaScriptフレームワーク  bootstrap(honoka), jQuery
- インフラ
    - heroku(12/26~1/5)
        - 30秒でリクエストがタイムアウトする仕様がアプリと合わなかったため
    - AWS Elastic Beanstalk,Route53(1/5~)
    - AWS ECS + CircleCI(予定)
        - docker化してCircleCIでの自動テスト・デプロイを実装予定  
  
  
## 機能説明
- ハローワーク求人情報検索
    - フォームから受け取った値をPOSTで受け取る
    - seleniumでchromeを使用し、ハローワークの求人検索ページに値を入力し、検索
    - BeautifulSoup,seleniumで情報を収集し、pandasで整形
    - 動的にテーブルを生成し、HTMLページに出力
    - ユーザー情報をもとにDBに検索結果を格納し、履歴を照会可能にする(作成中)
    - DBから必要な項目を選択し、csv出力、メール等で共有（作成中）
- バグ報告・問い合わせページ
    - フォームから受け取った値をPOSTで受け取る
    - 受け取った値をLINEBOTを使用し、製作者のLINEに送信
- しごとナビ求人情報検索（作成中）
    - しごとナビ求人検索APIを使用して、情報をjsonで取得
    - 動的にテーブルを生成し、HTMLページに出力
    - その他機能はハローワーク求人情報検索と同等のものを予定
- ユーザー情報登録・認証（作成中）
    - Firebaseを使用予定
    - ユーザー情報とDBを紐づけ、検索履歴を保存、閲覧可能にする


## 技術選定の際に考えたこと、意識して使用した技術
- このアプリを作った理由
    - 未経験からのエンジニア転職ということで、技術や考え方をアピールする手段としてポートフォリオは大きな役割を持つと考えました。<br>
    経験者も応募してくる中、ハードスキルでアピールすることは難しく、ソフトスキルでアピールする必要がありました。<br>
    そのため、リアリティのあるアプリを作りたいと考え、受講中であった職業訓練校のクラスメイトをターゲットに設定し、フィードバックをもらいながら、アジャイル開発をしていこうと考えました。<br>
    求人情報検索は、就職活動を進めていく上で必須でありながら、大きなリソースを割かれていると思い、自動化することには大きなメリットがあると考え、このアプリを制作しました。

- 要件定義
    -  アプリを作成するうえで、最低限必要な機能として、次の3つを定義しました。<br>
    1.フォームに検索条件を入力し、自動で検索<br>
    2.検索結果から情報を収集し、整形・出力<br>
    3.バグ報告や問い合わせをしやすいようにフォームの設置<br><br>
    さらに、使いやすくするために実装したい機能として、以下を考えました。<br>
    ・ユーザー登録をし、検索履歴を保持<br>
    ・検索結果から任意の情報を選択し、csvで出力、メール等で共有
  
- 機能毎に意識して使用した技術、学習した知識
    -   <strong>検索条件設定ページ</strong><br>
        ・JavaScriptによるフォームコントロールを行い、意図しないPOSTを防止<br>
        ・情報を収集して結果を表示するまでに時間がかかるため、検索を押した後に案内の表示、ローディングアニメーションの作成、設置<br>
        ・POST、GET、それぞれのメソッドの理解<br>
        <strong>検索結果表示ページ</strong><br>
        ・flask内蔵のjinja2による動的なHTMLの生成<br>
        <strong>問い合わせページ</strong><br>
        ・個人開発のため、送信先にメールではなく、LINEを設定<br>
        ・LINE MessageAPIを使用することで、APIトークン、キー、webhook等、APIへの理解

- なぜ「Python」?
    -   学習するサーバーサイド言語として、候補に挙がったのは「Java」「PHP」「RUby」「Python」の4つでした。<br>
    その中から「Python」を選択した理由は、大きく分けて3つあります。<br>
    1.可読性が高く、短くコードが書けるので、理解しやすいと考えたこと<br>
    2.学習の方向性が定まっていなかった為、ライブラリが豊富で、様々な分野をこなせることに魅力を感じたこと<br>
    3.基本情報技術者試験の受験を決めていたため、午後の言語として選択できること<br>
    以上、3つの点を考慮して最初に学習する言語として「Python」を選択しました。

- なぜ「Django」ではなく「flask」?
    -  開発を一人で進めるうえで、「Django」ではオーバースペックに感じたからです。<br>
    機能が少ないことも、学習コストが低く小回りが利くという面でデメリットよりもメリットを大きく感じました。<br>
    また、機能が少ないことでライブラリに頼らざるを得ず、ライブラリを自分で選定し、設定することは学習効果が大きいと考えました。


## ディレクトリ構成  
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
└─templates htmlファイル
