import os
import sqlite3

cookie_file = os.path.expanduser('~/Library/Application Support/Google/Chrome/Default/Cookies')


def query_cookies():
    with sqlite3.connect(cookie_file) as conn:
        result = conn.execute(
            "SELECT encrypted_value FROM cookies WHERE host_key = '.sankuai.com'").fetchall()
    return result

res = query_cookies()

print(res)
for k in res:
    print(k)
