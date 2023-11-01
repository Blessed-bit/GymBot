import sqlite3
from handlers import *


async def start_db(_):
    global db, cur
    db = sqlite3.connect('sub.db')
    cur = db.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
       userid INT PRIMARY KEY,
       weight int,
       height int,
       bench_press int,
       deadlift int,
       squat int)
    """)
    db.commit()


async def stop_dp(_):
    db.close()


async def create_profile(userid):
    cur.execute("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?);", (userid, 0, 0, 0, 0, 0))
    db.commit()


async def check_user_in_db(userid):
    user = cur.execute(f"SELECT * FROM users WHERE userid == {userid}").fetchone()
    return not user


async def bench_press(userid, bench):
    cur.execute(f"UPDATE users SET bench_press = ? WHERE userid = ?", (bench, userid))
    db.commit()


async def squat(userid, squat):
    cur.execute(f"UPDATE users SET squat = ? WHERE userid = ?", (squat, userid))
    db.commit()


async def deadlift(userid, deadlift):
    cur.execute(f"UPDATE users SET deadlift = ? WHERE userid = ?", (deadlift, userid))
    db.commit()


async def add_weight(weight, userid):
    cur.execute(f"UPDATE users SET weight = ? WHERE userid = ?", (weight, userid))
    db.commit()


async def add_height(height, userid):
    cur.execute(f"UPDATE users SET height = ? WHERE userid = ?", (height, userid))
    db.commit()


def show_weight(userid):
    result = cur.execute(f"SELECT weight FROM users WHERE userid = {userid};").fetchone()
    return result[0]


def show_height(userid):
    result = cur.execute(f"SELECT height FROM users WHERE userid = {userid};").fetchone()
    return result[0]


def show_bench_press(userid):
    result = cur.execute(f"SELECT bench_press FROM users WHERE userid = {userid};").fetchone()
    return result[0]



def show_deadlift(userid):
    result = cur.execute(f"SELECT deadlift FROM users WHERE userid = {userid};").fetchone()
    return result[0]


def show_squat(userid):
    result = cur.execute(f"SELECT squat FROM users WHERE userid = {userid};").fetchone()
    return result[0]


if __name__ == "__main__":
    start_db()