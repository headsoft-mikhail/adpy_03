## Решение [домашнего задания](https://github.com/netology-code/py-homeworks-advanced/tree/master/6.Web-scrapping) к лекции «Web-scrapping»
  1. При выполнении домашнего задания пользовался библиотеками requests - для получения html-кода и BeautifulSoup-для поиска нужных элементов в нем.
  1. Реализован класс Post, в экземпляры которого сохраняются собранные данные. В классе реализован метод __str__ для вывода в терминал в нужном формате, а также show_all - расширенный вывод вместе с текстом поста. 
  1. Метод get_compare_words формирует список слов для поиска совпадений. Для этого используются регулярные выражения и библиотека re. В зависимости от выставленных флагов будут использоваться соответствующие части поста. При выборе include_content=True также используется и полная версия статьи, если она предварительно получена в методе get_post_data с флагом extended_content=True
  1. В метод find передается не только список слов, но и имя функции для поиска совпадений, а также флаги используемых частей статьи (хабы, заголовок, текст)
  1. Для упрощенного поиска - реализован метод intersection, для более продвинутого - метод levenstein, рассчитывающий расстояние Левенштейна.
  1. Убавило скорость выполнения задания обновление сайта: вчера почти все было выполнено, а сегодня сайт обновился и нужно переделывать.

  ## Решение [домашнего задания](https://github.com/netology-code/py-homeworks-advanced/tree/master/3.Decorators) к лекции «Decorators»
  1. В новой ревизии был добавлен файл [main_decorator.py](https://github.com/headsoft-mikhail/adpy_03/blob/master/main_decorator.py), в котором реализованы три декоратора: 
  * logged - требуемый по заданию декоратор для логгирования, принимающий в качестве аргумента путь к файлу (например папка 'logs'), само название файла - фиксированное:  log.txt
  * delayed - выполняет декорированную функцию после задержки заданной длительности
  * repeated - повторяет выполнение декорированной функции заданное количество раз
  1. К проекту также приложен файл записанных логов [log.txt](https://github.com/headsoft-mikhail/adpy_03/blob/master/logs/log.txt)
  1. logged декорирует большинство функций приложения, а функция get_request декорирована всеми тремя реализованными декораторами для выполнения запросов с интервалом и логированием