import os
import re

txt_dir = '../txt/'
css_path = '../src/songs.css'
js_path = '../src/index.js'
output_file = '../build/index.html'

CHORDS = ['DO', 'RE', 'MI', 'FA', 'SOL', 'LA', 'SI', 
          'DO7', 'RE7', 'MI7', 'FA7', 'SOL7', 'LA7', 'SI7', 
          'DOb', 'REb', 'MIb', 'FAb', 'SOLb', 'LAb', 'SIb',
          'DO#', 'RE#', 'MI#', 'FA#', 'SOL#', 'LA#', 'SI#',
          'DO#7', 'RE#7', 'MI#7', 'FA#7', 'SOL#7', 'LA#7', 'SI#7',]

# with open(css_file, 'r') as css:
#     css_content = css.read()

# with open(js_file, 'r') as js:
#     js_content = js.read()

with open(output_file, 'w') as html_file:
    html_file.write('<html>\n')
    html_file.write('<head>\n')
    html_file.write('<meta charset="UTF-8">\n')
    # html_file.write('<style>\n' + css_content + '\n</style>\n')
    html_file.write(f'<link rel="stylesheet" href="{css_path}">\n')
    html_file.write('<title>Songbook</title>\n')
    html_file.write('<link rel="preconnect" href="https://fonts.googleapis.com">')
    html_file.write('<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>')
    html_file.write('<link href="https://fonts.googleapis.com/css2?family=Source+Code+Pro:ital,wght@0,200..900;1,200..900&display=swap" rel="stylesheet">')
    html_file.write('</head>\n')
    html_file.write('<body>\n')
    html_file.write('<div id="container">\n') # container
    # html_file.write('<script>\n' + js_content + '\n</script>\n')
    html_file.write(f'<script src="{js_path}"></script>\n')
    for filename in os.listdir(txt_dir):
        if filename.endswith('.txt'):
            with open(os.path.join(txt_dir, filename), 'r') as txt_file:
                content = txt_file.read()
                html_page = '<div class="song">\n'
                lines = content.split('\n')
                for i, line in enumerate(lines):
                    if i == 0:
                        html_page += f'<div class="title">{line}</div>\n'
                        html_page += '<div class="lyrics">\n'
                        html_page += '<div class="verse">\n'
                        continue
                    if line.strip() == "":
                        html_page += '</div>\n'
                        html_page += '<div class="verse">\n'
                    for chord in CHORDS:
                        line = re.sub(rf'(?<!\w){chord}(?!\w)', f'<div class="chord">{chord}</div>', line)
                    if line:
                        html_page += f'<div class="line">{line}</div>\n'
                html_page += '</div>\n' # verse
                html_page += '</div>\n' # lyrics    
                html_page += '</div>\n' # song
            html_file.write(html_page)
    html_file.write('</div>\n') # container
    html_file.write('</body>\n</html>')