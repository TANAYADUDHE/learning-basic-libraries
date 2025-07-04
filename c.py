import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
#sample dataframe
df=pd.DataFrame({'Branch':['EE','CSE','ENTC','MEC','ENTC','EE','CSE','MEC','ENTC'],
                 'Score':[85,90,78,88,97,95,78,80,92]})
#plot a boxplot
sns.boxplot(x='Branch',y='Score', data=df)
plt.show()