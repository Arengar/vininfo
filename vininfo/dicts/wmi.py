from ..brands import Lada, Nissan, Opel, Renault

# NOTE:
# if you want to extend this mapping with new WMIs, please use
# vininfo.utils.merge_wmi() function and replace the entire WMI with
# the result of this function. This comment must stay intact.
WMI = {
    '000': 'Maserati',
    '04W': 'Buick',
    '0VF': 'Ford',
    '112': 'Volkswagen',
    '115': 'Mercedes-Benz',
    '117': 'Volkswagen',
    '119': 'Replica/Kit Makes',
    '123': 'Mercedes-Benz',
    '124': 'Chevrolet',
    '137': 'AM',
    '178': 'Jaguar',
    '17V': 'Ford',
    '19': 'Acura',
    '19U': 'Acura',
    '19V': 'Acura',
    '19X': 'Honda',
    '1A4': 'Chrysler',
    '1A8': 'Chrysler',
    '1B': 'Dodge',
    '1B3': 'Dodge',
    '1B4': 'Dodge',
    '1B7': 'Dodge',
    '1C': 'Chrysler',
    '1C3': 'Chrysler',
    '1C4': 'Dodge',
    '1C6': 'Ram',
    '1C8': 'Chrysler',
    '1CN': 'Lincoln',
    '1D': 'Dodge',
    '1D3': 'Dodge',
    '1D4': 'Dodge',
    '1D5': 'Dodge',
    '1D7': 'Dodge',
    '1D8': 'Dodge',
    '1F': 'Ford',
    '1F1': 'Ford',
    '1F2': 'Subaru',
    '1F6': 'Ford',
    '1F9': 'FWD Corp.',
    '1FA': 'Ford',
    '1FB': 'Ford',
    '1FC': 'Ford',
    '1FD': 'Ford',
    '1FM': 'Ford',
    '1FT': 'Ford',
    '1FU': 'Freightliner',
    '1FV': 'Freightliner',
    '1G': 'General Motors',
    '1G1': 'Chevrolet',
    '1G2': 'Pontiac',
    '1G3': 'Oldsmobile',
    '1G4': 'Buick',
    '1G6': 'Cadillac',
    '1G8': 'Saturn',
    '1G9': 'Google',
    '1GA': 'Chevrolet',
    '1GB': 'Chevrolet USA',
    '1GC': 'Chevrolet',
    '1GD': 'GMC',
    '1GE': 'Cadillac',
    '1GG': 'Isuzu',
    '1GH': 'Oldsmobile',
    '1GJ': 'GMC',
    '1GK': 'GMC',
    '1GM': 'Pontiac',
    '1GN': 'Chevrolet USA',
    '1GT': 'GMC Truck',
    '1GY': 'Cadillac',
    '1H': 'Honda',
    '1HD': 'Harley-Davidson',
    '1HG': 'Honda',
    '1J': 'Jeep',
    '1J4': 'Jeep',
    '1J8': 'Jeep',
    '1JN': 'Nissan',
    '1L': 'Lincoln',
    '1L1': 'Lincoln',
    '1L4': 'Jeep',
    '1LN': 'Lincoln',
    '1M': 'Mercury',
    '1M1': 'Mack Truck',
    '1M2': 'Mack Truck',
    '1M3': 'Mack Truck',
    '1M4': 'Mack Truck',
    '1M9': 'Mynatt Truck & Equipment',
    '1ME': 'Mercury',
    '1N': Nissan(),
    '1N4': 'Nissan',
    '1N6': 'Nissan',
    '1NX': 'NUMMI',
    '1P3': 'Plymouth',
    '1P4': 'Plymouth',
    '1R9': 'Roadrunner Hay Squeeze',
    '1TK': 'Scion',
    '1V1': 'Volkswagen USA (Commercials)',
    '1V2': 'Volkswagen',
    '1V4': 'Nissan',
    '1VW': 'Volkswagen',
    '1XK': 'Kenworth',
    '1XP': 'Peterbilt',
    '1Y1': 'Chevrolet',
    '1YV': 'Mazda',
    '1Z3': 'Mitsubishi',
    '1Z7': 'Mitsubishi',
    '1ZV': 'Auto Alliance International',
    '1ZW': 'Mercury',
    '210': 'Ford',
    '2A4': 'Chrysler Canada',
    '2A8': 'Chrysler Canada',
    '2B3': 'Dodge Canada',
    '2B4': 'Dodge',
    '2B5': 'Dodge',
    '2B6': 'Dodge',
    '2B7': 'Dodge',
    '2B8': 'Dodge',
    '2C3': 'Chrysler',
    '2C4': 'Chrysler Canada',
    '2C7': 'Dodge',
    '2C8': 'Chrysler',
    '2CK': 'Pontiac',
    '2CN': 'CAMI',
    '2CT': 'General Motors',
    '2D3': 'Dodge',
    '2D4': 'Dodge Canada',
    '2D6': 'Dodge',
    '2D7': 'Dodge',
    '2D8': 'Dodge Canada',
    '2DG': 'Ontario Drive & Gear',
    '2F': 'Ford',
    '2FA': 'Ford',
    '2FD': 'Ford',
    '2FM': 'Ford',
    '2FT': 'Ford Motor Company',
    '2FU': 'Freightliner',
    '2FV': 'Freightliner',
    '2FZ': 'Sterling',
    '2G': 'General Motors',
    '2G1': 'Chevrolet',
    '2G2': 'Pontiac',
    '2G3': 'Oldsmobile',
    '2G4': 'Buick',
    '2G6': 'Cadillac',
    '2G9': 'Gnome Homes',
    '2GC': 'Chevrolet Canada',
    '2GE': 'Cadillac',
    '2GK': 'GMC',
    '2GN': 'Chevrolet Canada',
    '2GT': 'GMC',
    '2H': 'Honda',
    '2HG': 'Honda',
    '2HH': 'Acura',
    '2HJ': 'Honda',
    '2HK': 'Honda',
    '2HM': 'Hyundai',
    '2HN': 'Acura',
    '2L': 'Lincoln',
    '2L1': 'Lincoln',
    '2LM': 'Lincoln',
    '2LN': 'Lincoln',
    '2M': 'Mercury',
    '2ME': 'Mercury',
    '2MH': 'Mercury',
    '2MR': 'Mercury',
    '2NV': 'Nova Bus',
    '2P3': 'Plymouth',
    '2P4': 'Plymouth',
    '2S2': 'Suzuki',
    '2S3': 'Suzuki Canada',
    '2T': 'Toyota',
    '2T1': 'Toyota',
    '2T2': 'Lexus Canada',
    '2T3': 'Toyota',
    '2V4': 'Volkswagen',
    '2V8': 'Volkswagen',
    '2W': 'Western Star',
    '309': 'Chevrolet',
    '3A': 'Chrysler Mexico',
    '3A4': 'Chrysler',
    '3A8': 'Chrysler',
    '3B6': 'Dodge',
    '3B7': 'Dodge Mexico',
    '3C': 'Chrysler',
    '3C3': 'Fiat',
    '3C4': 'Dodge Mexico',
    '3C6': 'Ram',
    '3C7': 'Ram',
    '3C8': 'Chrysler',
    '3CZ': 'Honda Mexico',
    '3D': 'Dodge',
    '3D2': 'Dodge',
    '3D3': 'Dodge',
    '3D4': 'Dodge',
    '3D5': 'Dodge',
    '3D6': 'Dodge',
    '3D7': 'Dodge',
    '3F': 'Ford',
    '3FA': 'Ford',
    '3FC': 'Ford',
    '3FD': 'Ford',
    '3FE': 'Ford',
    '3FT': 'Ford',
    '3G': 'General Motors',
    '3G0': 'Saab',
    '3G1': 'Chevrolet',
    '3G2': 'Pontiac',
    '3G5': 'Buick',
    '3G7': 'Pontiac',
    '3GC': 'Chevrolet Mexico',
    '3GD': 'GMC',
    '3GK': 'GMC',
    '3GN': 'Chevrolet Mexico',
    '3GS': 'Saturn',
    '3GT': 'GMC',
    '3GV': 'Chevrolet',
    '3GY': 'Cadillac',
    '3H': 'Honda',
    '3HG': 'Honda',
    '3KP': 'Kia',
    '3LN': 'Lincoln',
    '3MD': 'Mazda',
    '3ME': 'Mercury Mexico',
    '3MY': 'Mazda Mexico',
    '3MZ': 'Mazda Mexico',
    '3N': Nissan(),
    '3N1': 'Nissan',
    '3N6': 'Chevrolet',
    '3N8': 'Nissan',
    '3NA': 'Nissan',
    '3P3': 'Plymouth Mexico',
    '3TM': 'Toyota Mexico',
    '3VV': 'Volkswagen',
    '3VW': 'Volkswagen',
    '460': 'Mercedes-Benz',
    '4A': 'Mitsubishi',
    '4A3': 'Mitsubishi',
    '4A4': 'Mitsubishi',
    '4B3': 'Dodge',
    '4C3': 'Chrysler',
    '4F': 'Mazda',
    '4F2': 'Mazda',
    '4F4': 'Mazda',
    '4G1': 'Chevrolet',
    '4GD': Opel(),
    '4J': 'Mercedes-Benz',
    '4JG': 'Mercedes-Benz',
    '4M': 'Mercury',
    '4M2': 'Mercury',
    '4N2': 'Nissan',
    '4NU': 'Isuzu',
    '4RK': 'Nova Bus',
    '4S': 'Subaru-Isuzu Automotive',
    '4S2': 'Isuzu',
    '4S3': 'Subaru',
    '4S4': 'Subaru',
    '4S6': 'Honda',
    '4T': 'Toyota',
    '4T1': 'Toyota',
    '4T3': 'Toyota',
    '4T4': 'Toyota',
    '4TA': 'Toyota',
    '4US': 'BMW',
    '4UZ': 'Frt-Thomas Bus',
    '4V': 'Volvo',
    '54D': 'Chevrolet',  # Spartan,
    '55': 'Mercedes-Benz',
    '55S': 'Mercedes-Benz',
    '58A': 'Lexus',
    '5BZ': 'Nissan',
    '5F': 'Honda',
    '5FN': 'Honda',
    '5FP': 'Honda',
    '5FR': 'Acura',
    '5GA': 'Buick',
    '5GN': 'Hummer',
    '5GR': 'Hummer',
    '5GT': 'Hummer',
    '5GZ': 'Saturn',
    '5J6': 'Honda',
    '5J8': 'Acura',
    '5KB': 'Honda',
    '5L': 'Lincoln',
    '5L1': 'Lincoln',
    '5LM': 'Lincoln',
    '5LT': 'Lincoln',
    '5N1': Nissan(),
    '5N3': Nissan('Infiniti'),
    '5NA': 'Nissan',
    '5NM': 'Hyundai',
    '5NP': 'Hyundai',
    '5S3': 'Saab',
    '5T': 'Toyota',
    '5TB': 'Toyota',
    '5TD': 'Toyota',
    '5TE': 'Toyota',
    '5TF': 'Toyota',
    '5U': 'BMW',
    '5UM': 'BMW',
    '5UX': 'BMW',
    '5X': 'Hyundai/Kia',
    '5XX': 'Kia',
    '5XY': 'Kia',
    '5Y2': 'Pontiac',
    '5YF': 'Toyota',
    '5YJ': 'Tesla',
    '5YM': 'BMW',
    '5Z6': 'Suzuki',
    '601': 'Replica/Kit Makes',
    '602': 'Toyota',
    '6AB': 'MAN',
    '6F': 'Ford',
    '6F4': Nissan('Nissan Motor Company'),
    '6F5': 'Kenworth',
    '6FP': 'Ford Motor Company',
    '6G': 'General Motors',
    '6G1': 'Chevrolet',
    '6G2': 'Pontiac',
    '6G3': 'Chevrolet Australia',
    '6H': 'Holden',
    '6H8': 'General Motors-Holden',
    '6MM': 'Mitsubishi',
    '6T1': 'Toyota',
    '7A3': 'Honda',
    '7FA': 'Honda',
    '8A1': Renault(),
    '8AC': 'Mercedes Benz',
    '8AD': 'Peugeot',
    '8AF': 'Ford',
    '8AG': 'General Motors',
    '8AJ': 'Toyota',
    '8AK': 'Suzuki',
    '8AP': 'Fiat',
    '8AT': 'Iveco',
    '8AW': 'Volkswagen',
    '8BC': 'Citroën',
    '8BR': 'Mercedes-Benz Argentina',
    '8BT': 'Mercedes-Benz Argentina',
    '8C3': 'Honda',
    '8GD': 'Peugeot',
    '8GG': 'Chevrolet',
    '935': 'Citroën',
    '936': 'Peugeot',
    '93H': 'Honda',
    '93R': 'Toyota',
    '93U': 'Audi',
    '93V': 'Audi Brazil',
    '93W': 'Fiat Professional',
    '93X': 'Souza Ramos - Mitsubishi / Suzuki',
    '93Y': Renault(),
    '93Z': 'Iveco',
    '94D': Nissan(),
    '953': 'VW Trucks / MAN',
    '95P': 'CAOA / Hyundai',
    '988': 'Jeep',
    '98M': 'BMW',
    '98R': 'Chery',
    '99A': 'Audi',
    '99J': 'JLR Jaguar Land Rover',
    '9BD': 'Fiat Automóveis',
    '9BF': 'Ford',
    '9BG': 'General Motors',
    '9BH': 'Hyundai Motor Company / Hyundai',
    '9BM': 'Mercedes Benz',
    '9BR': 'Toyota',
    '9BS': 'Scania',
    '9BV': 'Volvo Trucks',
    '9BW': 'Volkswagen',
    '9C2': 'Honda Motorcycles',
    '9C6': 'Yamaha',
    '9CD': 'Suzuki Motorcycles',
    '9FB': Renault(),
    '9UJ': 'Chery',
    '9UK': 'Lifan',
    '9UW': 'Kia',
    'AAV': 'Volkswagen',
    'AFA': 'Ford',
    'AHT': 'Toyota',
    'B01': 'Cadillac',
    'CF1': Renault(),
    'CL9': 'Wallyscar',
    'EDB': 'Mercedes-Benz',
    'FM2': 'Mercury',
    'FSM': 'FSM',
    'FV1': Renault(),
    'FV3': 'Peugeot',
    'FV7': 'Citroen',
    'G4G': 'Buick',
    'G61': 'Cadillac',
    'GA1': Renault(),
    'GKA': 'GMC',
    'JA': 'Isuzu',
    'JA3': 'Mitsubishi',
    'JA4': 'Mitsubishi',
    'JAC': 'Isuzu',
    'JAE': 'Acura',
    'JB3': 'Dodge',
    'JC1': 'Fiat Automobiles/Mazda',
    'JDA': 'Daihatsu',
    'JF': 'Fuji Heavy Industries',
    'JF1': 'Scion',
    'JF2': 'Subaru',
    'JF4': 'Saab',
    'JFS': 'Subaru',
    'JGN': 'Chevrolet',
    'JH': 'Honda',
    'JH4': 'Acura',
    'JHC': 'Honda',
    'JHL': 'Honda',
    'JHM': 'Honda',
    'JK': 'Kawasaki',
    'JM': 'Mazda',
    'JM1': 'Mazda',
    'JM3': 'Mazda',
    'JMB': 'Mitsubishi',
    'JN': Nissan(),
    'JN1': 'Nissan',
    'JN8': 'Nissan',
    'JNB': 'Nissan',
    'JNK': Nissan('Infiniti'),
    'JNR': Nissan('Infiniti'),
    'JNT': Nissan('Infiniti'),
    'JNX': Nissan('Infiniti'),
    'JS': 'Suzuki',
    'JS2': 'Suzuki',
    'JS3': 'Suzuki',
    'JT': 'Toyota',
    'JT2': 'Toyota',
    'JT3': 'Toyota',
    'JT4': 'Toyota',
    'JT5': 'Toyota',
    'JT6': 'Lexus',
    'JT8': 'Lexus',
    'JTD': 'Toyota',
    'JTE': 'Toyota',
    'JTH': 'Lexus',
    'JTJ': 'Lexus',
    'JTK': 'Scion',
    'JTL': 'Scion',
    'JTM': 'Toyota',
    'JTN': 'Scion',
    'JTS': 'Toyota',
    'JY': 'Yamaha',
    'KC4': 'Dodge',
    'KL': 'Daewoo/GM Korea',
    'KL1': 'Chevrolet',
    'KL2': 'Pontiac',
    'KL4': 'Buick',
    'KL5': 'Suzuki',
    'KL7': 'Chevrolet',
    'KL8': 'Chevrolet',
    'KLA': 'Chevrolet',
    'KLM': 'Lincoln',
    'KM': 'Hyundai',
    'KM8': 'Hyundai',
    'KMH': 'Genesis',
    'KN': 'Kia',
    'KN1': 'Nissan',
    'KNA': 'Kia',
    'KND': 'Kia',
    'KNM': Renault('Renault Samsung'),
    'KP': 'SsangYong',
    'KRX': 'BMW',
    'L4C': 'Buick',
    'L56': Renault('Renault Samsung'),
    'L5Y': 'Merato Motorcycle Taizhou Zhongneng',
    'L6T': 'Geely',
    'LBE': 'Beijing Hyundai',
    'LBV': 'BMW Brilliance',
    'LC0': 'BYD Bus',
    'LDC': 'Dongfeng Peugeot-Citroën',
    'LDY': 'Zhongtong Coach',
    'LE4': 'Beijing Benz',
    'LFM': 'FAW Toyota',
    'LFP': 'FAW Car',
    'LFV': 'FAW-Volkswagen',
    'LGB': 'Dongfeng Nissan',
    'LGH': 'Dong Feng (DFM), China',
    'LGJ': 'Dongfeng Fengshen',
    'LGW': 'Great Wall (Havel)',
    'LGX': 'BYD Auto',
    'LH1': 'FAW Haima',
    'LHG': 'Guangzhou Honda',
    'LJ1': 'JAC',
    'LJD': 'Dongfeng Yueda Kia',
    'LKL': 'Suzhou King Long',
    'LLV': 'Lifan',
    'LMG': 'GAC Trumpchi',
    'LPA': 'Changan PSA (DS Automobiles)',
    'LRB': 'Buick China',
    'LS5': 'Changan Suzuki',
    'LSG': 'SAIC General Motors',
    'LSJ': 'SAIC MG',
    'LSV': 'SAIC Volkswagen',
    'LSY': 'Brilliance Zhonghua',
    'LTV': 'FAW Toyota (Tianjin)',
    'LUC': 'Honda',
    'LVG': 'GAC Toyota',
    'LVH': 'Dongfeng Honda',
    'LVR': 'Changan Mazda',
    'LVS': 'Changan Ford',
    'LVV': 'Chery',
    'LVY': 'Volvo',
    'LWV': 'GAC Fiat',
    'LYV': 'Volvo China',
    'LZE': 'Isuzu Guangzhou',
    'LZG': 'Shaanxi Automobile Group',
    'LZM': 'MAN',
    'LZW': 'SAIC GM Wuling',
    'LZY': 'Yutong',
    'MA1': 'Mahindra',
    'MA3': 'Suzuki',
    'MA7': 'Honda Siel Cars',
    'MAJ': 'FordS',
    'MAL': 'Hyundai',
    'MAT': 'Tata',
    'MBH': Nissan(),
    'MC2': 'Volvo Eicher commercial vehicles limited.',
    'MDH': Nissan(),
    'MHR': 'Honda',
    'ML3': 'Mitsubishi Thailand',
    'MM0': 'Mazda',
    'MM8': 'Mazda',
    'MMB': 'Mitsubishi',
    'MMC': 'Mitsubishi',
    'MMM': 'Chevrolet',
    'MMS': 'Suzuki',
    'MMT': 'Mitsubishi',
    'MNB': 'Ford',
    'MNT': Nissan(),
    'MP1': 'Isuzu',
    'MPA': 'Isuzu',
    'MR0': 'Toyota',
    'MRH': 'Honda',
    'MS0': 'KIA Myanmar',
    'NLA': 'Honda',
    'NLE': 'Mercedes-Benz Turk Truck',
    'NLH': 'Hyundai',
    'NLJ': 'Hyundai',
    'NM0': 'Ford Otosan',
    'NM4': 'Tofas Turk',
    'NMT': 'Toyota',
    'PE1': 'Ford',
    'PE3': 'Mazda',
    'PL1': 'Proton',
    'SAD': 'Jaguar',
    'SAH': 'Honda',
    'SAJ': 'Jaguar',
    'SAL': 'Land Rover',
    'SAR': 'Rover',
    'SAT': 'Triumph',
    'SAX': 'Rover',
    'SB1': 'Toyota',
    'SBM': 'Mclaren',
    'SCA': 'Rolls Royce',
    'SCB': 'Bentley',
    'SCC': 'Lotus Cars',
    'SCE': 'DeLorean',
    'SCF': 'Aston Martin Lagonda Limited',
    'SDB': 'Peugeot UK',
    'SED': Opel(),
    'SEY': 'LDV',
    'SFA': 'Ford',
    'SFD': 'Alexander Dennis',
    'SHH': 'Honda',
    'SHS': 'Honda',
    'SJA': 'Bentley',
    'SJK': Nissan('Infiniti'),
    'SJN': Nissan(),
    'SKF': Opel(),
    'SMT': 'Triumph',
    'SNE': 'Jeep',
    'SNT': 'Honda',
    'STE': 'Toyota',
    'SU9': 'Solaris Bus & Coach',
    'SUF': 'Fiat Auto Poland / FSM',
    'SUL': 'Daewoo Poland / FSO',
    'SUP': 'Daewoo Poland / FSO',
    'SUR': 'Land Rover',
    'TC3': 'Chrysler',
    'TCC': 'Micro Compact Car AG (SMART 1998-1999)',
    'TDM': 'QUANTYA Swiss Electric Movement',
    'TK9': 'SOR',
    'TM9': 'Škoda trolleybuses',
    'TMA': 'Hyundai',
    'TMB': 'Škoda',
    'TMK': 'Karosa',
    'TMP': 'Škoda trolleybuses',
    'TMT': 'Tatra',
    'TN9': 'Karosa',
    'TNB': 'Skoda',
    'TRA': 'Ikarus Bus',
    'TRU': 'Audi',
    'TSE': 'Ikarus Egyedi Autobuszgyar',
    'TSM': 'Suzuki',
    'TYB': 'Mitsubishi',
    'U5Y': 'Kia',
    'U6Y': 'Kia',
    'USY': 'Kia',
    'UU': 'Dacia',
    'UU1': Renault('Renault Dacia'),
    'V0L': Opel(),
    'VA0': 'ÖAF',
    'VBK': 'KTM',
    'VF0': 'Ford',
    'VF1': Renault(),
    'VF2': Renault(),
    'VF3': 'Peugeot',
    'VF4': 'Talbot',
    'VF5': 'Iveco Unic SA',
    'VF6': 'Renault Trucks/Volvo',
    'VF7': 'Citroën',
    'VF8': 'Matra/Talbot/Simca',
    'VF9': 'Bugatti',
    'VFB': Renault(),
    'VFE': 'IvecoBus',
    'VFF': 'Peugeot',
    'VFG': 'Citroen',
    'VFJ': Renault(),
    'VFZ': 'Citroen',
    'VH8': 'Microcar',
    'VLG': 'Aixam',
    'VLU': 'Scania',
    'VN1': Opel(),
    'VNE': 'Irisbus',
    'VNK': 'Toyota',
    'VNV': Renault(),
    'VS1': 'Iveco',
    'VS3': 'Peugeot',
    'VS5': Renault(),
    'VS6': 'Ford',
    'VS7': 'Citroen',
    'VS9': 'Carrocerias Ayats',
    'VSA': 'Mercedes-Benz',
    'VSE': 'Suzuki / Santana Motors',
    'VSK': Nissan(),
    'VSS': 'SEAT',
    'VSX': Opel(),
    'VSY': Renault(),
    'VSZ': 'Seat',
    'VV9': 'Tauro Sport Auto',
    'VW1': Renault(),
    'VW2': 'Volkswagen',
    'VWA': Nissan(),
    'VWG': 'Volkswagen Spain',
    'VWV': 'Volkswagen',
    'VX1': 'Zastava / Yugo',
    'VY1': 'Volvo',
    'W00': Opel(),
    'W04': 'Buick',
    'W06': 'Cadillac',
    'W08': 'Saturn',
    'W09': 'Ruf Automobile',
    'W0L': Opel('Opel/Vauxhall'),
    'W0S': Opel('Opel Special Vehicles'),
    'W0V': Opel(),
    'WA1': 'Audi',
    'WAG': 'Neoplan',
    'WAP': 'Alpina',
    'WAU': 'Audi',
    'WAV': 'Audi',
    'WAX': 'SsangYong',
    'WB': 'BMW',
    'WBA': 'BMW',
    'WBD': 'Mercedes-Benz',
    'WBS': 'BMW M',
    'WBX': 'BMW',
    'WBY': 'BMW',
    'WCD': 'Mercedes-Benz (Sprinter)',
    'WD0': 'Dodge',
    'WD2': 'Dodge',
    'WD3': 'Daimler AG (Sprinter)',
    'WD4': 'Daimler AG (Sprinter)',
    'WD5': 'Dodge',
    'WD8': 'Mercedes-Benz',
    'WDA': 'Daimler AG (Sprinter)',
    'WDB': 'Mercedes-Benz',
    'WDC': 'DaimlerChrysler AG/Daimler AG',
    'WDD': 'DaimlerChrysler AG/Daimler AG',
    'WDF': 'Mercedes-Benz',
    'WDP': 'Mercedes-Benz (Sprinter)',
    'WDR': 'Mercedes-Benz (Sprinter)',
    'WDW': 'Dodge',
    'WDX': 'Dodge',
    'WDY': 'Mercedes-Benz (Sprinter)',
    'WDZ': 'Mercedes-Benz (Sprinter)',
    'WE0': 'Ford',
    'WEB': 'EvoBus',
    'WF0': 'Ford of Europe',
    'WF1': Renault(),
    'WF3': 'Peugeot',
    'WF7': 'Citroen',
    'WFD': 'Fliegl',
    'WFO': 'Ford',
    'WJM': 'Iveco',
    'WJR': 'Irmscher',
    'WKK': 'Karl Kässbohrer Fahrzeugwerke',
    'WMA': 'MAN',
    'WMB': 'Audi',
    'WME': 'Smart',
    'WMW': 'Mini',
    'WMX': 'DaimlerChrysler AG/Daimler AG',
    'WMZ': 'MINI',
    'WNK': 'Toyota',
    'WOL': Opel(),
    'WP0': 'Porsche car',
    'WP1': 'Porsche SUV',
    'WS0': 'Ford',
    'WSS': 'Seat',
    'WUA': 'Quattro',
    'WUW': 'Volkswagen',
    'WV': 'Volkswagen',
    'WV0': 'Ford',
    'WV1': 'Volkswagen Commercial Vehicles',
    'WV2': 'Volkswagen Commercial Vehicles',
    'WV3': 'Volkswagen Trucks',
    'WVG': 'Volkswagen',
    'WVW': 'Volkswagen',
    'WVZ': 'Volkswagen',
    'WWD': 'Mercedes-Benz',
    'WWW': 'Volkswagen',
    'WYG': 'Volkswagen',
    'WYW': 'Volkswagen',
    'WZW': 'Volkswagen',
    'X7L': Renault(),
    'X96': 'Mercedes-Benz',
    'XL9': 'Spyker',
    'XLB': 'Volvo',
    'XLR': 'DAF Trucks',
    'XMC': 'Mitsubishi (NedCar)',
    'XNC': 'Mitsubishi',
    'XTA': Lada('AvtoVAZ'),
    'XUF': Opel(),
    'XW8': 'Volkswagen',
    'XWE': 'Kia',
    'XWF': Opel(),
    'XXX': 'Honda',
    'Y6D': Opel(),
    'YAR': 'Toyota',
    'YCM': 'Mazda',
    'YH4': 'Fisker',
    'YK1': 'Saab',
    'YMB': 'Skoda',
    'YS2': 'Scania, Södertälje',
    'YS3': 'Saab',
    'YS4': 'Scania, Katrineholm',
    'YTN': 'Saab NEVS',
    'YV1': 'Volvo Cars',
    'YV2': 'Volvo Trucks',
    'YV3': 'Volvo Buses',
    'YV4': 'Volvo Cars',
    'Z12': Opel(),
    'Z3B': 'Chevrolet',
    'ZA9': 'Bugatti',
    'ZAC': 'FCA',
    'ZAF': 'Fiat',
    'ZAM': 'Maserati',
    'ZAP': 'Piaggio/Vespa/Gilera',
    'ZAR': 'Alfa Romeo',
    'ZAS': 'Alfa',
    'ZCF': 'Iveco',
    'ZCG': 'Cagiva SpA',
    'ZD4': 'Aprilia',
    'ZDF': 'Ferrari Dino',
    'ZDM': 'Ducati Motor Holdings SpA',
    'ZFA': 'Fiat Automobiles',
    'ZFB': 'Fiat',
    'ZFC': 'Fiat V.I.',
    'ZFF': 'Ferrari',
    'ZGA': 'IvecoBus',
    'ZHW': 'Lamborghini',
    'ZLA': 'Lancia',
    'ZN6': 'Maserati',
    'ZOM': 'OM',
    'ZSA': 'Fiat',
}
