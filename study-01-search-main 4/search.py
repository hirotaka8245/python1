
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
import pandas as pd
df = pd.read_csv("/Users/mac/Downloads/study-01-search-main 4/source.csv",encoding="utf-8")
source=list(df["name"])

### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    ### ここに検索ロジックを書く
    if word in source:
        print("{}は存在します".format(word))    
    else:
        print("{}は存在しません".format(word))
        source.append(word)
        print("{}をデータに追加しました".format(word))

        df=pd.DataFrame(source,columns=["name"])
        df.to_csv("/Users/mac/Downloads/study-01-search-main 4/source.csv",encoding="utf_8-sig")
        print(source)

if __name__ == "__main__":
    search()
