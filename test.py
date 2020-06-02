from lxml import etree

file = open('fullhtml.txt', 'r')

tree = etree.HTML(file.read())

# <div class="D(tbr) fi-row Bgc($hoverBgColor):h" data-reactid="71">
locator = ".//div[@class='D(tbr) fi-row Bgc($hoverBgColor):h']"
# Wait until the URL changes to make sure we are getting the rigth HTML
statements = tree.findall(locator)

for statement in statements:
    name_statement = statement.findtext(".//div/div/span")

    # The logic below is used because some values are marked as '-'.
    # This changes the page structure
    value_element = statement.find(
                ".//div[@class='Ta(c) Py(6px) Bxz(bb) BdB Bdc($seperatorColor) Miw(120px) Miw(140px)--pnclg Bgc($lv1BgColor) fi-row:h_Bgc($hoverBgColor) D(tbc)']"
                )
    if len(value_element)==0:
        value_statement = value_element.text
    else:
        value_statement = value_element.findtext(".//span")
    
    print(name_statement + " " +value_statement)


