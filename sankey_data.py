import pandas as pd

def obtain_tesla_data():
  # Data from TESLA Q3 FY23 report
  data = {
  'labels':['Automotive sales', 'Automotive regulatory credits', 'Automotive leasing','Automotive revenue',
            'Energy generation & storage','Services','Revenue','Gross profit',
            'Cost of revenue','Operating profit', 'Operating expense', 'Net profit',
            'Tax','Other','Interest','Automotive sales',
            'Automotive leasing', 'Energy generation & storage', 'Services', 'Research & development',
            'Selling, general & admit'],

  # where link starts
  'source':[0,1,2,3,
            4,5,3,6,
            6,7,7,9,
            9,9,14,8,
            8,8,8,10,10],

  # where link ends
  'target':[3,3,3,6,
            6,6,6,7,
            8,9,10,11,
            12,13,11,15,
            16,17,18,19,20],

  # item values
  'value':[18582,554,489,19625,
           1559,2166,0,4178,
           19172,1764,2414,1878,
           37,167,282,15656,
           301,1178,2037,1161,1253],

  # define the link color
  'link_colors':['rgb(140,140,140)','rgb(140,140,140)','rgb(140,140,140)','rgb(140,140,140)',
                'rgb(140,140,140)','rgb(140,140,140)','rgb(140,140,140)','rgb(153,162,231)',
                'rgb(240,128,128)','rgb(153,162,231)','rgb(240,128,128)','rgb(153,162,231)',
                'rgb(240,128,128)','rgb(240,128,128)','rgb(240,128,128)','rgb(240,128,128)',
                'rgb(240,128,128)','rgb(240,128,128)','rgb(240,128,128)','rgb(240,128,128)','rgb(240,128,128)'],

  # separate the item color
  'colors': ['rgb(0,0,0)','rgb(0,0,0)','rgb(0,0,0)','rgb(0,0,0)',
             'rgb(0,0,0)','rgb(0,0,0)','rgb(0,0,0)','rgb(0,31,231)',
             'rgb(231,41,0)','rgb(0,31,231)','rgb(231,41,0)','rgb(0,31,231)',
             'rgb(231,41,0)','rgb(231,41,0)','rgb(231,41,0)','rgb(231,41,0)',
             'rgb(231,41,0)','rgb(231,41,0)','rgb(231,41,0)','rgb(231,41,0)','rgb(231,41,0)'],

  # define node position (x,y)
  'x':[0,0.05,0.05,0.1,
       0.25,0.25,0.2,0.5,
       0.5,0.6,0.6,0.8,
       0.65,0.65,0.75,0.6,
       0.6,0.6,0.6,0.75,0.75],

  'y':[0,0.8,0.9,0,
       0.9,1,0,0.3,
       0.7,0.1,0.4,0.1,
       0.2,0.28,0.2,0.7,
       0.9,1,1.1,0.4,0.5]
  }

  link = "https://www.sec.gov/edgar/browse/?CIK=1318605&owner=exclude/"
  report_name = 'TESLA Q3 FY23'

  return data, link, report_name

def tesla_sankey_data():

  tesla_data,link,report_name = obtain_tesla_data()
  df = pd.DataFrame(tesla_data)

  # sum up revenue
  val = (df[df['labels']=='Automotive revenue']['value'].values[0]+
        df[df['labels']=='Energy generation & storage']['value'].values[0]+
        df[df['labels']=='Services']['value'].values[0])/1000

  df.loc[:,'label'] = [f'{label} <br>{v/1000}B' if v != 0 else f'{label}<br>{val}B' for label, v in zip(df['labels'], df['value'])]

  return df, link, report_name
