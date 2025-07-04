values = [10.2,'meg',25]
values
#%%
values.sort()
#%%
mix = [names,values]

mix
#%%
nums
#%%
nums.append(90)
nums
#%%
nums.insert(2,77)
nums
#%%
nums.remove(10)  #based on value
nums
#%%
nums.pop(1)   #based on index
#%%
nums
#%%
nums.pop()
nums
#%%
del nums[1:]
#%%
nums
#%%
nums.extend([29,22,77,82,12])
nums
#%%
min(nums)
#%%
max(nums)
#%%
sum(nums)
#%%
nums.sort()
#%%
nums
#%%
#TUPLES    IMMUTABLE  USED WHEN NO CHAGE IS REQUIRED AND IT PROCESS FASTER THAN LIST

tup = (21,36,21,14,25)
#%%
tup
#%%
tup[1]
#%%
tup[1] = 22
#%%
tup.count(21)
#%%
#SETS
#INDEXING IS NOT SUPPORTED
#REPEATED VALUE IS NOT ALLOWED

S= {22,25,5,14,12}
S
#%%
S
#%%
S = {22,25,5,14,12,12,22}
#%%
S
#%%
S
#%%
S[2]       #as indexing is not there so ....
#%%
#DICTIONARY


data = {1:'sam',2:'pam', 3:'meg'}
data
#%%
print(data)
#%%
data[4]
#%%
data[3]
#%%
data.get(1)

#%%
data.get(3)
#%%
data.get(1,'not found')
#%%
data.get(4,'not found')
#%%
keys = ['sam', 'pam', 'meg']
values = ['python', 'java', 'js']

data = dict (zip(keys,values))


data
#%%
data['pam']
#%%
data['carl'] = 'css'
#%%
data
#%%
del data['meg']
#%%
data
#%%
prog = {'js':'atom', 'cs':'vs',

        'python' : ['pycharm','sublime'],
        'java' : {'jse': 'netbeans', 'jee':'eclipse'}
        }

prog
#%%
prog['js']
#%%
prog['python']
#%%
prog['python'][1]
#%%
prog['java']
#%%
prog['java']['jee']
#%%
#new
#%%
