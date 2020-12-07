#%%
Provinciehoofdsteden = dict([
('Noord_Holland' , 'Amsterdam'),
('Zuid_Holland', 'Den_Haag'),
('Utrecht', 'Utrecht'),
])

type(Provinciehoofdsteden)
print(Provinciehoofdsteden)
Provinciehoofdsteden['Zeeland'] = 'Middelburg'
Provinciehoofdsteden['Limburg'] = 'Maastricht'
Provinciehoofdsteden['Gelderland'] = 'ert'
print(Provinciehoofdsteden)

del Provinciehoofdsteden["Zuid_Holland"]
print(Provinciehoofdsteden)

Provinciehoofdsteden["Gelderland"] = "Arnhem"
for key,val in Provinciehoofdsteden.items():
    print(key, "=>", val)
# %%
