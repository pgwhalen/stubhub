# StubHub

It's just a bunch of scripts that you can run/schedule as desired to save stubhub data.  Obviously you need a mongo instance somehwere (dbname 'stubhub' with collections 'events' and 'listings'), as well as stubhub api credentials, a la `config.py.example`

## Setting up mongodb

From within the mongo shell:
```
> use stubhub
switched to db stubhub
> db.createCollection('events')
{ "ok" : 1 }
> db.createCollection('listings')
{ "ok" : 1 }
```

## Using the code

 - `add_events.py` - reads from STDIN, line-delineated stubhub event ids to add their metadata to the `events` collection in mongo.
 - `record_listings.py` - records all listings in `listings` collection for all events in `events` collections.  this will have to be enhanced so it only tries to record listings for events that haven't happened yet.

Make a virtualenv to run it in, then while inside the env:
```
pip install -r requirements.txt
```
should get everything ready to go, assuming your config.py is properly set up.  `record_listings.py` will likely be a cron job, make sure to load the env for it.
