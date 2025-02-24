"""codestyle"""
import requests

class APIError(Exception):
    """API 呼び出し中に発生したエラーを処理する例外"""

def call_api(url):
    """API"""
    try:
        response = requests.get(url, timeout=5)
        # 応答コードが 200 でない場合、詳細なエラーメッセージを出力
        if response.status_code != 200:
            raise APIError(f"API 呼び出し失敗{response.status_code}, {response.text}")
        # API 応答データの処理
        return response.json()
    except requests.exceptions.RequestException as e:
        # ネットワークエラーまたはタイムアウトエラーを処理
        raise APIError(f"API リクエスト中にエラーが発生しました: {e}") from e


def main():
    """メイン処理"""
    url = "https://api.example.com/data"  # API URL
    try:
        data = call_api(url)
        print("API Response:", data)
    except APIError as e:
        print(f"API Error: {e}")

#----Generatorを利用して、大量のデータをループする時にメモリの節約ができる。
def t():
    """テスト用関数"""
    num = []
    for i in range(10):
        num.append(i)
    return num

def t_generator():
    """テスト用関数 (Generator)"""
    for i in range(10):
        yield i 



if __name__ == "__main__":
    for i in t():
        print(i)

    for i in t_generator():
        print(i)

    #main()


