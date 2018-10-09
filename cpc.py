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

    def out_msg(self):
        if(self.file_ok()):
           msg = "All profits are numeric. No changes in length and data types:"
        else:
           msg = "non-numeric profits are removed. New length and data types:"
        return msg

    def clean_file(self):
        import pandas as pd
        f=self.file_w_headers()
        if(not(self.file_ok())):
           non_numberic_profits = f.profit.str.contains('[^0-9.-]')
           f = f.loc[~non_numberic_profits]
           f.profit = f.profit.apply(pd.to_numeric)
        return f

    def len(self):
        return len(self.file_w_headers())

    def len_clean(self):
        return len(self.clean_file())

