import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
import json

#loading data
with open("data.txt",'r') as f:
    data = json.loads(f.read())


num_bins = 500
plt.hist(data, num_bins, facecolor='teal', alpha=0.9)

#Setting axis limits

plt.xlim(-200,200)
plt.ylim(0,1000)

#Setting graph labels
plt.title("Distribution of the Score of \"Data.\" Comments")
plt.ylabel("Number of Comments")
plt.xlabel("Number of Upvotes")

#Saving the figure
plt.savefig("apirlfirst.png",dpi=300)


#Zooming out the figure
plt.xlim(-400,400)
plt.ylim(0,2000)

plt.savefig("apirlfirst-zoomedout.png",dpi=300)


#Closing the figure
plt.close()
