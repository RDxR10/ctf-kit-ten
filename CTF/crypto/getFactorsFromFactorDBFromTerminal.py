#We have to get prime factors using factorDB API

>from factordb.factordb import FactorDB

>f = FactorDB(16)

>f.connect()

>result = f.get_factor_list()

>print(result)
