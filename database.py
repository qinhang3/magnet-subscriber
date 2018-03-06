import sqlite3
import time


def get_nodes(keyword=None):
    conn = sqlite3.connect('example.db')
    try:
        c = conn.cursor()
        if keyword is None:
            c.execute('SELECT * FROM torr')
        else:
            c.execute('SELECT * FROM torr where keyword = ?', (keyword, ))
        datas = c.fetchall()
        list = []
        for node in datas:
            list.append({'keyword': node[0], 'sup': node[1], 'title': node[2], 'detail': node[3], 'attr': node[4], 'magnet': node[5]})
        return list
    finally:
        conn.close()


def save_nodes(nodes, keyword):
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute("delete from torr where keyword = ?", (keyword, ))
    for node in nodes:
        para = (keyword, node.sup, node.title, node.titleHref, node.attr, node.magnet, get_time(), 0)
        c.execute("INSERT INTO torr VALUES(?,?,?,?,?,?,?,?)", para)
    conn.commit()
    conn.close()


def get_time():
    t = time.gmtime()
    return "%d-%02d-%02d %02d:%02d:%02d" % (t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour + 8, t.tm_min, t.tm_sec)


def add_task(username, name, magnet=''):
    conn = sqlite3.connect('example.db')
    try:
        c = conn.cursor()
        result = c.execute('update task set magnet = ?, gmt_modified = ?,delete_mark = 0 where keyword = ?'
                           ' and user_name = ?', (magnet, get_time(), name, username))
        print(result.rowcount)
        if result.rowcount == 0:
            c.execute("INSERT INTO task values(?, ?, ?, ?, ?, ?)", (name, '', get_time(), get_time(), 0, username))
            conn.commit()
            return "inserted."
        else:
            conn.commit()
            return "updated."
    finally:
        conn.close()


def get_tasks(username, offset=0, count=100):
    conn = sqlite3.connect('example.db')
    try:
        c = conn.cursor()
        c.execute("select * from task where delete_mark = 0 and user_name = ? order by gmt_create desc limit ?, ?", (username, offset, count))
        datas = c.fetchall()
        list = []
        for data in datas:
            list.append({'keyword': data[0], 'magnet': data[1], 'gmt_create': data[2]})
        return list
    finally:
        conn.close()


def delete_task(username, name):
    conn = sqlite3.connect('example.db')
    try:
        c = conn.cursor()
        c.execute("update task set delete_mark = 1 where keyword = ? and user_name = ?", (name, username))
        conn.commit()
    finally:
        conn.close()
