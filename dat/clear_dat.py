# 6 by 11, ((col1, col2 ... , col6), (row1, row2, ..., row11))
RATIOS = [(0.2578125, 0.3056640625, 0.412109375, 0.5185546875, 0.6640625, 0.8779296875), 
          (0.808695652173913, 0.7333333333333333, 0.6579710144927536, 0.5826086956521739, 0.5072463768115942, 0.4318840579710145, 0.3565217391304348, 
           0.2811594202898551, 0.20579710144927535, 0.13043478260869565, 0.05507246376811594)]

heiarchy = [
    ('vrg_ex', 5), ('vrg_tri', 4), ('vrg_hm', 3), ('vrg_bahsei', 2), ('vrg_oax', 1), ('vrg', 0),
    ('vdsr_ex', 5), ('vdsr_tri', 4), ('vdsr_hm', 3), ('vdsr_reef', 2), ('vdsr_twins', 1), ('vdsr', 0),
    ('vka_ex', 5), ('vka_tri', 4), ('vka_hm', 3), ('vka_vrol', 2), ('vka_yandir', 1), ('vka', 0),
    ('vss_ex', 4), ('vss_tri', 3), ('vss_hm', 2), ('vss_fire', 1), ('vss_ice', 1), ('vss', 0),
    ('vcr_ex', 5), ('vcr_tri', 4), ('vcr_hm', 3), ('vcr_2', 2), ('vcr_1', 1), ('vcr', 0),
    ('vas_ex', 4), ('vas_tri', 3), ('vas_hm', 2), ('vas_felms', 1), ('vas_llothis', 1), ('vas', 0),
    ('vhof_ex', 3), ('vhof_tri', 2), ('vhof_hm', 1), ('vhof', 0),
    ('vmol_ex', 2), ('vmol_hm', 1), ('vmol', 0),
    ('vso_hm', 1), ('vso', 0),
    ('vaa_hm', 1), ('vaa', 0),
    ('vhrc_hm', 1), ('vhrc', 0),
]

clear_data = [
    # Regular vet clears
    ('vdsr', RATIOS[0][0], RATIOS[1][0]),
    ('vrg', RATIOS[0][0], RATIOS[1][1]),
    ('vka', RATIOS[0][0], RATIOS[1][2]),
    ('vss', RATIOS[0][0], RATIOS[1][3]),
    ('vcr', RATIOS[0][0], RATIOS[1][4]),
    ('vas', RATIOS[0][0], RATIOS[1][5]),
    ('vhof', RATIOS[0][0], RATIOS[1][6]),
    ('vmol', RATIOS[0][0], RATIOS[1][7]),
    ('vso', RATIOS[0][0], RATIOS[1][8]),
    ('vaa', RATIOS[0][0], RATIOS[1][9]),
    ('vhrc', RATIOS[0][0], RATIOS[1][10]),
    
    # Partial HMs 1
    ('vdsr_twins', RATIOS[0][1], RATIOS[1][0]),
    ('vrg_oax', RATIOS[0][1], RATIOS[1][1]),
    ('vka_yandir', RATIOS[0][1], RATIOS[1][2]),
    ('vss_fire', RATIOS[0][1], RATIOS[1][3]),
    ('vcr_1', RATIOS[0][1], RATIOS[1][4]),
    ('vas_llothis', RATIOS[0][1], RATIOS[1][5]),
    
    # Partial HMs 2
    ('vdsr_reef', RATIOS[0][2], RATIOS[1][0]),
    ('vrg_bahsei', RATIOS[0][2], RATIOS[1][1]),
    ('vka_vrol', RATIOS[0][2], RATIOS[1][2]),
    ('vss_ice', RATIOS[0][2], RATIOS[1][3]),
    ('vcr_2', RATIOS[0][2], RATIOS[1][4]),
    ('vas_felms', RATIOS[0][2], RATIOS[1][5]),
    
    # Full HM's
    ('vdsr_hm', RATIOS[0][3], RATIOS[1][0]),
    ('vrg_hm', RATIOS[0][3], RATIOS[1][1]),
    ('vka_hm', RATIOS[0][3], RATIOS[1][2]),
    ('vss_hm', RATIOS[0][3], RATIOS[1][3]),
    ('vcr_hm', RATIOS[0][3], RATIOS[1][4]),
    ('vas_hm', RATIOS[0][3], RATIOS[1][5]),
    ('vhof_hm', RATIOS[0][3], RATIOS[1][6]),
    ('vmol_hm', RATIOS[0][3], RATIOS[1][7]),
    ('vso_hm', RATIOS[0][3], RATIOS[1][8]),
    ('vaa_hm', RATIOS[0][3], RATIOS[1][9]),
    ('vhrc_hm', RATIOS[0][3], RATIOS[1][10]),
    
    # Trifectas
    ('vdsr_tri', RATIOS[0][4], RATIOS[1][0]),
    ('vrg_tri', RATIOS[0][4], RATIOS[1][1]),
    ('vka_tri', RATIOS[0][4], RATIOS[1][2]),
    ('vss_tri', RATIOS[0][4], RATIOS[1][3]),
    ('vcr_tri', RATIOS[0][4], RATIOS[1][4]),
    ('vas_tri', RATIOS[0][4], RATIOS[1][5]),
    ('vhof_tri', RATIOS[0][4], RATIOS[1][6]),
    
    # Extras
    ('vdsr_ex', RATIOS[0][5], RATIOS[1][0]),
    ('vrg_ex', RATIOS[0][5], RATIOS[1][1]),
    ('vka_ex', RATIOS[0][5], RATIOS[1][2]),
    ('vss_ex', RATIOS[0][5], RATIOS[1][3]),
    ('vcr_ex', RATIOS[0][5], RATIOS[1][4]),
    ('vas_ex', RATIOS[0][5], RATIOS[1][5]),
    ('vhof_ex', RATIOS[0][5], RATIOS[1][6]),
    ('vmol_ex', RATIOS[0][5], RATIOS[1][7]),
]

