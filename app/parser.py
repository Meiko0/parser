from bs4 import BeautifulSoup

html_text = """
<div class="cake-card">
    <h2 class="cake-name"> Наполеон</h2>
    <span class="cake-price">1200</span>
</div>  
"""

soup = BeautifulSoup(html_text, 'html.parser')

cena = soup.find('span', class_="cake-price")

if cena:
    print(cena.text)
else:
    print("Элемнета нет")

