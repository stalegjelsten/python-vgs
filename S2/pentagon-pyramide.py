# %% [markdown]
# ![](https://r-knott.surrey.ac.uk/Figurate/FIGimgs/pyrSq5side.gif)
# 

#%%

n = 5
min_sum = 0
for i in range(1,n+1):
    antall_i_lag = i**2
    min_sum += antall_i_lag
    
print(min_sum)

#%% [markdown]
# ![](https://r-knott.surrey.ac.uk/Figurate/FIGimgs/pyrPent5side.gif)
#
# 

#%%

n = 5
min_sum = 0
for i in range(1,n+1):
    antall_i_lag =  i*5-i
    min_sum += antall_i_lag

print(min_sum)
