# jq_api_get_fins_statements_date.py
J-QuantsAPIベータ版で、日付期間を指定して財務情報を取得するお試しプログラム 

1）動作テストを実行した環境は、os: Centos7.4、python: 3.6.8 です。

２）実行はコマンドプロンプト等からpython環境で起動してください。
  
  有効期限内のIDトークンをファイルに保存してある必要が有ります。
    
    # 起動:  ./jq_api_get_fins_statements_date.py  from=[yyyymmdd]  to=[yyyymmdd]
      
    # ＩＤトークン保存ファイル名: 'jq_idtoken.json'
    
    # 財務データ出力ファイル名: 'jq_fins_statements_date.csv'
    
３）本プログラムは自由にご使用ください。

４）このソフトウェアを使用したことによって生じたすべての障害・損害・不具合等に関して、私と私の関係者および私の所属するいかなる団体・組織とも、一切の責任を負いません。各自の責任においてご使用ください。
