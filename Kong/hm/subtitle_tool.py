import re
def shift(file_in, time_shift, file_out):
    re_comp = re.compile(r'^(\d+):(\d+):(\d+),(\d+)\s+--\>\s+(\d+):(\d+):(\d+),(\d+)')

    with open(file_in, 'r', encoding='utf-8') as fin:
        with open(file_out, 'w', encoding='utf-8') as fout:
            for line in fin.readlines():
                g = tuple(map(int, re_comp.match(line)))
                if g:
                    n_st = (((g[0]*3600) + (g[1]*60) + g[2]) * 1000) + g[3] + time_shift
                    n_ft = (((g[4]*3600) + (g[5]*60) + g[6]) * 1000) + g[7] + time_shift
                    
                    if n_st <= 0 and n_ft <= 0:
                        pass
                    else:
                        n_st = 0 if n_st <= 0 else n_st
                        n_ft = 0 if n_ft <= 0 else n_ft
                        
                        n_st = tuple(map(lambda x: x.zfill(2), 
                            map(
                                str, ((n_st//1000)//3600, ((n_st//1000)%3600)/60, ((n_st//1000)%3600)%60, n_st%1000
                            ))))
                        n_ft = tuple(map(lambda x: x.zfill(2), 
                            map(
                                str, ((n_ft//1000)//3600, ((n_ft//1000)%3600)/60, ((n_ft//1000)%3600)%60, n_ft%1000
                            ))))
                        fout.write(f'{n_st[0]}:{n_st[1]}:{n_st[2]},{n_st[3]} --> {n_ft[0]}:{n_ft[1]}:{n_ft[2]},{n_ft[3]}')
                else:
                    fout.write(f'{line}\n')


# g = '00:00:00,50 --> 00:00:00,90'
# print(re_comp.match(g).groups())

'05:04:03,010'
'18000+240+3'
'18243000+10'

'18243010'
