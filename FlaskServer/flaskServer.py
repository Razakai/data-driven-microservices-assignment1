from flask import Flask, render_template, Response
import logging
import time
from database.queries import getData

app = Flask(__name__)


@app.route('/')
def index():
    data = getData()
    return f"""
    <table>
        <tr>
            <th>Average Number Words Per Post</th>
            <th>Post with Most Words</th>
            <th>Author Most Deleted Posts</th>
            <th>Average Word Length - 3 Min</th>
        </tr>
        <tr>
            <td>{data[0][1]}</td>
            <td>{data[0][2]}</td>
            <td>{data[0][3]}</td>
            <td>{data[0][4]}</td>
        </tr>
    </table>
    """



if __name__ == '__main__':
    app.run(host='0.0.0.0', threaded=True)