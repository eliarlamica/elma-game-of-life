# from bokeh.plotting import figure, curdoc
# from bokeh.driving import linear
# import random

# p = figure(plot_width=400, plot_height=400)
# r1 = p.line([], [], color="firebrick", line_width=2)
# r2 = p.line([], [], color="navy", line_width=2)

# ds1 = r1.data_source
# ds2 = r2.data_source

# @linear()
# def update(step):
#     ds1.data['x'].append(step)
#     ds1.data['y'].append(random.randint(0,300))
#     ds2.data['x'].append(step)
#     ds2.data['y'].append(random.randint(0,80))
#     ds1.trigger('data', ds1.data, ds1.data)
#     ds2.trigger('data', ds2.data, ds2.data)


# curdoc().add_root(p)

# # Add a periodic callback to be run every 500 milliseconds
# curdoc().add_periodic_callback(update, 500)

from bokeh.plotting import figure, output_file, show

game_world = [[1,0,1],[0,0,0],[1,0,0]];

live_cells_x = []
live_cells_y = []

size_of_cell = 20

for x, row in enumerate(game_world):
    for y, cell in enumerate(row):
        if cell == 1:
            live_cells_x.append(x*20)
            live_cells_y.append(y*20)

output_file('rectangles.html')

p = figure(plot_width=400, plot_height=400)
p.rect(x=live_cells_x, y=live_cells_y, width=size_of_cell, height=size_of_cell, color="red", alpha=0.5)
show(p)


