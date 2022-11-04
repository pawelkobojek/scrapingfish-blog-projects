from xml.etree import ElementTree

selected_category = "976759"  # Food

root = ElementTree.parse("sitemap_browse_fst.xml").getroot()

urls = set()
for url in root:
    urls.add(url[0].text)

food_category_codes = set()
for url in urls:
    category_code = url.split("/")[-2]
    if category_code.startswith(selected_category):
        food_category_codes.add(category_code)

final_food_category_codes = set()
for code in sorted(food_category_codes, key=len, reverse=True):
    if not any([c.startswith(code) for c in final_food_category_codes]):
        final_food_category_codes.add(code)

browse_urls = []
for code in sorted(final_food_category_codes):
    browse_urls.append(f"https://www.walmart.com/browse/{code}")

with open("category_urls.txt", "w") as f:
    f.write("\n".join(browse_urls))
