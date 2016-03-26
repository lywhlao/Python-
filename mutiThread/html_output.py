class HtmlOuter(object):
    #
    def __init__(self):
        self.datas = []

    def collect_data(self, new_data):
        if new_data is None:
            return
        self.datas.append(new_data)

    def output_html(self):
        fout = open(r'c:\output.html', 'a')
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table>")
        for data in self.datas:
            if 'url' not in data or 'title' not in data or 'summary' not in data:
                continue
            fout.write("<tr>")
            fout.write("<td>%s</td>" % data['url'].encode('utf-8'))
            fout.write("<td>"  "</td>")
            fout.write("<td>%s</td>" % data['title'].encode('utf-8'))
            fout.write("<td>"  "</td>")
            fout.write("<td>%s</td>" % data['summary'].encode('utf-8'))
            fout.write("</tr>")
        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

    def get_data_length(self):
        return len(self.datas)
