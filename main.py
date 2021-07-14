from bs4 import BeautifulSoup
import requests
import re
import nltk


class Post:
    def __init__(self):
        self.title = ''
        self.link = ''

        self.time = ''
        self.content = ''
        self.full_content = ''
        self.hubs = []

    def __str__(self):
        string = f'#{self.id} опубликован {self.time} "{self.title}" {self.link}\n'
        return string

    def show_all(self):
        string = self.__str__()
        for item in self.hubs:
            string += item + "\n"
        string += self.content + "___________________________\n"
        print(string)

    def get_compare_words(self, include_hubs=True, include_title=True, include_content=True, ):
        compare_words = []
        if include_hubs:
            compare_words += self.hubs
        if include_title:
            compare_words += self.title.strip().split(' ')
        if include_content:
            compare_words += re.findall(r'\w+\-?\w*', self.content.strip())
            compare_words += re.findall(r'\w+\-?\w*', self.full_content.strip())
        compare_words = set([item.strip().lower() for item in compare_words])
        return compare_words

    def find(self, checklist, compare_func, include_hubs=True, include_title=True, include_content=True):
        words_available = self.get_compare_words(include_hubs=include_hubs,
                                                 include_title=include_title,
                                                 include_content=include_content)
        checklist = set([re.sub(r'[!|:|;|\?|\.|,]]', '', word.lower()) for word in checklist])

        intersection = compare_func(checklist, words_available)
        if len(intersection) > 0:
            print(f"Совпадение в посте #{self.id}: {intersection}")
            return True
        else:
            return False


def intersection(checklist, words_available):
    return set(checklist).intersection(words_available)


def levenstein(checklist, words_available):
    intersection = []
    levenstein_threshold = 0.2
    for question in words_available:
        for replica in checklist:
            distance_weighted = nltk.edit_distance(question, replica) / len(question)
            if distance_weighted <= levenstein_threshold:
                if replica not in intersection:
                    intersection.append(replica)
    return intersection


def get_post_data(post, extended_content=True):
    p = Post()
    p.id = post.attrs.get('id')
    p.time = post.find('span', class_='tm-article-snippet__datetime-published').text
    p.title = post.find('h2', class_='tm-article-snippet__title_h2').text
    p.link = 'https://habr.com' + post.find('a', class_='tm-article-snippet__title-link').attrs.get('href')
    if extended_content:
        response = requests.get(p.link)
        if response.status_code != 200:
            print(f"Error {response.status_code}")
        else:
            full_post = BeautifulSoup(response.text, "html.parser")
            p.full_content = full_post.find('div', class_='article-formatted-body').text
    p.content = post.find('div', class_='article-formatted-body').text
    post_hubs = post.find_all('a', class_='tm-article-snippet__hubs-item-link')
    for hub in post_hubs:
        p.hubs.append(hub.text)
    return p


if __name__ == '__main__':
    KEYWORDS = ['OVH', 'linux', 'фото', 'ERP-консалтинг', 'python', 'обучение', 'S7-300', 'VUI-команды']

    response = requests.get("https://habr.com/ru/all/")
    if response.status_code != 200:
        print(f"Error {response.status_code}")
    else:
        soup = BeautifulSoup(response.text, "html.parser")
        posts = soup.find_all('article', class_='tm-articles-list__item')
        for post in posts:
            p = get_post_data(post, extended_content=False)
            if p.find(KEYWORDS, levenstein, include_hubs=True, include_title=True, include_content=True):
                print(p)
