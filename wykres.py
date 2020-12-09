from bokeh.plotting import figure, output_file, show

p = figure(plot_width=1400, plot_height=1000, tools = 'pan, reset')

p.title.text = "Earthquakes"
p.title.text_color = "orange"
p.title.text_font = "times"
p.title.text_font_style = "italic"
p.yaxis.minor_tick_line_color = "blue"
p.xaxis.minor_tick_line_color = "red"

p.xaxis.axis_label = "Times"
p.yaxis.axis_label = "Value"
p.circle([1,2,3,4,5], [5,6,5,5,3], size= 300, color="pink")

output_file("Scatter_plotting.html")
show(p)