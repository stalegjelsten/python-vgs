#%%
# T'(t) = -k(T(t) - T_0)
# k = -0.29

T_0 = 16
k = 0.29
tid = 5  # timer
oppløsning = tid * 3600  # beregner for hvert sekund
delta_t = 1 / oppløsning
T = 38

for i in range(oppløsning):
    deltaT = -k * (T - T_0) * delta_t
    T += deltaT
    print(T)
# %%

T_0 = 20
k = 0.10
tid = 5  # timer
oppløsning = tid * 60  # beregner for hvert sekund
delta_t = 1 / oppløsning
T = 90

for i in range(oppløsning):
    deltaT = -k * (T - T_0) 
    T += deltaT
    print(T)
# %%

delta_t = 0.1
tid = 5
antall_steg = round(tid/delta_t)
k = 0.10
T_omgivelse = 20
T = 90

for i in range(antall_steg):
    delta_T = -k * (T-T_omgivelse) * delta_t
    T += delta_T

print(T)
#%%
delta_t = 0.01
tid = 0
k = 0.29
T_omgivelse = 10
T_målt = 15
T = 38

while T > T_målt:
    delta_T = - k * (T-T_omgivelse) * delta_t
    T += delta_T
    tid += delta_t

print(f"Personen døde for {tid:.2f} timer siden.")




# %%
