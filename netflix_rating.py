import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms

import seaborn as sns

netflix_data = pd.read_csv('netflix.csv')

#netflix_data.describe()

#print(netflix_data[['ratingdescription','user_rating_score']].groupby(['user_rating_score']).describe())
#print(netflix_data[['ratingdescription','user_rating_score']].corr())

netflix_data[['title', 'release_year']].groupby(['release_year']).describe()
#print(netflix_data[['title', 'release_year']].corr())
number = netflix_data[['title', 'release_year']].groupby('release_year').count()
fig, ax = plt.subplots()
ax.plot(range(10))
ax.set_yticks((2,5,7))
labels = ax.set_ytickslabels(['title']) #set_yticklabels(())

def on_draw(event):
   bboxes = []
   for label in labels:
       bbox = label.get_window_extent()
       # the figure transform goes from relative coords->pixels and we
       # want the inverse of that
       bboxi = bbox.inverse_transformed(fig.transFigure)
       bboxes.append(bboxi)

   # this is the bbox that bounds all the bboxes, again in relative
   # figure coords
   bbox = mtransforms.Bbox.union(bboxes)
   if fig.subplotpars.left < bbox.width:
       # we need to move it over
       fig.subplots_adjust(left=1.1*bbox.width) # pad a little
       fig.canvas.draw()
   return False

fig.canvas.mpl_connect('draw_event', on_draw)
plt.show()