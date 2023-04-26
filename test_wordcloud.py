"""
https://amueller.github.io/word_cloud/generated/wordcloud.WordCloud.html#wordcloud.WordCloud

https://www.datacamp.com/tutorial/wordcloud-python
"""
import numpy as np
import pandas as pd
from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt



my_words_dict = {'Python ': 200,
                 'SQL ': 50,
                 'Git ': 30,
                 #
                 'English ': 90,
                 'Spanish ': 70,
                 'Italian ': 50,
                 'Portuguese ': 100,
                 #
                 'Team-Work ': 100,
                 'Self-Motivated ': 100,
                 'Self-learner ': 100,
                 'Comunication ': 90
}

my_words_string = ''
for word, experience in my_words_dict.items():
    my_words_string = my_words_string + (word * experience)
# my_words = ('Python '* 100 + 'English ' * 90 + 'Spanish ' * 70 \
#             + 'Italian ' * 50 + 'SQL ' * 60 \
#             + 'Team Work ' * 100 + 'Motivated ' * 100 \
#             + 'Self-learner ' * 100 + 'Comunication '* 90\
#             + 'git' * 30
#             )

with open('job_position.txt') as txt_file:
    txt_string = txt_file.read()


wordcloud = WordCloud(background_color='white', repeat=False).generate(my_words_string)
wordcloud = WordCloud(background_color='white', repeat=False).generate(txt_string)

fig = plt.figure()
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.show()
