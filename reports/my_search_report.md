Запускаемый код из раздела 14 не сработал, ошибка:

```
...
During handling of the above exception, another exception occurred:

URLError                                  Traceback (most recent call last)
Cell In[45], line 5
      1 MY_TOPIC = "solar holes influence to ionosphere"                 # например: "perovskite solar cell degradation"
      2 MY_QUERIES = ["За какое время Солнечный ветер достигает Земли?", "Насколько велика площадь корональных дыр по отношению к площади Солнца", "Корреляция корональных дыр и электронного содержания ионосферы", "Виды солнечного ветра", "Изображения корональных дыр"]               # пять запросов к собранной библиотеке, например: ["что ускоряет деградацию", ...]
      3 
      4 if MY_TOPIC and MY_QUERIES:
----> 5     data, request = openalex_get("/works", search=MY_TOPIC, per_page=50, filter="has_abstract:true",
      6                                  select="id,doi,display_name,publication_year,cited_by_count,abstract_inverted_index")
      7 
      8     print(data)

Cell In[37], line 13
      9     public = f"{OPENALEX}{path}" + ("?" + urllib.parse.urlencode(params) if params else "")
     10     if OPENALEX_KEY:
     11         params = {**params, "api_key": OPENALEX_KEY}
     12     req = urllib.request.Request(f"{OPENALEX}{path}?{urllib.parse.urlencode(params)}", headers={"User-Agent": USER_AGENT})
---> 13     return json.loads(urllib.request.urlopen(req, timeout=60).read()), public

File ~/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/urllib/request.py:215, in urlopen(url, data, timeout, cafile, capath, cadefault, context)
    213 else:
    214     opener = _opener
--> 215 return opener.open(url, data, timeout)

File ~/.local/share/uv/python/cpython-3.12.13-linux-x86_64-gnu/lib/python3.12/urllib/request.py:515, in OpenerDirector.open(self, fullurl, data, timeout)
    512     req = meth(req)
    514 sys.audit('urllib.Request', req.full_url, req.data, req.headers, req.get_method())
--> 515 response = self._open(req, data)
    517 # post-process response
    518 meth_name = protocol+"_response"
```


В соответствующих переменных было указано:


```
MY_TOPIC = "solar holes influence to ionosphere"                 # например: "perovskite solar cell degradation"
MY_QUERIES = ["За какое время Солнечный ветер достигает Земли?", "Насколько велика площадь корональных дыр по отношению к площади Солнца", "Корреляция корональных дыр и электронного содержания ионосферы", "Виды солнечного ветра", "Изображения корональных дыр"]
```
