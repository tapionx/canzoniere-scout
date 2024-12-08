import os
import re

txt_dir = '../txt/'
css_file = 'songs.css'
js_file = 'index.js'
output_file = '../build/index.html'

CHORDS = ['DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI']

with open(css_file, 'r') as css:
    css_content = css.read()

with open(js_file, 'r') as js:
    js_content = js.read()

with open(output_file, 'w') as html_file:
    html_file.write('<html>\n')
    html_file.write('<head>\n')
    html_file.write('<style>\n' + css_content + '\n</style>\n')
    html_file.write('<title>Songbook</title>\n')
    html_file.write('</head>\n')
    html_file.write('<body>\n')
    html_file.write('<script>\n' + js_content + '\n</script>\n')
    for filename in os.listdir(txt_dir):
        if filename.endswith('.txt'):
            with open(os.path.join(txt_dir, filename), 'r') as txt_file:
                content = txt_file.read()
                html_page = '<div class="song">\n'
                lines = content.split('\n')
                for i, line in enumerate(lines):
                    if i == 0:
                        html_page += f'<div class="title">{line}</div>\n'
                        continue
                    for chord in CHORDS:
                        line = re.sub(rf'(?<!\w){chord}(?!\w)', f'<div class="chord">{chord}</div>', line)
                    html_page += f'<div class="line">{line}</div>\n'
                html_page += '</div>\n'
            html_file.write(html_page)
    html_file.write('</body>\n</html>')