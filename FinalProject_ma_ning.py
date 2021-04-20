"""
Name: Ningchuan(Mark) Ma
Class: CS230 - HB4
Instructor: Prof. Masloff
Program Purpose:
    The purpose of this program is to present given data on skyscrapers around the world through an interactive
     data-drive web-based Python application that is Streamlit. Raw data will be organized and charted using
     appropriate modules such as pandas and MatPlotLib.
"""

import streamlit as st
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt

def scatter(df1):
    countries = df1['Country']
    print()

    # create a list of all the countries, some appear more than once in the list because they have more than 1 sky scraper that made the ranking list
    countries_list = countries.tolist()
    print()

    # convert the list into a dictionary for plotting later
    countries_dict = {}
    for i in countries_list:
        if i in countries_dict:
            countries_dict[i] += 1
        else:
            countries_dict[i] = 1

    # the sidebar selection
    countries_list_final = [i for i in countries_dict.keys()]   # for that each country name only appears once
    country = st.sidebar.selectbox('Select Country', countries_list_final)    # selectbox - a dropdown menu where users select a value (country)

    # showing only those in the selected country
    st.write('\n')
    st.write('\n')
    st.write('\n')
    st.write(f'There are {countries_dict[country]} sky scrappers in this country that made the ranking list.')
    df_selected = df1[df1['Country'] == country]        # making a subset of date frame what only contains the those in the selected country
    st.write(df_selected)

    # plot the chart
    # df_selected.plot(x='Year', y='Feet', title='Time Line', kind='scatter').invert_yaxis()

    x = df_selected['Year']
    y = df_selected['Feet']
    plt.scatter(x=x, y=y, c='red', alpha=1)
    plt.title('Time Line')
    plt.xlabel('Year')
    plt.ylabel('Feet')

    st.write('\n')
    st.write('\n')
    st.pyplot()


def main():
    st.set_option('deprecation.showPyplotGlobalUse', False)

    # the very original date frame
    df0 = pd.read_csv('skyscrapers.csv')
    st.title('Project Created by Mark')
    st.write('\n')
    st.write('\n')
    st.write('\n')

    # sorted data by height
    df1 = df0.sort_values(by=['Feet'], ascending=False)
    st.write('Here is the sorted data (by height) in Data Frame:')
    st.write(df1)
    st.write('\n')
    st.write('\n')
    st.write('\n')

    # create & display the map
    df_map = df1[['Name', 'Lat', 'Lon']]
    df_map = df_map.rename(columns={'Lat': 'lat', 'Lon': 'lon'})    # apparently df_map only takes all lower case 'lat' and 'lon' so I have to make such change here
    # print(df_map)
    st.write('Locate these sky scrappers on the map.')
    st.map(df_map)

    # create the scatter plot
    scatter(df1)


main()
