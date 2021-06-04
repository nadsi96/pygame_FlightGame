import pymysql
import pandas as pd
import numpy as np

class SingletonInstance:
    __instance = None
    
    @classmethod
    def __getInstance(cls):
        return cls.__instance
    
    @classmethod
    def instance(cls, *args, **kwargs):
        cls.__instance = cls(*args, **kwargs)
        cls.instance = cls.__getInstance
        return cls.__instance
    
class DB_Handler(SingletonInstance):
    def __init__(self):
        self.host = "localhost"
        port = "3306"
        self.database = "game_flight"
        self.username = "gameFlightuser"
        self.password = "1234qwerty!"
        self.score_table = "game_flight.scores"
        self.score_table_column_score = "score"
        return
    
    def create_Conn(self):
        conn = pymysql.connect(
                host = self.host,
                user = self.username,
                passwd=self.password,
                db=self.database,
                use_unicode=True,
                charset = "utf8")
        return conn
    
    # 게임 점수, 이름 저장
    def insert_Score(self, score=0, name=None):
        conn = self.create_Conn()
        query = """
                INSERT INTO {}
                VALUES(%s, %s)
                """.format(self.score_table)
        cursor = conn.cursor()
        cursor.execute(query, (score, name))
        
        conn.commit()
        conn.close()
        return
    
    # 게임 점수 상위 8개 찾아서 DataFrame으로 반환
    def get_Scores(self):
        conn = self.create_Conn()
        query = """SELECT *
                from {0}
                order by {1} desc
                limit {2}""".format(self.score_table, self.score_table_column_score, 8)
        cursor = conn.cursor()
        cursor.execute(query)
        
        score_datas = cursor.fetchall()
        df = pd.DataFrame(score_datas, columns=["Score", "Name"])
        df.index = list(range(1,df.shape[0]+1))
        conn.close()
        return df

if __name__ == "__main__":
    db_handler = DB_Handler.instance()
    df = db_handler.get_Scores()
#    db_handler.insert_Score(100)
#    df = db_handler.get_Scores()
    print(df)
    print(df.index)