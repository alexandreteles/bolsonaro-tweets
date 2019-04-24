import twint
import time

# setup query variables

timestamp = ''.join(['-', str(time.time()).replace('.', '')])
username = 'flaviobolsonaro'  # please check ./data/twitter_handles.txt
since = '2018-11-7'
output = ''.join(['./data/', username, timestamp, '.csv'])

# setup twint env

query = twint.Config()
query.Username = username
query.Since = since
query.Output = output
query.Store_csv = True
query.User_full = True

# start tweet scrapping

twint.run.Search(query)
