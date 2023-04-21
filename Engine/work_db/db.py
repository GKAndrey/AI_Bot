import sqlite3
import os as osis

PATH = osis.path.abspath(__file__ + '\..')
print(PATH)
conn = sqlite3.connect(osis.path.join(PATH, 'db.db'))
cur = conn.cursor()

if __name__ == '__main__':
    try:
        sql_u = '''
        CREATE TABLE base(
        num_mess int,
        mess str,
        good_bad int,
        type_answ string
        );'''
        cur.execute(sql_u)
    except sqlite3.OperationalError:
        sql_u = '''
        DELETE FROM base;
        '''
        cur.execute(sql_u)
        conn.commit()


def save_mess(mess):
    pass


def load_mess_list(mess):
    pass