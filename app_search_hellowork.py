from flask import Flask, render_template, request, redirect, url_for, Blueprint
from flask_sqlalchemy import SQLAlchemy
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import chromedriver_binary
import time
from bs4 import BeautifulSoup
import csv
import pandas as pd
import datetime as dt
import uuid


search_hellowork = Blueprint('app_search_hellowork', __name__)


@search_hellowork.route('/results', methods=['POST'])
def results():
    if request.method == 'POST':
        # POSTから受け取り
        age = int(request.form.get('age'))
        place_list = []
        place_list = request.form.getlist('place')
        place_list = list(map(int, place_list))
        place_list.extend([0, 0, 0, 0, 0])
        pref = format(place_list[0], '05')[:2]
        
        classfication_list = []
        classfication_list = request.form.getlist('classfication')
        classfication_list = list(map(str, classfication_list))
        classfication_list.extend([0, 0, 0])

        free_word = request.form.get('free_word')
        free_word = free_word.replace(' ', '　')# 空白を全角に置換

        # 検索
        # ハローワーク求人情報検索ページ
        HELLOWORK_URL = "https://www.hellowork.mhlw.go.jp/kensaku/GECA110010.do?action=initDisp&screenId=GECA110010"

        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(HELLOWORK_URL)
        time.sleep(1)

        # 求人区分
        driver.find_element_by_id("ID_ippanCKBox1").click()
        time.sleep(1)

        #年齢
        element = driver.find_element_by_id("ID_nenreiInput")
        element.send_keys(age)
        time.sleep(1)

        #就業場所 都道府県
        element = driver.find_element_by_id("ID_tDFK1CmbBox")
        Select(element).select_by_value(pref)
        time.sleep(1)

        # 就業場所 市区町村
        if any(place_list) != 0:
            buttons = driver.find_elements_by_css_selector("input.button")
            buttons[1].click()
            time.sleep(1)
            element = driver.find_element_by_id("ID_rank1CodeMulti")

        # リスト内の数字が0以外の時 for文で入力
        for place_list_num in place_list:
            if place_list_num > 0:
                place_list_num = f'{place_list_num:05}' 
                Select(element).select_by_value(place_list_num)
                
        time.sleep(1)
        driver.find_element_by_id("ID_ok").click()
        time.sleep(1)

        # 職業分類 
        # 入力箇所を選択するための変数を定義
        classfication_list_count = 1

        # リスト内の数字が0以外の時 for文で入力
        for classfication_list_num in classfication_list:
            # 小分類まで含めた5桁の時
            if classfication_list_num != 0 and len(classfication_list_num) > 4 :
                element = driver.find_element_by_id("ID_sKGYBRUIJo{}".format(classfication_list_count))
                element.send_keys(classfication_list_num[0] + classfication_list_num[1] + classfication_list_num[2])
                time.sleep(1)
                element = driver.find_element_by_id("ID_sKGYBRUIGe{}".format(classfication_list_count))
                element.send_keys(classfication_list_num[3] + classfication_list_num[4])
                classfication_list_count += 1
                time.sleep(1)
            # 大分類のみの3桁の時
            elif classfication_list_num != 0 :
                element = driver.find_element_by_id("ID_sKGYBRUIJo{}".format(classfication_list_count))
                element.send_keys(classfication_list_num)
                classfication_list_count += 1
                time.sleep(1)


        # 雇用形態 正社員
        driver.find_element_by_id("ID_koyoFltmCKBox1").click()
        time.sleep(1)

        # フリーワード
        driver.find_element_by_id("ID_freeWordRadioBtn0").click()
        time.sleep(1)
        element = driver.find_element_by_id("ID_freeWordInput")
        element.send_keys(free_word)
        time.sleep(1)

        # 「検索」をクリック
        driver.find_element_by_id("ID_searchBtn").click()
        time.sleep(2)

        # 「表示件数」ドロップダウンリスト 「50件」
        element = driver.find_element_by_id("ID_fwListNaviDispTop")
        Select(element).select_by_value("50")
        time.sleep(1)

        # データ収集
        # データを格納するリストを作成
        data = []
        url_list = []


        while True:
            # HTMLを整形して求人を抜き出す
            source = driver.page_source
            soup = BeautifulSoup(source, "html.parser")
            cases = soup.find_all("table", attrs={"class": "kyujin"})

            for case in cases:
                case_list = {} # 1件ごとに辞書を作成し、要素を格納する

                # 職種
                case_name = str(case.find("td", attrs={"class": "m13"}).text.strip())
                case_list['職種'] = case_name

                # kyujin_bodyタグ内の各要素抜き出し
                category_items = case.find_all("tr", attrs={"class": "border_new"})

                # 各要素リスト化 賃金は例外的に処理する
                for case_count,category_item in enumerate(category_items, 1):
                    if str(category_item) in "disp_inline_block width15em":
                        continue
                    category = str(category_item.find('div').text)
                    case_list[case_count] = category

                # 賃金
                category = category_items[5].find("div", attrs={"class": "disp_inline_block width15em"}).text
                case_list['賃金'] = category

                # URL
                case_url = case.find("div", attrs={"class": "flex jus_end"})
                a_tag = case_url.select_one('a[href]')
                href = str(a_tag.get('href'))
                url_list.append("https://www.hellowork.mhlw.go.jp/kensaku" + href.replace(".", "", 1))
                case_list['URL'] = "https://www.hellowork.mhlw.go.jp/kensaku" + href.replace(".", "", 1)

                # リスト(data)に辞書(case_list)を追記する
                data.append(case_list)

            # 次へボタンを探す
            next_btn = soup.find_all("input", attrs={'name': 'fwListNaviBtnNext'})

            # 次へボタンのタグがdisableされていなければ 
            if not 'disabled' in str(next_btn):
                driver.find_element_by_xpath("//input[@value='次へ＞']").click()

            # disableされている場合は終了
            else:
                driver.quit()
                break


        # データ処理
        # リスト(data)をpandasのデータフレームに変換
        df = pd.DataFrame(data)


        # 不要な列,空白の削除
        df = df.drop(columns=df.columns[1])
        df = df.drop(columns=df.columns[2])
        df = df.drop(columns=df.columns[3])
        df = df.drop(columns=df.columns[3])
        df = df.drop(columns=df.columns[4])
        df = df.drop(columns=df.columns[4])
        df = df.drop(columns=df.columns[5])
        df = df.replace('\n''\t', '', regex=True)

        # 列のリネーム
        df = df.rename(columns={ 
        2: '事業所名', 
        4: '仕事の内容',
        6: '賃金', 
        7: '就業時間', 
        10: '求人番号' 
        })

        # 列の並び替え
        df = df.reindex(columns=[
        '求人番号',
        '職種',
        '仕事の内容',
        '賃金',
        '就業時間',
        '事業所名',
        'URL'
        ])
        
        # CSVの保存
        csv_id = str(uuid.uuid4())
        now = dt.datetime.now()
        today = now.strftime('%Y%m%d')
        df.to_csv('./output/{}.csv'.format(csv_id), encoding='utf_8_sig',index=False)
        csv_path = './output/{}.csv'.format(csv_id)

        # tableに出力するためにURLをリンク
        df = df.drop(columns=df.columns[6])
        df_values = df.values.tolist()
        i = 0
        for df_value in df_values:
            df_values[i][0] = '<a href="' + url_list[i] + '">' + df_values[i][0]  + '</a>'
            i += 1

        return render_template('results.html', df_values = df_values, csv_path = csv_path, today = today)

    else:
        return redirect('hellowork.html')