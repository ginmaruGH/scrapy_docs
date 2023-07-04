import sqlite3


class BooksSqlitePipeline:
    def open_spider(self, spider) -> None:
        # データベースの作成と接続
        self.connection = sqlite3.connect("book_online.db")
        # Create cursor
        self.cursor = self.connection.cursor()
        # booksテーブルが存在しない場合は作成する
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS books(
                id INTEGER PRIMARY KEY,
                title TEXT,
                price TEXT,
                detail_page_url TEXT
            )"""
        )

    def process_item(self, item, spider):
        # titleがすでにテーブルにあるかどうかをチェックする
        # check_title = item["title"]
        res = self.cursor.execute("SELECT title FROM books WHERE title = ?", (item["title"],))
        result = res.fetchone()

        # テーブルにある場合は、ログメッセージを作成する
        if result:
            spider.logger.warn("Item already in table: %s" % item["title"])
        # テーブルにtitleがない場合、データを挿入する
        else:
            # insertステートメントの定義
            self.cursor.execute(
                """INSERT INTO books (title, price, detail_page_url) VALUES (?, ?, ?)""",
                (
                    item["title"],
                    item["price"],
                    item["detail_page_url"]
                )
            )
            # テーブルへのデータ挿入の実行
            self.connection.commit()

        return item

    def close_spider(self, spider):
        self.connection.close()
