import azure.functions as func
import requests
from bs4 import BeautifulSoup
import json

app = func.FunctionApp()

DEFAULT_URL = "https://quotes.toscrape.com/"


@app.route(route="GetQuotes", auth_level=func.AuthLevel.ANONYMOUS)
def get_quotes(req: func.HttpRequest) -> func.HttpResponse:

    # 1️⃣ 取得 query param / url
    url = req.params.get("url")

    if not url:
        try:
            req_body = req.get_json()
        except Exception:
            req_body = None

        if req_body:
            url = req_body.get("url")

    # 2️⃣ 預設網址
    if not url:
        url = DEFAULT_URL

    try:
        # 3️⃣ request 網頁
        res = requests.get(url, timeout=10)
        res.raise_for_status()

        soup = BeautifulSoup(res.text, "html.parser")

        quotes = soup.select(".quote")

        results = []

        for q in quotes:
            text = q.select_one(".text")
            author = q.select_one(".author")
            tags = q.select(".tags .tag")

            results.append({
                "text": text.get_text() if text else None,
                "author": author.get_text() if author else None,
                "tags": [t.get_text() for t in tags] if tags else []
            })

        # 4️⃣ 回傳 JSON
        return func.HttpResponse(
            json.dumps(results, ensure_ascii=False, indent=2),
            mimetype="application/json",
            status_code=200
        )

    except Exception as e:
        return func.HttpResponse(
            json.dumps({
                "error": str(e),
                "url": url
            }, ensure_ascii=False),
            mimetype="application/json",
            status_code=500
        )