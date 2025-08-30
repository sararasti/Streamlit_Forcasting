{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "3bcbdc6a-ed04-4a99-aa37-0a807b973453",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.base import BaseEstimator, TransformerMixin\n",
    "from sklearn.preprocessing import LabelEncoder\n",
    "import pandas as pd\n",
    "\n",
    "class LotteryPreprocessor(BaseEstimator, TransformerMixin):\n",
    "    def __init__(self):\n",
    "        self.le = LabelEncoder()\n",
    "\n",
    "    def fit(self, X, y=None):\n",
    "        self.le.fit(X['Gender'])\n",
    "        return self\n",
    "\n",
    "    def transform(self, X, y=None):\n",
    "        X = X.copy()\n",
    "\n",
    "        X['Gender'] = self.le.transform(X['Gender'])\n",
    "\n",
    "        X['RegisterDate'] = pd.to_datetime(X['RegisterDate'])\n",
    "        X['LastLotteryDate'] = pd.to_datetime(X['LastLotteryDate'])\n",
    "        today = pd.Timestamp.today()\n",
    "        X['DaysSinceRegister'] = (today - X['RegisterDate']).dt.days\n",
    "        X['DaysSinceParticipate'] = (today - X['LastLotteryDate']).dt.days\n",
    "\n",
    "        X.drop(columns=['RegisterDate', 'LastLotteryDate'], inplace=True)\n",
    "\n",
    "        lower = X[\"TotalPurchase\"] - 3 * X[\"TotalPurchase\"].std()\n",
    "        upper = X[\"TotalPurchase\"] + 3 * X[\"TotalPurchase\"].std()\n",
    "        X = X[(X[\"TotalPurchase\"] > lower) & (X[\"TotalPurchase\"] < upper)]\n",
    "        return X\n",
    "columns = [\n",
    "            'UserID', 'Gender', 'Age', 'Participated', 'RegisterDate',\n",
    "            'LastLotteryDate', 'TotalPurchase', 'Region'\n",
    "        ]"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
