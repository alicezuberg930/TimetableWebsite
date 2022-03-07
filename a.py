from flask import Flask, render_template, request, url_for
# from get_truyen import TimetableArray
from os import name
from requests_html import HTMLSession
import io
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        student_id = request.form['student_id']
        url = "http://thongtindaotao.sgu.edu.vn/Default.aspx?page=thoikhoabieu&sta=1&id=" + student_id
        session = HTMLSession()
        r = session.get(url)
        Schedule = r.html.find("div.grid-roll2", first=True)
        TimetableArray = []
        file = open("timetable.txt", "w")
        file.close()
        with io.open("timetable.txt", 'a', encoding='utf8') as f:
            f.write(Schedule.text)
        with io.open("timetable.txt", 'r', encoding='utf-8') as f:
            lines = f.readlines()
        f.close()
        for l in lines:
            if 'Ghi chú' in l:
                break
            if 'DSSV' in l or '123456789012345' in l:
                pass
            else:
                TimetableArray.append(l.strip())
        return render_template("timetable.html", TimeTableList=TimetableArray)
    else:
        return render_template("timetable.html")


if __name__ == "__main__":
    app.run(debug=True)
