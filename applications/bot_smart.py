# accessing page n downloading PDFs..

import mechanize
import http.cookiejar as cookielib

browser = mechanize.Browser()

url = 'https://github.com/login'

user = 'seuemail@delogin'
password = 'suasenha'

# Prepare cookies
cj = cookielib.LWPCookieJar()
browser.set_cookiejar(cj)

# adjusting browser
browser.set_handle_equiv(True)
browser.set_handle_gzip(False)
browser.set_handle_redirect(True)
browser.set_handle_referer(True)
browser.set_handle_robots(False)
browser.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

browser.addheaders = [('User-agent', 'Mozilla/5.0 (X11;\
 U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615\
Fedora/3.0.1-1.fc9 Firefox/3.0.1')]      

# Prepare cookies
browser.open(url)
browser.select_form(nr=0)


# # return from form..
for f in browser.forms():
    print(f)

# for control in browser.form.controls:
#     print(control)
#     print(control.type)
#     print(control.name)

# typing the form

# browser.select_form(name="commit")

# browser.form['login'] = user
# browser.form['password'] = password

# browser.submit() 

# html = browser.response().read()

# print(html)