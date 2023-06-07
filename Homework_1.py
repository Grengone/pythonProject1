from selene import browser, be, have

browser.open('http://google.com')
browser.element('[name="q"]') .should(be.blank) .type('Grishanya') .press_enter()
browser.element('[id="search"]') .should(have.text('Grishanya'))