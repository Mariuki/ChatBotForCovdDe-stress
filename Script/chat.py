# -*- coding: utf-8 -*-
"""De-Stress Chatbot.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nJOL3jGeZyfNRaxrWqK26mLz4VQd7xZo

# Funciones
"""

def is_question(input_string):
  for i in input_string:
    if i == '?':
      output = True
    else:
      output = False
  return output

def remove_punctuation(input_string):
  out_string = ""
  for i in input_string:
    if i not in string.punctuation:
      out_string += i
  return out_string

def prepare_text(input_string):
  temp_string = input_string.lower()
  temp_string = remove_punctuation(temp_string)
  out_list = temp_string.split()
  return out_list

def respond_echo(input_string, number_of_echoes,spacer):
  if input_string != None:
    echo_output = (input_string + spacer) * number_of_echoes
  else:
    echo_output = None
  return echo_output

def selector(input_list, check_list, return_list):
  output = None
  for i in input_list:
    if i in check_list:
      output = random.choice(return_list)
      break
  return output

def string_concatenator(string1, string2, separator):
  output = string1 + separator + string2
  return output

def list_to_string(input_list, separator):
  output = input_list[0]
  for i in input_list[1:]:
    output = string_concatenator(output, i, separator)
  return output

def end_chat(input_list):
  if 'quit' in input_list:
    output = True
  else:
    output = False
  return output

def is_in_list(list_one, list_two):
    """Check if any element of list_one is in list_two."""
    
    for element in list_one:
        if element in list_two:
            return True
    return False

def find_in_list(list_one, list_two):
    """Find and return an element from list_one that is in list_two, or None otherwise."""
    
    for element in list_one:
        if element in list_two:
            return element
    return None

def is_points(input_string):
  p = 0
  h = []
  for i in input_string:
    o = i.count('.')
    if o == 1:
      p += 1
      if p == 5:
        break
    h.append(i)
  h.append('.')
  return h

"""# Librerias"""

#!pip install covid
from covid import Covid
import string
import random
import nltk
import pandas as pd
import numpy as np
import textwrap
import cv2

"""# Información"""

#!git clone https://github.com/ChatBotChallengeCdCMX/ChatBotForCovidDe-stress.git

Hombres = pd.read_csv('/content/ChatBotForCovidDe-stress/DataBases/nombreshombres .csv')
Mujeres = pd.read_csv('/content/ChatBotForCovidDe-stress/DataBases/nombresmujeres.csv')
Hombres = list(Hombres.iloc[:,0])
Mujeres = list(Mujeres.iloc[:,0])
Nombres = Hombres + Mujeres
Musica = pd.read_csv('/content/ChatBotForCovidDe-stress/DataBases/Music.csv')
Music = pd.DataFrame(Musica)
categorias_musica = list(pd.unique(Music['terms']))
Videos = pd.read_csv('/content/ChatBotForCovidDe-stress/DataBases/YTVideos.csv')
Videos = pd.DataFrame(Videos)
categorias_videos = list(pd.unique(Videos['category']))
Libros = pd.read_csv('/content/ChatBotForCovidDe-stress/DataBases/booksdataset.csv')
Books = pd.DataFrame(Libros)
categorias_libros = list(pd.unique(Books['category']))
Wiki = pd.read_csv('/content/ChatBotForCovidDe-stress/DataBases/WIKI.csv')
Wikis = pd.DataFrame(Wiki)
name_wikis = list(pd.unique(Wikis['Name']))
categorias_wikis = list(pd.unique(Wikis['Vertical1']))


"""# Custom Chatbot"""

# This cell defines a collection of input and output things our chatbot can say and respond to
Init_greetings = ['Hi! Im your quarantine friend! Are having a good day?', 'Hello! How are you feeling today?', 'Hi! Whats Your name?']
GREETINGS_IN = ['hello', 'hi', 'hey', 'hola', 'welcome', 'bonjour', 'greetings']
GREETINGS_OUT = ["Hello, it's nice to talk to you!", 'Nice to meet you!',  "Hey - Let's chat!"]

NOMBRES_IN = Nombres
NOMBRES_OUT = ['nice to meet you , my name is D-Stress Bot', 'that´s a cool name', ", hello, it's nice to talk to you!" ]

MUSICA_IN = categorias_musica


BOOKS_IN = ['little', 'few', 'lot', 'so', 'or', 'medium', 'large', 'short']

BOOKS_NAMES = categorias_libros

VIDEOS_IN = ['entertainment', 'films', 'style', 'comedy', 'tech', 'blogs', 'sports', 
             'activism', 'news', 'gaming', 'education', 'animals', 'cars', 'travel', 'science']

VIDEOS_NAMES = dict(zip(VIDEOS_IN, categorias_videos))
VIDEOS_NAMES['science'] = VIDEOS_NAMES['tech']

CATEGORY_IN = ['book', 'books', 'music', 'videos', 'video', 'yes', 'reading']
BOOKS_DIC1 = {'short': 'short', 'medium': 'medium', 'large': 'large', 'little': 'short'
             , 'few': 'short', 'lot': 'large', 'so': 'short', 'or': 'short'}
COVID_IN = ['quarentine', 'covid', 'coronavirus', 'lockdown', '19', 'sars', 'corona']


COMP_IN = ['python', 'code', 'computer', 'algorithm', ]
COMP_OUT = ["Python is what I'm made of.", \
            "Did you know I'm made of code!?", \
            "Computers are so magical", \
            "Do you think I'll pass the Turing test?"]

PEOPLE_IN = ['turing', 'hopper', 'neumann', 'lovelace']
PEOPLE_OUT = ['was awesome!', 'did so many important things!', 'is someone you should look up :).']
PEOPLE_NAMES = {'turing': 'Alan', 'hopper': 'Grace', 'neumann': 'John von', 'lovelace': 'Ada'}

JOKES_IN = ['funny', 'hilarious', 'ha', 'haha', 'hahaha', 'lol']
JOKES_OUT = ['ha', 'haha', 'lol'] 

NONO_IN = ['matlab', 'java', 'C++']
NONO_OUT = ["I'm sorry, I don't want to talk about"]

NEGATIVE = ['no', "dont", 'not', "wouldnt", "couldnt", "wont", "doesnt", "arent", "havent", 'none', 'neither', "didnt", "hasnt"]

UNKNOWN = ['Good.', 'Okay', 'Huh?', 'Yeah!', 'Well...', 'Ñam', 'Hum']
CHATTING = ['What would you like to do now? I could recommend you some music, books or cool video, which one do you prefer?', 'Hum so, what type of music do yo like?',
            'Do you want something to relax?', 'I could search some good music for you, what gender do you like?', 'I have some cool videos here, pick one category! :D',
            'Do you like videos? I have different categories', 'Also, I have here some of my favorite books, you like reading a lot, so so, or just a few?', 
            'What should I search about?']

QUESTION = "I'm too shy to answer questions. What do you want to talk about?"

def have_a_chat():
    """Main function to run our chatbot."""
    print(chr(27)+"[1;34m"+'Hi! Im your quarantine friend! What´s your name?: \n')
    chat = True
    urname = None
    while chat:
        
        # Get a message from the user
        if urname != None:
          msg = input(chr(27)+"[1;30m"+str(urname) +': \t')
        else: 
          msg = input(chr(27)+"[1;30m"+'INPUT : \t')

        out_msg = None

        n = msg.upper()
        n = n.split()

        w = msg.capitalize()
        w = w.split()
        
        # Check if the input is a question
        question = is_question(msg)

        # Prepare the input message
        msg = prepare_text(msg)

        # Check for an end msg 
        if end_chat(msg):
            out_msg = 'Bye!'
            chat = False

        # Check for a selection of topics that we have defined to respond to
        #   Here, we will check for a series of topics that we have designed to answer to
        if not out_msg:

            # Initialize to collect a list of possible outputs
            outs = []

            # Check if the input looks like a greeting, add a greeting output if so
            outs.append(selector(msg, GREETINGS_IN, GREETINGS_OUT))

            # Check if the input looks like a computer thing, add a computer output if so
            outs.append(selector(msg, COMP_IN, COMP_OUT))

            # Check if the input mentions a person that is specified, add a person output if so
            for i in n:
              i = [i]
              if is_in_list(i, NOMBRES_IN):
                  urname = find_in_list(i, NOMBRES_IN)
                  outs.append(list_to_string([urname.capitalize(),
                                              selector(i, NOMBRES_IN, NOMBRES_OUT)], ' '))
                            
            # Check if the input mentions a person that is specified, add a person output if so
            if is_in_list(msg, PEOPLE_IN):
                name = find_in_list(msg, PEOPLE_IN)
                outs.append(list_to_string([PEOPLE_NAMES[name], name.capitalize(),
                                            selector(msg, PEOPLE_IN, PEOPLE_OUT)], ' '))
                
            if is_in_list(msg, VIDEOS_IN):
                name = find_in_list(msg, VIDEOS_IN)
                ran = np.random.randint(0,len(Videos[Videos['category']==VIDEOS_NAMES[name]]))
                title = Videos[Videos['category']==VIDEOS_NAMES[name]][['title', 'video_id']]
                outs.append(
                    'If you like {} I recommend you this video "{}" that you can watch in https://www.youtube.com/watch?v={}'.format(name,
                        title.iloc[ran][0], title.iloc[ran][1]))  
                
            if is_in_list(msg, MUSICA_IN):
                name = find_in_list(msg, MUSICA_IN)
                ran = np.random.randint(0,len(Music[Music['terms']==name]))
                title = Musica[Musica['terms']==name][['release.name', 'artist.name']]
                outs.append(
                    'If you like {} I recommend you the song "{}" by {}'.format(name,
                        title.iloc[ran][0], title.iloc[ran][1])) 
                
            if is_in_list(msg, COVID_IN):
              covid = Covid()
              cases = covid.get_status_by_country_name(country_name='mexico')
              print(chr(27)+"[1;31m"+'CHATBOT: Here are some information about Covid in your zone: \n')
              for x in cases:
                print(chr(27)+"[1;31m"+ x, ':', cases[x])
              #img = cv2.imread('/content/ChatBotForCovidDe-stress/Imagenes/figura_covid_nacional.png')
              #plt.imshow(img)
              print(chr(27)+"[1;31m"+"CHATBOT: You could find a cool map here: https://gisanddata.maps.arcgis.com/apps/opsdashboard/index.html#/bda7594740fd40299423467b48e9ecf6")
              print(chr(27)+"[1;32m"+"CHATBOT: But let's talk about something more relaxing")
              
            
            if is_in_list(msg, BOOKS_IN):
              name = find_in_list(msg, BOOKS_IN)
              ran = np.random.randint(0,len(Books[Books['category']==BOOKS_DIC1[name]]))
              title = Books[Books['category']==BOOKS_DIC1[name]][['title', 'authors', 'num_pages']]
              outs.append(
                  'This book "{}" could be nice for you, was written by {} with {} pages.'.format(
                      title.iloc[ran][0], title.iloc[ran][1], title.iloc[ran][2]))
              
            if is_in_list(w, name_wikis):
                name = find_in_list(w, name_wikis)
                ran = np.random.randint(0,len(Wikis[Wikis['Name']==name]))
                title = Wikis[Wikis['Name']==name][['Name', 'WikiDescription','WikiUrl']]
                outs.append(
                    'Here is a cool definition of {} that I found for you: {}'.format(
                        title.iloc[ran][0], list_to_string(is_points(title.iloc[ran][1]), '')) +
                     ' You could continue reading in {}'.format(
                        title.iloc[ran][2])) 
                
            if is_in_list(msg, CATEGORY_IN):
                name = find_in_list(msg, CATEGORY_IN)
                outs.append('I have this categories, which one would you like?'+'\n'+
                            '\n -BOOKS: {}'.format(str(categorias_libros)) + '\n' +
                            '\n -VIDEOS:{}'.format(str(VIDEOS_IN)) + '\n' +
                            'and about **MUSIC**, any gender that you like.') 

            # Check if the input looks like a joke, add a repeat joke output if so
            outs.append(respond_echo(selector(msg, JOKES_IN, JOKES_OUT), 3, ''))

            # Check if the input has some words we don't want to talk about, say that, if so
            if is_in_list(msg, NONO_IN):
                outs.append(list_to_string([selector(msg, NONO_IN, NONO_OUT), find_in_list(msg, NONO_IN)], ' '))

            # IF YOU WANTED TO ADD MORE TOPICS TO RESPOND TO, YOU COULD ADD THEM IN HERE

            # We could have selected multiple outputs from the topic search above (if multiple return possible outputs)
            #   We also might have appended None in some cases, meaning we don't have a reply
            #   To deal with this, we are going to randomly select an output from the set of outputs that are not None
            options = list(filter(None, outs))
            if options:
                out_msg = random.choice(options)

        # If we don't have an output yet, but the input was a question, return msg related to it being a question
        if not out_msg and question:
            out_msg = QUESTION
  

        # Catch-all to say something if msg not caught & processed so far
        if not out_msg:
            out_msg = random.choice(UNKNOWN)
        
        print(chr(27)+"[1;36m"+'CHATBOT:')

        for i in textwrap.wrap(str(out_msg), 130):
          print(chr(27)+"[1;36m"+ i)

        if out_msg != 'Bye!':
          print('\n' +chr(27)+"[1;36m"+'CHATBOT: \t'+random.choice(CHATTING))
