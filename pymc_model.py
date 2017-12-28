import pandas as pd
import sklearn.datasets as ds
import pymc

# 팬다스 데이터프레임을 준비한다.
bs = ds.load_boston()
df = pd.DataFrame(bs.data, columns=bs.feature_names)
df['MEDV'] = bs.target

# 우리가 추정할 매개변수를 정의한다.
A = pymc.Exponential('A', beta=1)
B = pymc.Exponential('B', beta=1)
C = pymc.Exponential('C', beta=1)

# 학생/교사 비율 
ptratio = pymc.Exponential(
    'ptratio', beta=df.PTRATIO.mean(),
    observed=True, value=df.PTRATIO)
# 범죄율
crim = pymc.Exponential('crim',
                        beta=A * ptratio, observed=True, value=df.CRIM)
# 방의 개수
rm = pymc.Normal('rm', mu=df.RM.mean(),
                 tau=1 / (df.RM.std() ** 2), value=df.RM, observed=True)
# 집값의 중간값
medv = pymc.Normal('medv', mu=B * rm * (C - crim),
                   value=df.MEDV, observed=True)

