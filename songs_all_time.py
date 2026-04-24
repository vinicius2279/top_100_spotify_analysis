#!/usr/bin/env python
# coding: utf-8

# In[114]:


#Análise de top 100 músicas do Spotify da história do app até a disponibilização do dataset
#no site kaggle.com, onde também há 2 arquivos .csv do chamado Spotify Wrapped 2025
#source: https://www.kaggle.com/datasets/alitaqishah/spotify-wrapped-2025-top-songs-and-artists


# In[115]:


#import das bibliotecas necessárias
import pandas as pd
import numpy as np
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)
pd.set_option("display.max_colwidth", None)


# In[116]:


#leitura do arquivo .csv onde estão os dados
df_spotifySongs = pd.read_csv('spotify_alltime_top100_songs.csv')


# In[117]:


#lista de colunas e as 10 primeiras linhas do dataset pra melhor compreensão dos dados
print(df_spotifySongs.head(10))


# In[118]:


#1 - Classificando as músicas do artista The Weeknd pelo total de streams
print("\n----- Classificação das músicas de The Weeknd -----\n")
filterTheWeeknd = df_spotifySongs['artist'] == 'The Weeknd'
resultado = df_spotifySongs[filterTheWeeknd].sort_values(by='total_streams_billions', ascending=False)

print(resultado)


# In[119]:


#2 - mostrando as músicas de rock do top 100, organizado por posição histórica
filterRock = df_spotifySongs['primary_genre'].str.contains('Rock')
resultadoRock = df_spotifySongs[filterRock].sort_values(by='alltime_rank', ascending=True)
print(resultadoRock)


# In[120]:


#3 - média de bilhões de streams por artista
print("\n----- Média de streams por artista (bilhões) -----\n")

print(df_spotifySongs[['artist', 'total_streams_billions']].groupby('artist')['total_streams_billions'] \
    .mean().sort_values(ascending=False).head(10).round(2))


# In[121]:


#4 - contagem de gêneros que mais se repetem no top 100
print("\n----- Gêneros mais repetidos -----\n")

print(df_spotifySongs['primary_genre'].value_counts())


# In[122]:


#5 - gerando linha randômica do dataframe
print("\n----- Linha Randômica -----\n")

import random as rd
rd1 = rd.randint(0, 100)
RdiLoc = df_spotifySongs.iloc[[rd1]]
print(RdiLoc)


# In[123]:


#6 exibindo os países com maior média de streams
print("\n-----Países com maiores média de streams-----\n")

print(df_spotifySongs.groupby('artist_country')['total_streams_billions'] \
 .mean().sort_values(ascending=False).head(10).round(3))


# In[124]:


#7 - as músicas mais dançantes e seus respectivos artistas, posições e streams
print("\n------ Músicas mais dançantes -----\n")

print(df_spotifySongs[['artist', 'alltime_rank', 'total_streams_billions', 'danceability']]
      .sort_values(by='danceability', ascending=False).head(10))


# In[125]:


#8 contagem de músicas explícitas usando estrutura de repetição
print("\n---- Músicas explícitas e não explícitas com For -----\n")

explicitT = 0
explicitF = 0
for index, row in df_spotifySongs.iterrows() :
    if (row['explicit']) :
        explicitT +=1
    else:
        explicitF +=1

print("Explícitas: ", explicitT)
print("Não explícitas: ", explicitF)


# In[126]:


#9 contagem de músicas explícitas usando counts (bem mais fácil)
print("\n---- Total de músicas explícitas usando value counts -----\n")

print(df_spotifySongs['explicit'].value_counts())


# In[127]:


#10 - gráfico de barra com os artisas qie mais se repetem e seus streams
import matplotlib.pyplot as plt

top_artists = (
    df_spotifySongs.groupby('artist')['total_streams_billions'].sum()
    .sort_values(ascending=False).head(10)
)

plt.figure(figsize=(10, 5))
plt.bar(top_artists.index, top_artists.values)

plt.title("Top 10 artistas por streams")
plt.xlabel("Artista")
plt.ylabel("Total de streams (bilhões)")

plt.xticks(rotation=45)
plt.show()


# In[128]:


#gráfico de pizza com países com maior quantidade de streams
top_countries = (df_spotifySongs.groupby(['artist_country'])['total_streams_billions']
.sum().head(10))

plt.figure(figsize=(8,8))
plt.title("Top 10 países por streams")
plt.pie(top_countries.values, labels=top_countries.index,autopct='%1.1f%%')
plt.show()

