db.getCollection('tweets.From_2016_12_23_To_2016_12_30').find({})


db.getCollection('tweets.From_2016_12_23_To_2016_12_30').find({}, {_id: 0, vertex1: 1, vertex2: 1})