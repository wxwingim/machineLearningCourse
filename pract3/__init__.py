from bs4 import BeautifulSoup as bs
import codecs
import requests

def main():
    doc = bs(codecs.open('markes', encoding='utf-8', mode='r').read(), 'html.parser')

    name = doc.select('.product__title')[0].decode_contents().strip()
    tags = list(map(lambda x: x.decode_contents().strip(), doc.select('a.product__seria')))

    print('book name: ', name)
    print('tags: ', tags)


    comments = []
    # for node in doc.select('section.review-list div.review-item'):
    for node in doc.select('section.review-list div.review-item'):
        text = node.select('p.review__text')[0].decode_contents().strip()
        author = node.select('.review__author')[0].decode_contents().strip()
        rating = -1
        popular = int(node.select('div.review__voting_stat span')[1].decode_contents().strip())
        try:
            rating_str = node.select('.total-rating')[0].decode_contents().strip()
            rating = int(rating_str[8])
        except: Exception
            # rating = -1

        comments.append({'text': text, 'rating': rating, 'author': author, 'popular': popular})

    # вывод информации по комментариям
    print('Комментариев в статье: ', len(comments))
    print('Самый большой комментарий:', sorted(comments, key=lambda x: len(x['text']))[len(comments)-1]['text'])


    most_popular = sorted(comments, key=lambda x: x['popular'], reverse=True)[0]
    print('Самый популярный комментарий:', most_popular['text'], '\nПопулярность ', most_popular['popular'])


    # print(comments[0])

if __name__ == '__main__':
    main()