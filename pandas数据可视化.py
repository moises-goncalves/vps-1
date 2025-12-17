from operator import index

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
# data = pd.Series(np.random.randn(1000),index=np.arange(1000))
# data = data.cumsum()



data = pd.DataFrame(np.random.randn(1000,4),
                    index=np.arange(1000),
                    columns=list("ABCD"))
data = data.cumsum()
print(data.head)
# plot方法 bar条形图 hist box area scatter hexbin pie
ax = data.plot.scatter(x = "A",y = "B",color = "DarkBlue",label = "Class 1")

plt.show()