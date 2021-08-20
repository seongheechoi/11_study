import pandas as pd
import os

class SAC_S:
    def __init__(self, dir):
        mv_odu = pd.read_csv(dir, skiprows=6)
        mv_odu['mv_sec'] = (mv_odu['siter'] - 1) * 2
        comp = mv_odu[['mv_sec', 'INV 현재']]

        float32 = ['Error', 'ErrorUnit', '압축비', '설정온도차', 'INV 목표', 'INV 현재', 'FAN 목표', 'FAN 현재', 'FAN2 목표',
                   'FAN2 현재', '공기온도', '흡입온도', '응축온도', '증발온도', 'INV 토출온도', '열교환기온도', '열교환기출구', 'Comp Heatsink',
                   'INV토출과열도', 'IHEX 입구', 'IHEX 출구']
        int16 = ['siter', '운전모드', '목표고압', '목표저압', 'INV1토출목표', '현재고압', '현재저압', 'COMP기준', 'PC CTRL', '운전상태 유지',
                 '4WAY', 'HOT GAS', 'SUMP HEAT', 'Cooling Fan', '오일분리기', 'POWERRELAY', 'PFC', 'PFC CTRL', 'COP',
                 'DEFROSTING', 'OIL REFUREL', 'OIL RETURN', 'FAN1 H', 'FAN1 L', 'FAN2 H', 'FAN2 L', 'Main EEV',
                 'COMP운전', 'Sub EEV', 'VI EEV1', 'mv_sec']

        mv_odu_list = float32 + int16

        mv_odu.loc[:, float32] = mv_odu.loc[:, float32].astype('float32')
        mv_odu.loc[:, int16] = mv_odu.loc[:, int16].astype('int16')

        mv0_odu = mv_odu[mv_odu_list]
        mv0_odu = pd.merge(mv0_odu, mv_odu['mv_sec'])

        self.mv0_odu = mv0_odu
        self.comp = comp

        # ODU1 파일명 확인하기
        filename = os.path.splitext(dir)[0]
        mv_name = filename[:-5]
        # 전체 mv데이터 불러오기
        idu1 = mv_name + "_IDU1.csv"
        odu2 = mv_name + "_ODU2.csv"
        emctl = mv_name + "_EMCTL.csv"
        if os.path.isfile(idu1):
            data_IDU1 = pd.read_csv(idu1, skiprows=6)
            self.idu1 = data_IDU1
        else:
            print('Warning', 'IDU1 파일이 없습니다.')
        if os.path.isfile(odu2):
            data_ODU2 = pd.read_csv(odu2, skiprows=6)
            self.odu2 = data_ODU2
        else:
            print('Warning', 'ODU2 파일이 없습니다.')
        if os.path.isfile(emctl):
            data_EMCTL = pd.read_csv(emctl, skiprows=6)
            self.emctl = data_EMCTL
        else:
            print('Warning', 'EMCTL 파일이 없습니다.')