# %%
import pandas as pd
import matplotlib.pyplot as plt



# %%
data = pd.read_csv('Book2.csv')

data.head()



# %%
plt.plot(data.UnitPrice, data.TotalPrice)
plt.xlabel('UnitPrice')
plt.ylabel('TotalPrice')

plt.show()

# %%


x = [1,2,3,4,5,7]
y=[1,3,5,7,9,11]
z =[1,2,4,8,10,11]
plt.plot(x,y)
plt.plot(x,z)
plt.xlabel('x')
plt.ylabel('y and z')
plt.legend(['this is y', 'this is z'])
plt.show()
