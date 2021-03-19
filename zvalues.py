import pandas as pd
g=pd.read_csv('newgamestats.csv')
h=g[['possession','shots_ongoal','allowed_ongoal','team','opponent']]
t=h.groupby('team').agg(['std','mean'])
t=t.reset_index()
#t.loc[t['team']=='Willem II'].iloc[:,1]
endframe=pd.DataFrame()
for i in range(len(h)):
    strin=h.iloc[i,:]
    pos=strin.possession
    sh=strin.shots_ongoal
    ash=strin.allowed_ongoal
    op_p_std = t.loc[t['team']==strin.opponent].iloc[:,1]
    op_pos= t.loc[t['team']==strin.opponent].iloc[:,2]

    op_ash_std=t.loc[t['team']==strin.opponent].iloc[:,5]
    op_ash=t.loc[t['team']==strin.opponent].iloc[:,6]

    op_sh_std=t.loc[t['team']==strin.opponent].iloc[:,3]
    op_sh=t.loc[t['team']==strin.opponent].iloc[:,4]

    strin['Z_pos']=(op_pos+pos-100)/op_p_std
    strin['Z_attack']=(sh-op_ash)/op_ash_std
    strin['Z_def']=(op_sh-ash)/op_sh_std
    endframe=endframe.append(strin,ignore_index=True)

endframe.to_csv('endframe.csv')
print(endframe)
