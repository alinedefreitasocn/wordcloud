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

# It worked with the image Irina changed for me because it was pure black and
# white. You can get the nparray straight from the image. Doesn need to
# make the for transformation
# getting my png file
leaf_mask = np.array(Image.open('/home/aline/code/personal_projects/wordcloud/masks/susteinability_black_white.png'))
leaf_mask = np.array(Image.open('/home/aline/code/personal_projects/wordcloud/masks/big_one_leaf.png'))

#########################################################################

# trying to work on my image
leaf_image = Image.open('/home/aline/code/personal_projects/wordcloud/masks/big_one_leaf.png')

# for when your image is already pure black and white
# function to transform zero values into 255 (white)
def transform_format(val):
    if val != 0:
        return 255
    else:
        return val

# Transform your mask into a new one that will work with the function:
# transformed_leaf_mask = np.ndarray((leaf_mask.shape[0],
#                                     leaf_mask.shape[1]),
#                                     np.int32)

# for i in range(len(leaf_mask)):
#     transformed_leaf_mask[i] = list(map(transform_format, leaf_mask[i]))


# creating my string of words
my_words_dict = {'Python ': 100,
                 'SQL ': 80,
                 'Git ': 80,
                 'Jupyter notebook': 50,
                 'Time-series Analysis': 100,
                 'Environmental Analysis': 100,
                 'Statistical Analysis': 90,
                 #
                 'English ': 100,
                 'Spanish ': 70,
                 'Italian ': 50,
                 'Portuguese ': 90,
                 'French': 20,
                 'German': 10,
                 #
                 'Team-Work ': 100,
                 'Self-Motivated ': 100,
                 'Self-learner ': 100,
                 'Comunication ': 90,
                 'Adaptability': 100,
                 'Resiliente': 100,
                 'Multi-disciplinary': 100

}

my_words_string = ''
for word, experience in my_words_dict.items():
    my_words_string = my_words_string + (word * experience)

# getting the string from the job position
# string_file = '/home/aline/code/personal_projects/wordcloud/job_position.txt'
# with open(string_file) as txt_file:
#     txt_string = txt_file.read()
colors = ['#606C38', '#283618', '#DDA15E', '#BC6C25']
# creating the wordcloud
# wc = WordCloud(background_color="white",
#                max_words=700000000,
#                 contour_width=3,
#                 min_font_size=8,
#                 colormap='gist_earth',
#                 prefer_horizontal=1,
#                 #Importance of relative word frequencies for font-size.
#                 # With relative_scaling=0, only word-ranks are considered.
#                 # With relative_scaling=1, a word that is twice as frequent
#                 # will have twice the size. If you want to consider the word
#                 # frequencies and not only their rank, relative_scaling around
#                 # .5 often looks good.
#                 relative_scaling=1,
#                 # Whether to repeat words and phrases until
#                 # max_words or min_font_size is reached.
#                 repeat=True,
#                 width=600,
#                 height=900)

# For github
wc_git = WordCloud(background_color="black",
               max_words=7000000,
                contour_width=3,
                min_font_size=8,
                colormap='plasma',
                prefer_horizontal=1,
                #Importance of relative word frequencies for font-size.
                # With relative_scaling=0, only word-ranks are considered.
                # With relative_scaling=1, a word that is twice as frequent
                # will have twice the size. If you want to consider the word
                # frequencies and not only their rank, relative_scaling around
                # .5 often looks good.
                relative_scaling=1,
                # Whether to repeat words and phrases until
                # max_words or min_font_size is reached.
                repeat=True,
                width=800,
                height=400)

wc_git.generate_from_frequencies(my_words_dict)


# wordcloud = WordCloud(background_color='white', repeat=False).generate(my_words_string)
# wordcloud = WordCloud(background_color='white', repeat=False).generate(txt_string)

fig = plt.figure()
plt.imshow(wc_git, interpolation="bilinear")
plt.axis("off")
plt.show()
