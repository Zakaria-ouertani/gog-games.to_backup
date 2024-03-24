from json import loads
from pathlib import Path
from sys import argv
import os


def make_game_page(json_filename, json_path):
    html_file = open(json_path + "html\\" + "all\\" + json_filename[0:json_filename.rfind(".")] + ".html", "w", encoding = "utf8")
    json_file = open(json_path + json_filename, 'r', encoding = "utf8")
    parsed_json = loads(json_file.read())
    html_file.write('<!DOCTYPE html>\n')
    html_file.write('<html lang="en">\n')
    html_file.write('<head>\n')
    html_file.write('    <meta charset="UTF-8">\n')
    html_file.write('    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
    html_file.write('    <title>Document</title>\n')
    html_file.write('    <link rel="stylesheet" href="../style.css">\n')
    html_file.write('</head>\n')
    
    game_title = parsed_json["MSG"]["title"]
    game_id = parsed_json["MSG"]["id"]
    game_link_official = parsed_json["MSG"]["url"];
    game_category = parsed_json["MSG"]["category"]
    game_dev = parsed_json["MSG"]["developer"]
    html_file.write(f'<h1>{game_title}</h1><a href="{game_link_official}">Buy</a>')
    html_file.write(f'<p>{game_category} | {game_dev}</p>')
    html_file.write('<div id="div_game_links">')
    html_file.write('<h1>Game Download Links</h1>')
    for link in parsed_json["MSG"]["links"]["GAME"]:
        html_file.write(f"<a href={link["links"][0]["link"]}>{link["name"]}</a><br>")
    html_file.write('</div>')

    html_file.write('<div id="div_goodies_links">')
    html_file.write('<h1>Goodies Download Links</h1>')
    for link in parsed_json["MSG"]["links"]["GOODIES"]:
        html_file.write(f"<a href={link["links"][0]["link"]}>{link["name"]}</a><br>")
    
    html_file.write('</div>')
    
    html_file.write('<div id="div_patches_links">')
    html_file.write('<h1>Patch/Other Downloads</h1>')
    for link in parsed_json["MSG"]["links"]["PATCHES"]:
        html_file.write(f"<a href={link["links"][0]["link"]}>{link["name"]}</a><br>")
        html_file.write('<div id="div_game">')
    html_file.write('</div>')

    html_file.write('<hr>')
    if parsed_json["MSG"]["files"] != False:
        html_file.write('<h1>Game Items Included</h1>')
        for name in parsed_json["MSG"]["files"]["GAME"]:
            html_file.write(f"<p> {name["name"]}</p><br>")
        html_file.write('</div>')

        html_file.write('<div id="div_goodies">')
        html_file.write('<h1>Goodies Included</h1>')
        for name in parsed_json["MSG"]["files"]["GOODIES"]:
            html_file.write(f"<p>href={name["name"]}</p><br>")

        html_file.write('</div>')

        html_file.write('<div id="div_patches">')
        html_file.write('<h1>Patch/Other Items Included</h1>')
        for name in parsed_json["MSG"]["files"]["PATCHES"]:
            html_file.write(f"<>{name["name"]}</p><br>")

        html_file.write('</div>')
    html_file.write('</body>\n')
    html_file.write('</html>')
    return [game_title, game_id]

files = os.listdir(argv[1])
index = open(argv[1] + "html\\index.html", "w", encoding="utf8")
index.write('<!DOCTYPE html>\n')
index.write('<html lang="en">\n')
index.write('<head>\n')
index.write('    <meta charset="UTF-8">\n')
index.write('    <meta name="viewport" content="width=device-width, initial-scale=1.0">\n')
index.write('    <title>Document</title>\n')
index.write('    <link rel="stylesheet" href="style.css">\n')
index.write('</head>\n')
index.write('<script src="script.js"></script>')
index.write('<input type="text" onkeypress="search()" id="searchbar">')
for file_name in files:
    if os.path.isfile(argv[1] + file_name):
        title, id = make_game_page(file_name, argv[1])
        index.write('<div class="list_item">')
        index.write(f'<img src="../img/" placeholder="test">')
        index.write(f'<a href="{"all/" + file_name[0:file_name.rfind(".")] + ".html"}">{title}</a>')
        index.write("</div>")
index.write('</body>\n')
index.write('</html>')
