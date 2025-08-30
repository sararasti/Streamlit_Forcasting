from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.preprocessing import LabelEncoder
import pandas as pd

class PrepProcesor(BaseEstimator, TransformerMixin):
    def __init__(self):
        self.le = LabelEncoder()

    def fit(self, X, y=None):
        self.le.fit(X['Gender'])
        return self

    def transform(self, X, y=None):
        X = X.copy()
        X['Gender'] = self.le.transform(X['Gender'])
        X['RegisterDate'] = pd.to_datetime(X['RegisterDate'])
        X['LastLotteryDate'] = pd.to_datetime(X['LastLotteryDate'])
        today = pd.Timestamp.today()
        X['DaysSinceRegister'] = (today - X['RegisterDate']).dt.days
        X['DaysSinceParticipate'] = (today - X['LastLotteryDate']).dt.days
        X.drop(columns=['RegisterDate', 'LastLotteryDate'], inplace=True)
        lower = X["TotalPurchase"] - 3 * X["TotalPurchase"].std()
        upper = X["TotalPurchase"] + 3 * X["TotalPurchase"].std()
        X = X[(X["TotalPurchase"] > lower) & (X["TotalPurchase"] < upper)]
        return X


columns = [
    'NationalCode', 'Gender', 'Tier', 'TotalPurchase',
    'Frequency', 'LongLife', 'RegisterDate', 'LastLotteryDate',
    'Participated'
]