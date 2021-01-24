"""webapp/app.py
author          : nsuhara <na010210dv@gmail.com>
date created    : 2020/9/18
python version  : 3.7.3
"""
import os

from flask import Flask

app = Flask(__name__)


@app.route('/test')
def hello():
    """hello
    """
    return '単語計算機'


def main():
    """main
    """
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', '5000'))
    app.run(host=host, port=port)


if __name__ == '__main__':
    main()
