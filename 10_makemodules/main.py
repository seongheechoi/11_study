import read_mv

try:
    fname = 'D:/01_Bigdata/11_study/10_makemodules/data/u18_ODU1_test.csv'
    if fname[0]:
        df = read_mv.SAC_S(fname)
        mv0_odu = df.mv0_odu
        comp = df.comp
    else:
        print('Warning', '파일을 선택하지 않았습니다.')
except (KeyError, UnicodeDecodeError, NameError, pd.errors.EmptyDataError, pd.errors.ParserError):
    print('Warning', 'ODU1 MV 파일이 아닙니다. ODU1 MV 원본파일을 선택하십시오.')
print(comp)
print(mv0_odu)