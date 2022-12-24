{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "9e5b1354",
   "metadata": {},
   "outputs": [
    {
     "ename": "FileNotFoundError",
     "evalue": "[Errno 2] No such file or directory: 'C:/Users/bjaya/Downloads/vehicles.csv'",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mFileNotFoundError\u001b[0m                         Traceback (most recent call last)",
      "Input \u001b[1;32mIn [1]\u001b[0m, in \u001b[0;36m<cell line: 3>\u001b[1;34m()\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28;01mimport\u001b[39;00m \u001b[38;5;21;01mpandas\u001b[39;00m \u001b[38;5;28;01mas\u001b[39;00m \u001b[38;5;21;01mpd\u001b[39;00m\n\u001b[0;32m      2\u001b[0m url \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[1;32m----> 3\u001b[0m dataframe \u001b[38;5;241m=\u001b[39m \u001b[43mpd\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mread_csv\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[38;5;124;43mC:/Users/bjaya/Downloads/vehicles.csv\u001b[39;49m\u001b[38;5;124;43m'\u001b[39;49m\u001b[43m)\u001b[49m\n\u001b[0;32m      4\u001b[0m dataframe1 \u001b[38;5;241m=\u001b[39m pd\u001b[38;5;241m.\u001b[39mread_csv(\u001b[38;5;124m'\u001b[39m\u001b[38;5;124mC:/Users/bjaya/Downloads/vehicles.csv\u001b[39m\u001b[38;5;124m'\u001b[39m)\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\util\\_decorators.py:311\u001b[0m, in \u001b[0;36mdeprecate_nonkeyword_arguments.<locals>.decorate.<locals>.wrapper\u001b[1;34m(*args, **kwargs)\u001b[0m\n\u001b[0;32m    305\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m \u001b[38;5;28mlen\u001b[39m(args) \u001b[38;5;241m>\u001b[39m num_allow_args:\n\u001b[0;32m    306\u001b[0m     warnings\u001b[38;5;241m.\u001b[39mwarn(\n\u001b[0;32m    307\u001b[0m         msg\u001b[38;5;241m.\u001b[39mformat(arguments\u001b[38;5;241m=\u001b[39marguments),\n\u001b[0;32m    308\u001b[0m         \u001b[38;5;167;01mFutureWarning\u001b[39;00m,\n\u001b[0;32m    309\u001b[0m         stacklevel\u001b[38;5;241m=\u001b[39mstacklevel,\n\u001b[0;32m    310\u001b[0m     )\n\u001b[1;32m--> 311\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m func(\u001b[38;5;241m*\u001b[39margs, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwargs)\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\parsers\\readers.py:680\u001b[0m, in \u001b[0;36mread_csv\u001b[1;34m(filepath_or_buffer, sep, delimiter, header, names, index_col, usecols, squeeze, prefix, mangle_dupe_cols, dtype, engine, converters, true_values, false_values, skipinitialspace, skiprows, skipfooter, nrows, na_values, keep_default_na, na_filter, verbose, skip_blank_lines, parse_dates, infer_datetime_format, keep_date_col, date_parser, dayfirst, cache_dates, iterator, chunksize, compression, thousands, decimal, lineterminator, quotechar, quoting, doublequote, escapechar, comment, encoding, encoding_errors, dialect, error_bad_lines, warn_bad_lines, on_bad_lines, delim_whitespace, low_memory, memory_map, float_precision, storage_options)\u001b[0m\n\u001b[0;32m    665\u001b[0m kwds_defaults \u001b[38;5;241m=\u001b[39m _refine_defaults_read(\n\u001b[0;32m    666\u001b[0m     dialect,\n\u001b[0;32m    667\u001b[0m     delimiter,\n\u001b[1;32m   (...)\u001b[0m\n\u001b[0;32m    676\u001b[0m     defaults\u001b[38;5;241m=\u001b[39m{\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mdelimiter\u001b[39m\u001b[38;5;124m\"\u001b[39m: \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124m,\u001b[39m\u001b[38;5;124m\"\u001b[39m},\n\u001b[0;32m    677\u001b[0m )\n\u001b[0;32m    678\u001b[0m kwds\u001b[38;5;241m.\u001b[39mupdate(kwds_defaults)\n\u001b[1;32m--> 680\u001b[0m \u001b[38;5;28;01mreturn\u001b[39;00m \u001b[43m_read\u001b[49m\u001b[43m(\u001b[49m\u001b[43mfilepath_or_buffer\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[43mkwds\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\parsers\\readers.py:575\u001b[0m, in \u001b[0;36m_read\u001b[1;34m(filepath_or_buffer, kwds)\u001b[0m\n\u001b[0;32m    572\u001b[0m _validate_names(kwds\u001b[38;5;241m.\u001b[39mget(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mnames\u001b[39m\u001b[38;5;124m\"\u001b[39m, \u001b[38;5;28;01mNone\u001b[39;00m))\n\u001b[0;32m    574\u001b[0m \u001b[38;5;66;03m# Create the parser.\u001b[39;00m\n\u001b[1;32m--> 575\u001b[0m parser \u001b[38;5;241m=\u001b[39m TextFileReader(filepath_or_buffer, \u001b[38;5;241m*\u001b[39m\u001b[38;5;241m*\u001b[39mkwds)\n\u001b[0;32m    577\u001b[0m \u001b[38;5;28;01mif\u001b[39;00m chunksize \u001b[38;5;129;01mor\u001b[39;00m iterator:\n\u001b[0;32m    578\u001b[0m     \u001b[38;5;28;01mreturn\u001b[39;00m parser\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\parsers\\readers.py:933\u001b[0m, in \u001b[0;36mTextFileReader.__init__\u001b[1;34m(self, f, engine, **kwds)\u001b[0m\n\u001b[0;32m    930\u001b[0m     \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39moptions[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhas_index_names\u001b[39m\u001b[38;5;124m\"\u001b[39m] \u001b[38;5;241m=\u001b[39m kwds[\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mhas_index_names\u001b[39m\u001b[38;5;124m\"\u001b[39m]\n\u001b[0;32m    932\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhandles: IOHandles \u001b[38;5;241m|\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[1;32m--> 933\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39m_engine \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43m_make_engine\u001b[49m\u001b[43m(\u001b[49m\u001b[43mf\u001b[49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mengine\u001b[49m\u001b[43m)\u001b[49m\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\parsers\\readers.py:1217\u001b[0m, in \u001b[0;36mTextFileReader._make_engine\u001b[1;34m(self, f, engine)\u001b[0m\n\u001b[0;32m   1213\u001b[0m     mode \u001b[38;5;241m=\u001b[39m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mrb\u001b[39m\u001b[38;5;124m\"\u001b[39m\n\u001b[0;32m   1214\u001b[0m \u001b[38;5;66;03m# error: No overload variant of \"get_handle\" matches argument types\u001b[39;00m\n\u001b[0;32m   1215\u001b[0m \u001b[38;5;66;03m# \"Union[str, PathLike[str], ReadCsvBuffer[bytes], ReadCsvBuffer[str]]\"\u001b[39;00m\n\u001b[0;32m   1216\u001b[0m \u001b[38;5;66;03m# , \"str\", \"bool\", \"Any\", \"Any\", \"Any\", \"Any\", \"Any\"\u001b[39;00m\n\u001b[1;32m-> 1217\u001b[0m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhandles \u001b[38;5;241m=\u001b[39m \u001b[43mget_handle\u001b[49m\u001b[43m(\u001b[49m\u001b[43m  \u001b[49m\u001b[38;5;66;43;03m# type: ignore[call-overload]\u001b[39;49;00m\n\u001b[0;32m   1218\u001b[0m \u001b[43m    \u001b[49m\u001b[43mf\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1219\u001b[0m \u001b[43m    \u001b[49m\u001b[43mmode\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1220\u001b[0m \u001b[43m    \u001b[49m\u001b[43mencoding\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43moptions\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mget\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mencoding\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43;01mNone\u001b[39;49;00m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1221\u001b[0m \u001b[43m    \u001b[49m\u001b[43mcompression\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43moptions\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mget\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mcompression\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43;01mNone\u001b[39;49;00m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1222\u001b[0m \u001b[43m    \u001b[49m\u001b[43mmemory_map\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43moptions\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mget\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mmemory_map\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43;01mFalse\u001b[39;49;00m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1223\u001b[0m \u001b[43m    \u001b[49m\u001b[43mis_text\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mis_text\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1224\u001b[0m \u001b[43m    \u001b[49m\u001b[43merrors\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43moptions\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mget\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mencoding_errors\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mstrict\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1225\u001b[0m \u001b[43m    \u001b[49m\u001b[43mstorage_options\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;28;43mself\u001b[39;49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43moptions\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mget\u001b[49m\u001b[43m(\u001b[49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43mstorage_options\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\u001b[43m \u001b[49m\u001b[38;5;28;43;01mNone\u001b[39;49;00m\u001b[43m)\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m   1226\u001b[0m \u001b[43m\u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m   1227\u001b[0m \u001b[38;5;28;01massert\u001b[39;00m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhandles \u001b[38;5;129;01mis\u001b[39;00m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;28;01mNone\u001b[39;00m\n\u001b[0;32m   1228\u001b[0m f \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mself\u001b[39m\u001b[38;5;241m.\u001b[39mhandles\u001b[38;5;241m.\u001b[39mhandle\n",
      "File \u001b[1;32m~\\anaconda3\\lib\\site-packages\\pandas\\io\\common.py:789\u001b[0m, in \u001b[0;36mget_handle\u001b[1;34m(path_or_buf, mode, encoding, compression, memory_map, is_text, errors, storage_options)\u001b[0m\n\u001b[0;32m    784\u001b[0m \u001b[38;5;28;01melif\u001b[39;00m \u001b[38;5;28misinstance\u001b[39m(handle, \u001b[38;5;28mstr\u001b[39m):\n\u001b[0;32m    785\u001b[0m     \u001b[38;5;66;03m# Check whether the filename is to be opened in binary mode.\u001b[39;00m\n\u001b[0;32m    786\u001b[0m     \u001b[38;5;66;03m# Binary mode does not support 'encoding' and 'newline'.\u001b[39;00m\n\u001b[0;32m    787\u001b[0m     \u001b[38;5;28;01mif\u001b[39;00m ioargs\u001b[38;5;241m.\u001b[39mencoding \u001b[38;5;129;01mand\u001b[39;00m \u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mb\u001b[39m\u001b[38;5;124m\"\u001b[39m \u001b[38;5;129;01mnot\u001b[39;00m \u001b[38;5;129;01min\u001b[39;00m ioargs\u001b[38;5;241m.\u001b[39mmode:\n\u001b[0;32m    788\u001b[0m         \u001b[38;5;66;03m# Encoding\u001b[39;00m\n\u001b[1;32m--> 789\u001b[0m         handle \u001b[38;5;241m=\u001b[39m \u001b[38;5;28;43mopen\u001b[39;49m\u001b[43m(\u001b[49m\n\u001b[0;32m    790\u001b[0m \u001b[43m            \u001b[49m\u001b[43mhandle\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    791\u001b[0m \u001b[43m            \u001b[49m\u001b[43mioargs\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mmode\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    792\u001b[0m \u001b[43m            \u001b[49m\u001b[43mencoding\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43mioargs\u001b[49m\u001b[38;5;241;43m.\u001b[39;49m\u001b[43mencoding\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    793\u001b[0m \u001b[43m            \u001b[49m\u001b[43merrors\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[43merrors\u001b[49m\u001b[43m,\u001b[49m\n\u001b[0;32m    794\u001b[0m \u001b[43m            \u001b[49m\u001b[43mnewline\u001b[49m\u001b[38;5;241;43m=\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[38;5;124;43m\"\u001b[39;49m\u001b[43m,\u001b[49m\n\u001b[0;32m    795\u001b[0m \u001b[43m        \u001b[49m\u001b[43m)\u001b[49m\n\u001b[0;32m    796\u001b[0m     \u001b[38;5;28;01melse\u001b[39;00m:\n\u001b[0;32m    797\u001b[0m         \u001b[38;5;66;03m# Binary mode\u001b[39;00m\n\u001b[0;32m    798\u001b[0m         handle \u001b[38;5;241m=\u001b[39m \u001b[38;5;28mopen\u001b[39m(handle, ioargs\u001b[38;5;241m.\u001b[39mmode)\n",
      "\u001b[1;31mFileNotFoundError\u001b[0m: [Errno 2] No such file or directory: 'C:/Users/bjaya/Downloads/vehicles.csv'"
     ]
    }
   ],
   "source": [
    "import pandas as pd\n",
    "url = \"\"\n",
    "dataframe = pd.read_csv('C:/Users/bjaya/Downloads/vehicles.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "89120562",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataframe"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f90e3bb7",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataframe.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8151034c",
   "metadata": {},
   "outputs": [],
   "source": [
    "#dataframe = dataframe.sort_values(by='price')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "335717f7",
   "metadata": {},
   "outputs": [],
   "source": [
    "import seaborn as sns\n",
    "\n",
    "sns.heatmap(dataframe.isnull())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "771f6cab",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(\"Unique values in Transmission: \",dataframe['transmission'].unique())\n",
    "print(\"Unique values in Type: \",dataframe['type'].unique())\n",
    "print(\"Unique values in Fuel: \",dataframe['fuel'].unique())\n",
    "print(\"Unique values in Condition: \",dataframe['condition'].unique())\n",
    "print(\"Unique values in Title status: \",dataframe['title_status'].unique())\n",
    "print(\"Unique values in Cylinders: \",dataframe['cylinders'].unique())\n",
    "print(\"Unique values in Drive: \",dataframe['drive'].unique())\n",
    "print(\"Unique values in Manufacturer: \",dataframe['manufacturer'].unique())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1b0d16c8",
   "metadata": {},
   "outputs": [],
   "source": [
    "from matplotlib import pyplot as plt\n",
    "dataframe['drive'].value_counts().plot(kind='pie',title =\"Drive\",radius=2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5f1e3e5d",
   "metadata": {},
   "outputs": [],
   "source": [
    "from matplotlib import pyplot as plt\n",
    "dataframe['manufacturer'].value_counts().plot(kind='pie',title =\"Manufacturer\",radius=2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "aab5f069",
   "metadata": {},
   "outputs": [],
   "source": [
    "from matplotlib import pyplot as plt\n",
    "dataframe['transmission'].value_counts().plot(kind='pie',title =\"Transmission\",radius=2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3a32200a",
   "metadata": {},
   "outputs": [],
   "source": [
    "from matplotlib import pyplot as plt\n",
    "dataframe['type'].value_counts().plot(kind='pie',title =\"Type\",radius=2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "28b9c1d2",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataframe['title_status'].value_counts().plot(kind='pie',title =\"Title Status\",radius=2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9717c030",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataframe['fuel'].value_counts().plot(kind='pie',title =\"Fuel\",radius=2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0b0ce932",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataframe['cylinders'].value_counts().plot(kind='pie',title =\"Cylinders\",radius=2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "96ec8b8d",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataframe['condition'].value_counts().plot(kind='pie',title =\"Condition\",radius=2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b903c9bd",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataframe=dataframe.drop('posting_date', axis=1)\n",
    "dataframe=dataframe.drop('county', axis=1)\n",
    "dataframe=dataframe.drop('description', axis=1)\n",
    "dataframe=dataframe.drop('image_url', axis=1)\n",
    "dataframe=dataframe.drop('VIN', axis=1)\n",
    "dataframe=dataframe.drop('url', axis=1)\n",
    "dataframe=dataframe.drop('region_url', axis=1)\n",
    "dataframe=dataframe.drop('id', axis=1)\n",
    "dataframe=dataframe.drop('model', axis=1)\n",
    "dataframe=dataframe.drop('state', axis=1)\n",
    "dataframe=dataframe.drop('lat', axis=1)\n",
    "dataframe=dataframe.drop('long', axis=1)\n",
    "dataframe=dataframe.drop('region', axis=1)\n",
    "dataframe=dataframe.drop('paint_color', axis=1)\n",
    "dataframe=dataframe.drop('size', axis=1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "da978aaf",
   "metadata": {},
   "outputs": [],
   "source": [
    "import seaborn as sns\n",
    "\n",
    "sns.heatmap(dataframe.isnull())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6ecfae2f",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn import preprocessing\n",
    "le = preprocessing.LabelEncoder()\n",
    "dataframe['manufacturer'] = le.fit_transform(dataframe['manufacturer'])\n",
    "dataframe['fuel'] = le.fit_transform(dataframe['fuel'])\n",
    "dataframe['transmission'] = le.fit_transform(dataframe['transmission'])\n",
    "dataframe['type'] = le.fit_transform(dataframe['type'])\n",
    "dataframe['drive'] = le.fit_transform(dataframe['drive'])\n",
    "dataframe['condition'] = le.fit_transform(dataframe['condition'])\n",
    "dataframe['cylinders'] = le.fit_transform(dataframe['cylinders'])\n",
    "dataframe['title_status'] = le.fit_transform(dataframe['title_status'])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4155d6f5",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataframe"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d86dae73",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataframe.corr()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "85de1bc8",
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.heatmap(dataframe.corr())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b99d0e73",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataframe.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b1b49451",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.experimental import enable_iterative_imputer\n",
    "from sklearn.impute import IterativeImputer\n",
    "ds=['cylinders','price','manufacturer','condition','fuel','title_status','year','transmission','drive','type','odometer']\n",
    "\n",
    "imputer = IterativeImputer()\n",
    "imputer.fit(dataframe[ds])\n",
    "dataframe[ds]=imputer.transform(dataframe[ds])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5f79b4b3",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataframe.corr()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7d9e2ee4",
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.heatmap(dataframe.corr())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "fe93530d",
   "metadata": {},
   "outputs": [],
   "source": [
    "fig,ax = plt.subplots(figsize =(10, 7))\n",
    "ax.hist(dataframe['price'], bins = [0,50000,100000,150000,200000,250000,300000])\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "deefc606",
   "metadata": {},
   "outputs": [],
   "source": [
    "for i in range(len(dataframe)):\n",
    "    if(dataframe['price'][i]>=100000):\n",
    "        dataframe.drop(i,inplace=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a973432a",
   "metadata": {},
   "outputs": [],
   "source": [
    "len(dataframe)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "916e408f",
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.heatmap(dataframe.corr())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "60e12a4c",
   "metadata": {},
   "outputs": [],
   "source": [
    "import seaborn as sns\n",
    "\n",
    "sns.heatmap(dataframe.isnull())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2669b0dc",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataframe.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3b6f1941",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=dataframe.dropna()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e9fe7a96",
   "metadata": {},
   "outputs": [],
   "source": [
    "na='price'\n",
    "pIQR=dataframe[na].quantile(0.75)-dataframe[na].quantile(0.25)\n",
    "pupper=dataframe[na].quantile(0.75)+1.5*pIQR\n",
    "plower=dataframe[na].quantile(0.25)-1.5*pIQR\n",
    "\n",
    "print(na)\n",
    "print(dataframe[na].quantile(0.75))\n",
    "print(dataframe[na].quantile(0.05))\n",
    "print(pupper)\n",
    "print(plower)\n",
    "\n",
    "\n",
    "na='odometer'\n",
    "oIQR=dataframe[na].quantile(0.75)-dataframe[na].quantile(0.25)\n",
    "oupper=dataframe[na].quantile(0.75)+1.5*oIQR\n",
    "olower=dataframe[na].quantile(0.25)-1.5*oIQR\n",
    "dataframe=dataframe[dataframe.price<pupper]\n",
    "dataframe=dataframe[dataframe.odometer<oupper]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "da53fc96",
   "metadata": {},
   "outputs": [],
   "source": [
    "dataframe"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0f2129c2",
   "metadata": {},
   "outputs": [],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6ebd23eb",
   "metadata": {},
   "outputs": [],
   "source": [
    "y = df['price']\n",
    "x = df.drop('price',axis= 1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cca058aa",
   "metadata": {},
   "outputs": [],
   "source": [
    "# creating train and test sets\n",
    "\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.metrics import mean_squared_error, mean_absolute_error\n",
    "X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5c03c2ab",
   "metadata": {},
   "outputs": [],
   "source": [
    "output=[]\n",
    "output.append([\"Regression Algorithm\",\"RMSE\",\"R Squared\",\"Mean Squared Error\",\"Absolute Mean Error\"])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b07f4524",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import LinearRegression\n",
    "model = LinearRegression(fit_intercept=True)\n",
    "\n",
    "model.fit(X_train,y_train)\n",
    "\n",
    "\n",
    "predictions = model.predict(X_test)\n",
    "\n",
    "print('Linear Regression\\nmean_squared_error : ', mean_squared_error(y_test, predictions))\n",
    "print('mean_absolute_error : ', mean_absolute_error(y_test, predictions))\n",
    "print(\"R-Squared\",model.score(X_test,y_test, sample_weight=None))\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "plt.figure(figsize=(40,40))\n",
    "plt.plot( y_test, predictions,'b.',alpha=0.05)\n",
    "plt.plot(y_test,y_test,'r-')\n",
    "\n",
    "\n",
    "mse=mean_squared_error(y_test, predictions)\n",
    "mae=mean_absolute_error(y_test, predictions)\n",
    "rs=model.score(X_test,y_test, sample_weight=None)\n",
    "rmse=math.sqrt(mse)\n",
    "\n",
    "output.append([\"Linear Regression\",rmse,rs,mse,mae])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c25940af",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.figure(figsize=(40,40))\n",
    "plt.plot(t.index, t.values, 'b.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d5581e07",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import Ridge\n",
    "model = Ridge(fit_intercept=True,random_state=1)\n",
    "\n",
    "model.fit(X_train,y_train)\n",
    "predictions = model.predict(X_test)\n",
    "print('Ridge Regression\\nmean_squared_error : ', mean_squared_error(y_test, predictions))\n",
    "print('mean_absolute_error : ', mean_absolute_error(y_test, predictions))\n",
    "print(\"R-Squared\",model.score(X_train,y_train, sample_weight=None))\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "plt.figure(figsize=(40,40))\n",
    "plt.plot( y_test, predictions,'b.',alpha=0.05)\n",
    "plt.plot(y_test,y_test,'r-')\n",
    "\n",
    "mse=mean_squared_error(y_test, predictions)\n",
    "mae=mean_absolute_error(y_test, predictions)\n",
    "rs=model.score(X_test,y_test, sample_weight=None)\n",
    "rmse=math.sqrt(mse)\n",
    "\n",
    "output.append([\"Ridge Regression\",rmse,rs,mse,mae])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "77e38f14",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.figure(figsize=(40,40))\n",
    "plt.plot(t.index, t.values, 'b.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "81fcddf2",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import Lasso\n",
    "\n",
    "model = Lasso(fit_intercept=True,random_state=1)\n",
    "model.fit(X_train,y_train)\n",
    "predictions = model.predict(X_test)\n",
    "print('Lasso\\nmean_squared_error : ', mean_squared_error(y_test, predictions))\n",
    "print('mean_absolute_error : ', mean_absolute_error(y_test, predictions))\n",
    "print(\"R-Squared\",model.score(X_train,y_train, sample_weight=None))\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "plt.figure(figsize=(40,40))\n",
    "plt.plot( y_test, predictions,'b.',alpha=0.05)\n",
    "plt.plot(y_test,y_test,'r-')\n",
    "\n",
    "\n",
    "\n",
    "mse=mean_squared_error(y_test, predictions)\n",
    "mae=mean_absolute_error(y_test, predictions)\n",
    "rs=model.score(X_test,y_test, sample_weight=None)\n",
    "rmse=math.sqrt(mse)\n",
    "\n",
    "output.append([\"Lasso\",rmse,rs,mse,mae])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d4431f4e",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.figure(figsize=(40,40))\n",
    "plt.plot(t.index, t.values, 'b.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "96867ebc",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.tree import DecisionTreeRegressor\n",
    "from sklearn import tree\n",
    "model = DecisionTreeRegressor(max_depth=47,max_features='auto',random_state=1)\n",
    "\n",
    "model.fit(X_train,y_train)\n",
    "predictions = model.predict(X_test)\n",
    "print('Decision Tree Regressor\\nmean_squared_error : ', mean_squared_error(y_test, predictions))\n",
    "print('mean_absolute_error : ', mean_absolute_error(y_test, predictions))\n",
    "print(\"R-Squared\",model.score(X_train,y_train, sample_weight=None))\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "plt.figure(figsize=(40,40))\n",
    "plt.plot( y_test, predictions,'b.',alpha=0.05)\n",
    "plt.plot(y_test,y_test,'r-')\n",
    "\n",
    "\n",
    "\n",
    "mse=mean_squared_error(y_test, predictions)\n",
    "mae=mean_absolute_error(y_test, predictions)\n",
    "rs=model.score(X_test,y_test, sample_weight=None)\n",
    "rmse=math.sqrt(mse)\n",
    "\n",
    "output.append([\"Decision Tree Regressor\",rmse,rs,mse,mae])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "814f3c94",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.figure(figsize=(40,40))\n",
    "plt.plot(t.index, t.values, 'b.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1d0e1af1",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.ensemble import RandomForestRegressor\n",
    "model = RandomForestRegressor(n_estimators=100,max_depth=41,max_features='log2',random_state=1)\n",
    "\n",
    "model.fit(X_train,y_train)\n",
    "predictions = model.predict(X_test)\n",
    "print('Random Forest Regressor\\nmean_squared_error : ', mean_squared_error(y_test, predictions))\n",
    "print('mean_absolute_error : ', mean_absolute_error(y_test, predictions))\n",
    "print(\"R-Squared\",model.score(X_train,y_train, sample_weight=None))\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "plt.figure(figsize=(40,40))\n",
    "plt.plot( y_test, predictions,'b.',alpha=0.05)\n",
    "plt.plot(y_test,y_test,'r-')\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "mse=mean_squared_error(y_test, predictions)\n",
    "mae=mean_absolute_error(y_test, predictions)\n",
    "rs=model.score(X_test,y_test, sample_weight=None)\n",
    "rmse=math.sqrt(mse)\n",
    "\n",
    "output.append([\"Random Forest Regressor\",rmse,rs,mse,mae])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3c334fb9",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.figure(figsize=(40,40))\n",
    "plt.plot(t.index, t.values, 'b.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9233c1a1",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.neural_network import MLPRegressor\n",
    "model=MLPRegressor(hidden_layer_sizes=(20,20,20,1),activation='relu',learning_rate='adaptive', learning_rate_init=0.00001, solver='adam', max_iter=1300,random_state=1)\n",
    "model.fit(X_train,y_train)\n",
    "predictions = model.predict(X_test)\n",
    "print('MLP Regressor\\nmean_squared_error : ', mean_squared_error(y_test, predictions))\n",
    "print('mean_absolute_error : ', mean_absolute_error(y_test, predictions))\n",
    "print(\"R-Squared\",model.score(X_train,y_train, sample_weight=None))\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "plt.figure(figsize=(40,40))\n",
    "plt.plot( y_test, predictions,'b.',alpha=0.05)\n",
    "plt.plot(y_test,y_test,'r-')\n",
    "\n",
    "\n",
    "\n",
    "mse=mean_squared_error(y_test, predictions)\n",
    "mae=mean_absolute_error(y_test, predictions)\n",
    "rs=model.score(X_test,y_test, sample_weight=None)\n",
    "rmse=math.sqrt(mse)\n",
    "\n",
    "output.append([\"MLP Regressor\",rmse,rs,mse,mae])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "450f7052",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.figure(figsize=(40,40))\n",
    "plt.plot(t.index, t.values, 'b.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5e742393",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import BayesianRidge\n",
    "model=BayesianRidge(fit_intercept=True)\n",
    "\n",
    "model.fit(X_train,y_train)\n",
    "predictions = model.predict(X_test)\n",
    "print('Bayesian Ridge Regressor\\nmean_squared_error : ', mean_squared_error(y_test, predictions))\n",
    "print('mean_absolute_error : ', mean_absolute_error(y_test, predictions))\n",
    "print(\"R-Squared\",model.score(X_train,y_train, sample_weight=None))\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "plt.figure(figsize=(40,40))\n",
    "plt.plot( y_test, predictions,'b.',alpha=0.05)\n",
    "plt.plot(y_test,y_test,'r-')\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "mse=mean_squared_error(y_test, predictions)\n",
    "mae=mean_absolute_error(y_test, predictions)\n",
    "rs=model.score(X_test,y_test, sample_weight=None)\n",
    "rmse=math.sqrt(mse)\n",
    "\n",
    "output.append([\"Bayesian Ridge Regressor\",rmse,rs,mse,mae])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "27f83026",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.figure(figsize=(40,40))\n",
    "plt.plot(t.index, t.values, 'b.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "62be25af",
   "metadata": {},
   "outputs": [],
   "source": [
    "from lightgbm import LGBMRegressor\n",
    "model=LGBMRegressor(max_depth=13,random_state=1)\n",
    "\n",
    "model.fit(X_train,y_train)\n",
    "predictions = model.predict(X_test)\n",
    "print('LGBM Regressor\\nmean_squared_error : ', mean_squared_error(y_test, predictions))\n",
    "print('mean_absolute_error : ', mean_absolute_error(y_test, predictions))\n",
    "print(\"R-Squared\",model.score(X_train,y_train, sample_weight=None))\n",
    "t=abs(predictions-y_test)\n",
    "temp=t.values\n",
    "c=0\n",
    "for i in temp:\n",
    "    if (i<10000):\n",
    "        c+=1\n",
    "print(\"\\nAccuracy: \",c/len(temp))\n",
    "import matplotlib.pyplot as plt\n",
    "plt.figure(figsize=(40,40))\n",
    "plt.plot(X_test.index, predictions, 'r.')\n",
    "plt.plot(X_test.index, y_test, 'b.')\n",
    "\n",
    "\n",
    "mse=mean_squared_error(y_test, predictions)\n",
    "mae=mean_absolute_error(y_test, predictions)\n",
    "rs=model.score(X_test,y_test, sample_weight=None)\n",
    "rmse=math.sqrt(mse)\n",
    "\n",
    "output.append([\"LGBM Regressor\",rmse,rs,mse,mae])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "362e3110",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.figure(figsize=(40,40))\n",
    "plt.plot(t.index, t.values, 'b.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e8f14ea2",
   "metadata": {},
   "outputs": [],
   "source": [
    "import xgboost as xg\n",
    "model=xg.XGBRegressor(max_depth=32,random_state=1)\n",
    "\n",
    "model.fit(X_train,y_train)\n",
    "predictions = model.predict(X_test)\n",
    "print('XGB Regressor\\nmean_squared_error : ', mean_squared_error(y_test, predictions))\n",
    "print('mean_absolute_error : ', mean_absolute_error(y_test, predictions))\n",
    "print(\"R-Squared\",model.score(X_train,y_train, sample_weight=None))\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "plt.figure(figsize=(40,40))\n",
    "plt.plot( y_test, predictions,'b.',alpha=0.05)\n",
    "plt.plot(y_test,y_test,'r-')\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "mse=mean_squared_error(y_test, predictions)\n",
    "mae=mean_absolute_error(y_test, predictions)\n",
    "rs=model.score(X_test,y_test, sample_weight=None)\n",
    "rmse=math.sqrt(mse)\n",
    "\n",
    "output.append([\"XGB Regressor\",rmse,rs,mse,mae])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6b04991c",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.figure(figsize=(40,40))\n",
    "plt.plot(t.index, t.values, 'b.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "29b2e6d5",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.ensemble import GradientBoostingRegressor\n",
    "model=GradientBoostingRegressor(max_depth=21,random_state=1)\n",
    "\n",
    "model.fit(X_train,y_train)\n",
    "predictions = model.predict(X_test)\n",
    "print('XGB Regressor\\nmean_squared_error : ', mean_squared_error(y_test, predictions))\n",
    "print('mean_absolute_error : ', mean_absolute_error(y_test, predictions))\n",
    "print(\"R-Squared\",model.score(X_train,y_train, sample_weight=None))\n",
    "\n",
    "import matplotlib.pyplot as plt\n",
    "plt.figure(figsize=(40,40))\n",
    "plt.plot( y_test, predictions,'b.',alpha=0.05)\n",
    "plt.plot(y_test,y_test,'r-')\n",
    "\n",
    "\n",
    "\n",
    "\n",
    "mse=mean_squared_error(y_test, predictions)\n",
    "mae=mean_absolute_error(y_test, predictions)\n",
    "rs=model.score(X_test,y_test, sample_weight=None)\n",
    "rmse=math.sqrt(mse)\n",
    "output.append([\"Gradient Boosting Regressor\",rmse,rs,mse,mae])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "28a22eed",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.figure(figsize=(40,40))\n",
    "plt.plot(t.index, t.values, 'b.')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8a08d70d",
   "metadata": {},
   "outputs": [],
   "source": [
    "#output.pop(4)\n",
    "output"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ad3a97a5",
   "metadata": {},
   "outputs": [],
   "source": []
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
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
