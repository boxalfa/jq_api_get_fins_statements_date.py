# -*- coding: utf-8 -*-
# 2022.10.03 coded by yo.
# MIT License
# Python 3.6.8 / centos7.4

import urllib3
import requests
import datetime
import json
import sys
from datetime import datetime as dt



# 変数名  説明  型  例
# DisclosureNumber  開示番号  String  20220126573026
# DisclosedDate  開示日  String  44588
# ApplyingOfSpecificAccountingOfTheQuarterlyFinancialStatements  四半期財務諸表の作成に特有の会計処理の適用  String  ​
# AverageNumberOfShares  期中平均株式数  String  530119112
# BookValuePerShare  1株当たり純資産  String  ​
# ChangesBasedOnRevisionsOfAccountingStandard  会計基準等の改正に伴う会計方針の変更  String  0
# ChangesInAccountingEstimates  会計上の見積りの変更  String  0
# ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard  会計基準等の改正に伴う変更以外の会計方針の変更  String  0
# CurrentFiscalYearEndDate  当事業年度終了日  String  44651
# CurrentFiscalYearStartDate  当事業年度開始日  String  44287
# CurrentPeriodEndDate  当会計期間終了日  String  44561
# DisclosedTime  開示時刻  String  0.5
# DisclosedUnixTime  開示UnixTime  String  1643252400
# EarningsPerShare  1株当たり当期純利益  String  71.71
# Equity  純資産  String  42714000000
# EquityToAssetRatio  自己資本比率  String  0.005
# ForecastDividendPerShare1stQuarter  配当予想_第1四半期末  String  ​
# ForecastDividendPerShare2ndQuarter  配当予想_第2四半期末  String  ​
# ForecastDividendPerShare3rdQuarter  配当予想_第3四半期末  String  ​
# ForecastDividendPerShareAnnual  配当予想_合計  String  53
# ForecastDividendPerShareFiscalYearEnd  配当予想_期末  String  27
# ForecastEarningsPerShare  1株当たり当期純利益_通期予想  String  50.31
# ForecastNetSales  売上高_通期予想  String  ​
# ForecastOperatingProfit  営業利益_通期予想  String  ​
# ForecastOrdinaryProfit  経常利益_通期予想  String  ​
# ForecastProfit  当期純利益_通期予想  String  850000000
# LocalCode  銘柄コード  String  86970
# MaterialChangesInSubsidiaries  期中における重要な子会社の異動  String  0
# NetSales  売上高  String  100586000000
# NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock  期末発行済株式数  String  536351448
# NumberOfTreasuryStockAtTheEndOfFiscalYear  期末自己株式数  String  8822727
# OperatingProfit  営業利益  String  55967000000
# OrdinaryProfit  経常利益  String  55936000000
# Profit  当期純利益  String  591000000
# ResultDividendPerShare1stQuarter  配当実績_第1四半期末  String  －
# ResultDividendPerShare2ndQuarter  配当実績_第2四半期末  String  26
# ResultDividendPerShare3rdQuarter  配当実績_第3四半期末  String  －
# ResultDividendPerShareAnnual  配当実績_合計  String  ​
# ResultDividendPerShareFiscalYearEnd  配当実績_期末  String  ​
# RetrospectiveRestatement  修正再表示  String  ​
# TotalAssets  総資産  String  62076519000000
# TypeOfCurrentPeriod  当会計期間の種類  String  3Q
# TypeOfDocument  書類種別  String  3QFinancialStatements_Consolidated_IFRS





# ---------------------------------------------
# 機能: コマンドライン入力のパラメーターをチェックする。
# 引数1: コマンドライン入力のパラメーター（list型）
# 引数2: 出力ファイル名（string型）
# 返値: なし
# ---------------------------------------------
def func_parse_parameter(sys_argv, str_fname_output):
    if len(sys_argv) == 2 :
        if sys_argv[1] == '-h' \
            or sys_argv[1] == '--help':
            print(sys_argv[0], ' form=[yyyymmdd] to=[yyyymmdd]')
            print()
            print('sample')
            print(sys_argv[0], 'form=20220801 to=20220831')
            print(sys_argv[0], 'form=20220808')
            print(sys_argv[0], 'to=20220808')
            exit()
        else :
            pass
        
    elif len(sys_argv) == 1 or len(sys_argv) > 5 :
            print(sys_argv[0], ' form=[yyyymmdd] to=[yyyymmdd]')
            print()
            print('sample')
            print(sys_argv[0], 'form=20220801 to=20220831')
            print(sys_argv[0], 'form=20220808')
            print(sys_argv[0], 'to=20220808')
            exit()
    else:
        pass


# ---------------------------------------------
# 機能: コマンドライン入力のパラメーターを取得する。
# 引数1: コマンドライン入力のパラメーター（list型）
#
# 返値: 引数セット（辞書型）
# ---------------------------------------------
def func_get_parameter(sys_argv) :
    str_start = ''
    str_end = ''
    for i in range(len(sys_argv)) :
        if i > 0 :
            if sys_argv[i][:5] == 'code=' :
                print('日付け指定のみできます。')
                print('form=[yyyymmdd] to=[yyyymmdd]')
                exit()
            elif sys_argv[i][:5] == 'from=' :
                if len(sys_argv[i][5:]) == 8 :
                    str_start = sys_argv[i][5:]
                else :
                    print('開始日付けを正しく指定してください。')
                    print('form=[yyyymmdd] to=[yyyymmdd]')
                    exit()
            elif sys_argv[i][:3] == 'to=' :
                if len(sys_argv[i][3:]) == 8 :
                    str_end = sys_argv[i][3:]
                else :
                    print('終了日付けを正しく指定してください。')
                    print('form=[yyyymmdd] to=[yyyymmdd]')
                    exit()
            else :
                print('入力パラメーターの形式が正しくありません。')
                print('sys_rgv[', i,']:', sys.argv[i])
                print('日付け指定のみできます。')
                print('form=[yyyymmdd] to=[yyyymmdd]')
                exit()
    if len(str_start) == 8 and len(str_end) == 8 :
        date_start = datetime.datetime.strptime(str_start, '%Y%m%d')
        date_end   = datetime.datetime.strptime(str_end, '%Y%m%d')
        if date_start > date_end :
            date_tmp = date_start
            date_start = date_end
            date_end = date_tmp

    elif len(str_start) == 8 and len(str_end) == 0 :
        date_start = datetime.datetime.strptime(str_start, '%Y%m%d')
        date_end   = date_start
    elif len(str_start) == 0 and len(str_end) == 8 :
        date_end = datetime.datetime.strptime(str_end, '%Y%m%d')
        date_start = date_end
    else :
        print('入力パラメーターの形式が正しくありません。')
        print('sys_rgv[', i,']:', sys.argv[i])
        print('日付け指定のみできます。')
        print('form=[yyyymmdd] to=[yyyymmdd]')
        exit()
    
    dic_argv = {'from=':date_start, 'to=':date_end}
    return dic_argv



# ---------------------------------------------
# 機能 : 起動したディレクトリでファイルに書き込む。
# 引数1: 出力ファイル名（string型）
# 引数2: 出力文字列（string型）
# 返値 : 無し
# ---------------------------------------------
def func_read_from_file(str_fname):
    str_read = ''
    try:
        with open(str_fname, 'r', encoding = 'utf_8') as fin:
            while True:
                line = fin.readline()
                if not len(line):
                    break
                str_read = str_read + line
        return str_read

    except IOError as e:
        print('Can not read!!!')
        print(type(e))



# ---------------------------------------------
# 機能 : 起動したディレクトリでファイルに書き込む。
# 引数1: 出力ファイル名（string型）
# 引数2: 出力文字列（string型）
# 返値 : 無し
# ---------------------------------------------
def func_write_to_file(str_fname_output, str_text):
    try:
        with open(str_fname_output, 'w', encoding = 'utf_8') as fout:
            fout.write(str_text)     

    except IOError as e:
        print('Can not write!!!')
        print(type(e))




# ---------------------------------------------
# 機能 : ファイルに保存してあるIDトークンを読み出す。
# 引数1: IDトークン保存ファイル名（string型）
# 返値 : IDトークン（string型）
# 備考 : IDトークン保存ファイルのデータ形式は、
#   {"time_idtoken":"value","idToken":"value"}
# ---------------------------------------------
def func_read_idtoken(str_fname_idtoken):
    # ＩＤトークンの読み出し
    str_id_json = func_read_from_file(str_fname_idtoken)

    dic_idtoken = json.loads(str_id_json)
    str_idtoken = dic_idtoken.get('idToken')
    # ＩＤトークンを取得できない場合
    if str_idtoken is None :
        print('ＩＤトークンが取得できません。')
        quit()

    # ＩＤトークンの取得時間を表示
    str_time_idtoken = dic_idtoken.get('time_idToken')
    time_idtoken = dt.strptime(str_time_idtoken, '%Y-%m-%d %H:%M:%S.%f')
    print('[ id token ]')
    print('time stamp :', time_idtoken)

    # ＩＤトークンの有効期限を表示（有効期限24時間）
    span_expire = datetime.timedelta(days=1)
    time_expire = time_idtoken + span_expire
    print('expiry date:', time_expire)
    time_remain = time_expire - datetime.datetime.now()
    print('remaining time:', time_remain)
    if time_remain > datetime.timedelta(days=0) :
        print('IDトークンの有効期間は２４時間です。')
    else :
        print('IDトークンは、無効です。有効期間を過ぎました。')
        
    print()
    return str_idtoken





# ---------------------------------------------
# 機能 : 出力ファイルにタイトル行を書き込む。
# 引数1: 出力ファイル名（string型）
# 返値 : 無し
# ---------------------------------------------
def func_write_title(str_fname_output):
    # csvで保存
    try:
        with open(str_fname_output, 'w', encoding = 'utf_8') as fout:
            print('file open at w, "fout": ', str_fname_output )
            # 1行目 タイトル行
            str_text = ''

            str_text = str_text + '"' + '銘柄コード' + '"' + ','
            str_text = str_text + '"' + '開示日' + '"' + ','
            str_text = str_text + '"' + '開示番号' + '"' + ','
            str_text = str_text + '"' + '四半期財務諸表の作成に特有の会計処理の適用' + '"' + ','
            str_text = str_text + '"' + '期中平均株式数' + '"' + ','
            str_text = str_text + '"' + '1株当たり純資産' + '"' + ','
            str_text = str_text + '"' + '会計基準等の改正に伴う会計方針の変更' + '"' + ','
            str_text = str_text + '"' + '会計上の見積りの変更' + '"' + ','
            str_text = str_text + '"' + '会計基準等の改正に伴う変更以外の会計方針の変更' + '"' + ','
            str_text = str_text + '"' + '当事業年度終了日' + '"' + ','
            str_text = str_text + '"' + '当事業年度開始日' + '"' + ','
            str_text = str_text + '"' + '当会計期間終了日' + '"' + ','
            str_text = str_text + '"' + '開示時刻' + '"' + ','
            str_text = str_text + '"' + '開示UnixTime' + '"' + ','
            str_text = str_text + '"' + '1株当たり当期純利益' + '"' + ','
            str_text = str_text + '"' + '純資産' + '"' + ','
            str_text = str_text + '"' + '自己資本比率' + '"' + ','
            str_text = str_text + '"' + '配当予想_第1四半期末' + '"' + ','
            str_text = str_text + '"' + '配当予想_第2四半期末' + '"' + ','
            str_text = str_text + '"' + '配当予想_第3四半期末' + '"' + ','
            str_text = str_text + '"' + '配当予想_合計' + '"' + ','
            str_text = str_text + '"' + '配当予想_期末' + '"' + ','
            str_text = str_text + '"' + '1株当たり当期純利益_通期予想' + '"' + ','
            str_text = str_text + '"' + '売上高_通期予想' + '"' + ','
            str_text = str_text + '"' + '営業利益_通期予想' + '"' + ','
            str_text = str_text + '"' + '経常利益_通期予想' + '"' + ','
            str_text = str_text + '"' + '当期純利益_通期予想' + '"' + ','
            str_text = str_text + '"' + '期中における重要な子会社の異動' + '"' + ','
            str_text = str_text + '"' + '売上高' + '"' + ','
            str_text = str_text + '"' + '期末発行済株式数' + '"' + ','
            str_text = str_text + '"' + '期末自己株式数' + '"' + ','
            str_text = str_text + '"' + '営業利益' + '"' + ','
            str_text = str_text + '"' + '経常利益' + '"' + ','
            str_text = str_text + '"' + '当期純利益' + '"' + ','
            str_text = str_text + '"' + '配当実績_第1四半期末' + '"' + ','
            str_text = str_text + '"' + '配当実績_第2四半期末' + '"' + ','
            str_text = str_text + '"' + '配当実績_第3四半期末' + '"' + ','
            str_text = str_text + '"' + '配当実績_合計' + '"' + ','
            str_text = str_text + '"' + '配当実績_期末' + '"' + ','
            str_text = str_text + '"' + '修正再表示' + '"' + ','
            str_text = str_text + '"' + '総資産' + '"' + ','
            str_text = str_text + '"' + '当会計期間の種類' + '"' + ','
            str_text = str_text + '"' + '書類種別' + '"' + '\n'

            # タイトル２行目 英文        
            str_text = str_text + '"' + 'LocalCode' + '",'
            str_text = str_text + '"' + 'DisclosedDate' + '",'
            str_text = str_text + '"' + 'DisclosureNumber' + '",'
            str_text = str_text + '"' + 'ApplyingOfSpecificAccountingOfTheQuarterlyFinancialStatements' + '",'
            str_text = str_text + '"' + 'AverageNumberOfShares' + '",'
            str_text = str_text + '"' + 'BookValuePerShare' + '",'
            str_text = str_text + '"' + 'ChangesBasedOnRevisionsOfAccountingStandard' + '",'
            str_text = str_text + '"' + 'ChangesInAccountingEstimates' + '",'
            str_text = str_text + '"' + 'ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard' + '",'
            str_text = str_text + '"' + 'CurrentFiscalYearEndDate' + '",'
            str_text = str_text + '"' + 'CurrentFiscalYearStartDate' + '",'
            str_text = str_text + '"' + 'CurrentPeriodEndDate' + '",'
            str_text = str_text + '"' + 'DisclosedTime' + '",'
            str_text = str_text + '"' + 'DisclosedUnixTime' + '",'
            str_text = str_text + '"' + 'EarningsPerShare' + '",'
            str_text = str_text + '"' + 'Equity' + '",'
            str_text = str_text + '"' + 'EquityToAssetRatio' + '",'
            str_text = str_text + '"' + 'ForecastDividendPerShare1stQuarter' + '",'
            str_text = str_text + '"' + 'ForecastDividendPerShare2ndQuarter' + '",'
            str_text = str_text + '"' + 'ForecastDividendPerShare3rdQuarter' + '",'
            str_text = str_text + '"' + 'ForecastDividendPerShareAnnual' + '",'
            str_text = str_text + '"' + 'ForecastDividendPerShareFiscalYearEnd' + '",'
            str_text = str_text + '"' + 'ForecastEarningsPerShare' + '",'
            str_text = str_text + '"' + 'ForecastNetSales' + '",'
            str_text = str_text + '"' + 'ForecastOperatingProfit' + '",'
            str_text = str_text + '"' + 'ForecastOrdinaryProfit' + '",'
            str_text = str_text + '"' + 'ForecastProfit' + '",'
            str_text = str_text + '"' + 'MaterialChangesInSubsidiaries' + '",'
            str_text = str_text + '"' + 'NetSales' + '",'
            str_text = str_text + '"' + 'NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock' + '",'
            str_text = str_text + '"' + 'NumberOfTreasuryStockAtTheEndOfFiscalYear' + '",'
            str_text = str_text + '"' + 'OperatingProfit' + '",'
            str_text = str_text + '"' + 'OrdinaryProfit' + '",'
            str_text = str_text + '"' + 'Profit' + '",'
            str_text = str_text + '"' + 'ResultDividendPerShare1stQuarter' + '",'
            str_text = str_text + '"' + 'ResultDividendPerShare2ndQuarter' + '",'
            str_text = str_text + '"' + 'ResultDividendPerShare3rdQuarter' + '",'
            str_text = str_text + '"' + 'ResultDividendPerShareAnnual' + '",'
            str_text = str_text + '"' + 'ResultDividendPerShareFiscalYearEnd' + '",'
            str_text = str_text + '"' + 'RetrospectiveRestatement' + '",'
            str_text = str_text + '"' + 'TotalAssets' + '",'
            str_text = str_text + '"' + 'TypeOfCurrentPeriod' + '",'
            str_text = str_text + '"' + 'TypeOfDocument' + '"\n'
            
            fout.write(str_text)

            fout.close

    except IOError as e:
        print('Can not write!!!')
        print(type(e))

        


# ---------------------------------------------
# 機能 : J-Quants API に財務情報を問い合わせる。
# 引数1: IDトークンの値（string型）
# 引数1: 問合せURL（string型）
# 返値 : 財務データ（List型）
# ---------------------------------------------
def func_query_api(str_idToken, str_url):
    headers = {'Authorization': 'Bearer {}'.format(str_idToken)}
    resp = requests.get(str_url, headers=headers)

    dic_resp = json.loads(resp.text)    # jsonをパースして辞書型に変換
    if resp.status_code == 200 :
        # 正常に銘柄情報を取得
        list_statements = dic_resp.get('statements')       # "info"のvalueを取り出す。リスト型。
        return list_statements
    else :
        # info を取得できなかった場合
        # --- Message -----------------------------2022.10.03--
        # エラーで、403の場合のmessageは'M'と大文字になっているので注意。
        # エラーは400,401,403と3種類有る
        # 400: 未確認。これは何で起こるのしょう。
        # 401: {"message":"The incoming token has expired"}
        # 403: {"Message":"Access Denied"}
        # -----------------------------------------
        print('status_code:', resp.status_code)
        if resp.status_code == 400 or resp.status_code == 401 :
            print('message    :', dic_resp.get('message'))
        elif resp.status_code == 403 :
            print('message    :', dic_resp.get('Message'))
            print(resp.text)
        else :
            print(resp.text)

        quit()  # 終了

    

# =============================================
# 機能 : 保存してあるIDトークンを使い、財務情報を取得し、保存する。
# 引数1: 開始日 書式 from=[yyyymmdd] 
# 引数2: 終了日 書式 to=[yyyymmdd] 
# 返値 : 無し
# 備考 : 出力のファイル名、IDトークンを保存してあるファイル名は適宜変更してください。
#       1銘柄ごとの取得になります。
#       財務データが複数返されます（複数ある場合）。
# ---------------------------------------------

# 出力ファイル名
str_fname_output = 'jq_fins_statements_date.csv'

# ＩＤトークン保存ファイル名
str_fname_idtoken = 'jq_idtoken.json'

# ＩＤトークンの読み出し
str_idtoken = func_read_idtoken(str_fname_idtoken)
# IDトークン保存ファイルのデータ形式は、
#   {"time_idtoken":"value","idToken":"value"}


# 入力パラメーターの書き出し
for i in range(len(sys.argv)):
    print('sys.argv[', i,']:', sys.argv[i])
print()

# パラメーターチェック
func_parse_parameter(sys.argv, str_fname_output)

dic_argv = func_get_parameter(sys.argv)
date_from = dic_argv.get('from=')
date_to = dic_argv.get('to=')
print('dic_argv')
print('date_from:', date_from)
print('date_to:', date_to)
print()

# ファイルにタイトル行を書き込む
func_write_title(str_fname_output)

date_search = date_from
n = 0
# 財務情報取得
try:
    while date_to >= date_search :
        str_parameter = 'date=' + datetime.datetime.strftime(date_search.date(), '%Y%m%d')
        str_url = 'https://api.jpx-jquants.com/v1/fins/statements?' + str_parameter #+ '"'
        list_statements = func_query_api(str_idtoken, str_url)

        # 銘柄コード順にソート
        list_statements = sorted(list_statements, key=lambda x:x['LocalCode'])

        if len(list_statements) > 0 :
            with open(str_fname_output, 'a', encoding = 'utf_8') as fout:
                # データ行
                for i in range(len(list_statements)):
                    str_text = ''
                    str_text = str_text + '"' + list_statements[i].get('LocalCode') + '",'
                    str_text = str_text + '"' + list_statements[i].get('DisclosedDate') + '",'
                    str_text = str_text + '"' + list_statements[i].get('DisclosureNumber') + '",'
                    str_text = str_text + '"' + list_statements[i].get('ApplyingOfSpecificAccountingOfTheQuarterlyFinancialStatements') + '",'
                    str_text = str_text + '"' + list_statements[i].get('AverageNumberOfShares') + '",'
                    str_text = str_text + '"' + list_statements[i].get('BookValuePerShare') + '",'
                    str_text = str_text + '"' + list_statements[i].get('ChangesBasedOnRevisionsOfAccountingStandard') + '",'
                    str_text = str_text + '"' + list_statements[i].get('ChangesInAccountingEstimates') + '",'
                    str_text = str_text + '"' + list_statements[i].get('ChangesOtherThanOnesBasedOnRevisionsOfAccountingStandard') + '",'
                    str_text = str_text + '"' + list_statements[i].get('CurrentFiscalYearEndDate') + '",'
                    str_text = str_text + '"' + list_statements[i].get('CurrentFiscalYearStartDate') + '",'
                    str_text = str_text + '"' + list_statements[i].get('CurrentPeriodEndDate') + '",'
                    str_text = str_text + '"' + list_statements[i].get('DisclosedTime') + '",'
                    str_text = str_text + '"' + list_statements[i].get('DisclosedUnixTime') + '",'
                    str_text = str_text + '"' + list_statements[i].get('EarningsPerShare') + '",'
                    str_text = str_text + '"' + list_statements[i].get('Equity') + '",'
                    str_text = str_text + '"' + list_statements[i].get('EquityToAssetRatio') + '",'
                    str_text = str_text + '"' + list_statements[i].get('ForecastDividendPerShare1stQuarter') + '",'
                    str_text = str_text + '"' + list_statements[i].get('ForecastDividendPerShare2ndQuarter') + '",'
                    str_text = str_text + '"' + list_statements[i].get('ForecastDividendPerShare3rdQuarter') + '",'
                    str_text = str_text + '"' + list_statements[i].get('ForecastDividendPerShareAnnual') + '",'
                    str_text = str_text + '"' + list_statements[i].get('ForecastDividendPerShareFiscalYearEnd') + '",'
                    str_text = str_text + '"' + list_statements[i].get('ForecastEarningsPerShare') + '",'
                    str_text = str_text + '"' + list_statements[i].get('ForecastNetSales') + '",'
                    str_text = str_text + '"' + list_statements[i].get('ForecastOperatingProfit') + '",'
                    str_text = str_text + '"' + list_statements[i].get('ForecastOrdinaryProfit') + '",'
                    str_text = str_text + '"' + list_statements[i].get('ForecastProfit') + '",'
                    str_text = str_text + '"' + list_statements[i].get('MaterialChangesInSubsidiaries') + '",'
                    str_text = str_text + '"' + list_statements[i].get('NetSales') + '",'
                    str_text = str_text + '"' + list_statements[i].get('NumberOfIssuedAndOutstandingSharesAtTheEndOfFiscalYearIncludingTreasuryStock') + '",'
                    str_text = str_text + '"' + list_statements[i].get('NumberOfTreasuryStockAtTheEndOfFiscalYear') + '",'
                    str_text = str_text + '"' + list_statements[i].get('OperatingProfit') + '",'
                    str_text = str_text + '"' + list_statements[i].get('OrdinaryProfit') + '",'
                    str_text = str_text + '"' + list_statements[i].get('Profit') + '",'
                    str_text = str_text + '"' + list_statements[i].get('ResultDividendPerShare1stQuarter') + '",'
                    str_text = str_text + '"' + list_statements[i].get('ResultDividendPerShare2ndQuarter') + '",'
                    str_text = str_text + '"' + list_statements[i].get('ResultDividendPerShare3rdQuarter') + '",'
                    str_text = str_text + '"' + list_statements[i].get('ResultDividendPerShareAnnual') + '",'
                    str_text = str_text + '"' + list_statements[i].get('ResultDividendPerShareFiscalYearEnd') + '",'
                    str_text = str_text + '"' + list_statements[i].get('RetrospectiveRestatement') + '",'
                    str_text = str_text + '"' + list_statements[i].get('TotalAssets') + '",'
                    str_text = str_text + '"' + list_statements[i].get('TypeOfCurrentPeriod') + '",'
                    str_text = str_text + '"' + list_statements[i].get('TypeOfDocument') + '"\n'

                    fout.write(str_text)     
            fout.close
            print(str_parameter,' 銘柄数:', i + 1 )  # 0からカウントしているので1加算
        else :
            print(str_parameter,' 銘柄数: 0')
                  
        n = n + 1
        date_search = date_from + datetime.timedelta(days=n)


except IOError as e:
    print('Can not write!!!')
    print(type(e))
    #print(line)
