import streamlit as st
from datetime import datetime, time

# タイトルを設定
st.title('FS評価用パラメータ定義 BI用データ作成実行')

# ユーザー入力のための数値入力フィールドを作成
FS_PRECON_1_input1 = st.date_input('FS評価開始日 (YYYY/MM/DD) を入力', help='FS評価を開始する日付を入力')
FS_PRECON_1_input2 = st.time_input('FS評価開始時刻 (HH：MM) を入力',  help='FS評価を開始する時刻を入力')
FS_PRECON_2 = st.number_input('FS評価期間 (h) を入力', placeholder='h', value=0, help='FS評価する対象期間を入力') # 時間で期間を定義する？
FS_PRECON_3 = st.number_input('年修日数（年間の設備停止日数） (day/annual) を入力', placeholder='day/annual', value=30)
FS_PRECON_7 = st.selectbox('通貨単位を選択',('YEN', 'RMB', 'INR'), index=0)
FS_PRECON_8 = st.number_input('コークス単価（Dry） (通貨/ton-coke) を入力', placeholder='通貨/ton-coke', value=0, help='市場単価に合わせ、顧客にて入力　（例：2500 RMB/ton-coke）')
FS_PRECON_9 = st.number_input('蒸気単価 (通貨/ton-steam) を入力', placeholder='通貨/ton-steam', value=0, help='市場単価に合わせ、顧客にて入力　（例：160 RMB/ton-steam）')
FS_PRECON_10 = st.number_input('電力単価 (通貨/kw) を入力', placeholder='通貨/kw', value=0, help='市場単価に合わせ、顧客にて入力　（例：1 RMB/kw）')
FS_PRECON_11 = st.number_input('TG発電効率　（蒸気 1tonあたりの発電量） (kw/ton-steam) を入力', placeholder='kw/ton-steam', value=290, help='TG仕様により異なるが、263.13kw/t-s  or  290kw/t-s が一般的')
FS_PRECON_12 = st.number_input('CO濃度増加におけるソリューションロス低減比率（経験理論値） ((ton-coke/h)/%(CO)) を入力', min_value=0.00, max_value=100.00,value=0.01,step=0.01,placeholder='(ton-coke/h)/%(CO)',help='CO濃度1％増加あたりのSL量低減率')
FS_PRECON_13 = st.number_input('コークス投入量に占めるダスト回収比率 (%) を入力', min_value=0.00, max_value=100.00,value=0.01,step=0.01,placeholder='')
FS_PRECON_14 = st.number_input('蒸気発生量原単位 ((ton-steam/h)/(ton-coke/h)) を入力', placeholder='(ton-steam/h)/(ton-coke/h)', value=0.56, help='コークス1ton あたりの蒸気発生量　※基本は0.56～0.57。保証値であり、基本は左記達成')
FS_PRECON_15 = st.number_input('CO濃度増加における主蒸気流量低下率（経験理論値）((ton-steam/h)/%(CO)) を入力', placeholder='(ton-steam/h)/%(CO)', value=0.011, help='VMなどの影響も大きく難しい')
FS_PRECON_16 = st.time_input('シフト開始時刻 (HH：MM) を入力',  help='FS評価する顧客のシフトの開始時間を入力')
FS_PRECON_17 = st.number_input('1シフト時間 (ｈ) を入力', placeholder='ｈ', value=8, help='FS評価する顧客の1シフト時間を入力（2交代なら12, 3交代なら8）')
FS_TIME_1 = st.number_input('メリット最適化の対象期間 (h) を入力', placeholder='h', value=0, help='移動平均による評価期間を入力。単価変動/改定する頻度による　（例：24hr)')
QI130_1_A_FS_1 = st.number_input('CO濃度　管理目標値（顧客前提） (％) を入力', placeholder='％', min_value=0.00, max_value=100.00,value=0.01, help='顧客毎にヒアリングした結果を入力')
QI130_1_A_FS_2 = st.number_input('CO濃度　管理目標値（追い込み）（After / 自動制御導入） (％) を入力', placeholder='％', min_value=0.00, max_value=100.00, value=0.01, help='自動制御導入後の実績')
QI130_1_A_FS_3 = st.number_input('CO濃度　管理上限値　（顧客・地域によるが、基本上限10％） (％) を入力', placeholder='％', min_value=0.00, max_value=100.00, value=0.01, help='顧客毎にヒアリングした結果を入力')
QI130_1_A_FS_6 = st.number_input('CO濃度　操業精度・レンジ上限　（After / 自動制御導入） (％) を入力', placeholder='％', min_value=0.00, max_value=100.00, value=0.01, help='自動制御導入後の実績')
QI130_1_A_FS_10 = st.number_input('CO濃度　操業精度・レンジFS結果　（After / 自動制御導入） (土　％) を入力', placeholder='土　％', min_value=0.00, max_value=100.00,value=0.01, help='操業目標値（After / 自動制御導入）に対して、±１％')
TI120_FS_1 = st.number_input('ボイラー入口温度　管理目標値（顧客前提） (℃) を入力', placeholder='℃', value=0, help='顧客毎にヒアリングした結果を入力')
TI120_FS_2 = st.number_input('ボイラー入口温度　管理目標値（追い込み）（After / 自動制御導入） (℃) を入力', placeholder='℃', value=0, help='自動制御導入後の実績')
TI120_FS_3 = st.number_input('ボイラー入口温度　管理上限値　（基本980℃） (℃) を入力', placeholder='℃', value=0, help='顧客毎にヒアリングした結果を入力')
TI120_FS_6 = st.number_input('ボイラー入口温度　操業精度・レンジ上限　（After / 自動制御導入） (℃) を入力', placeholder='℃', value=0, help='自動制御導入後の実績')
TI120_FS_10 = st.number_input('ボイラー入口温度　操業精度・レンジFS結果　（After / 自動制御導入） (土　℃) を入力', placeholder='土　℃', value=0, help='操業目標値（After / 自動制御導入）に対して、±１％')
FIC103_Pv_FS_1 = st.number_input('SF空気導入流量 操作回数/カウント基準値　(流量変化量前提) (Nm3/h/min) を入力', placeholder='Nm3/h/min', value=0, help='')
FIC103_Mv_FS_1 = st.number_input('SF空気導入流量 操作回数/カウント基準値　(開度変化量前提) (%/min) を入力', placeholder='%/min', value=0, help='')
FIC136_Pv_FS_1 = st.number_input('バイパスガス流量 操作回数/カウント基準値　(流量変化量前提) (Nm3/h/min) を入力', placeholder='Nm3/h/min', value=0, help='')
FIC136_Mv_FS_1 = st.number_input('バイパスガス流量 操作回数/カウント基準値　(開度変化量前提) (%/min) を入力', placeholder='%/min', value=0, help='')

# 入力をもとにした計算
FS_PRECON_1 = datetime.combine(FS_PRECON_1_input1, FS_PRECON_1_input2)
# FIC103_Pv_FS_2 = IF ( ABS ( FIC103_Pv(現在) - FIC103_Pv(1分前) )　>　基準値,1,0)
# FIC103_Mv_FS_2 = IF ( ABS ( FIC103_Mv(現在) - FIC103_Mv(1分前) )　>　基準値,1,0)
# FIC136_Pv_FS_2 = IF ( ABS ( FIC136_Pv(現在) - FIC136_Pv(1分前) )　>　基準値,1,0)
# FIC136_Mv_FS_2 = IF ( ABS ( FIC136_Mv(現在) - FIC136_Mv(1分前) )　>　基準値,1,0)

# 実行ボタンを作成
if st.button('BI用データ作成実行'):
    st.write('Result: FINISHED（ダミー）')
