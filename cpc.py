class dc:

    def __init__(self, name):
        self.name = name

    def get_filename(self):
        return self.name+".csv" 
            
    def raw_file(self):
        import pandas as pd
        return pd.read_csv(self.get_filename())

    def file_w_headers(self):
        f=self.raw_file()
        f.columns = ['year', 'rank', 'company', 'revenue', 'profit']
        return f

    def file_ok(self):
        f=self.file_w_headers()
        return f.profit.dtype == 'float64'

