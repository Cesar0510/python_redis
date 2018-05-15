# https://plot.ly/
# http://www.pygal.org/en/latest/documentation/first_steps.html
import pygal                                                      
bar_chart = pygal.Bar()                                            
bar_chart.add('Fibonacci', [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]) 
bar_chart.add('Fibonacci 2 ', [1, 3, 5, 7,9, 0]) 
bar_chart.render_to_file('bar_chart.svg')