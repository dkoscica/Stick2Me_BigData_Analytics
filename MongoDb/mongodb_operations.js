function totalNumberOfTweets() {
    return db.tweets.all.count()
}

function sortedUsersWithMostStick2MeTweets() {
 return db.tweets.all.aggregate(
    {$group : { _id : '$user_name', count : {$sum : 1}}},
    {$sort : { count : -1}})
}

function tweetsPerUserByInterval(startDate, endDate){ 
   return db.tweets.all.aggregate(
          {$match : { "created_at": { $gte: ISODate(startDate), $lt: ISODate(endDate)}}},
          {$group : { _id : '$user_name', count : {$sum : 1}}},
          {$sort  : { count : -1}})
}

function tweetsPerWeek(startDate, endDate){ 
   var numberOfTweets = db.tweets.all.find({"created_at": { $gte: ISODate(startDate), $lt: ISODate(endDate)}}).count()
   print("Tweets count: " + numberOfTweets +" (" + startDate + " - " + endDate + ")") 
}

totalNumberOfTweets()
//sortedUsersWithMostStick2MeTweets()

//Most active Stick2Me twitters during a weeks period and sorted by descending order
tweetsPerUserByInterval("2016-12-20", "2017-02-28")

/*
tweetsPerUserByInterval("2017-01-07", "2017-01-14");
tweetsPerUserByInterval("2017-01-14", "2017-01-21");
tweetsPerUserByInterval("2017-01-21", "2017-01-28");
tweetsPerUserByInterval("2017-01-28", "2017-01-31");

//Number of Stick2Me tweets per week
tweetsPerWeek("2017-01-01", "2017-01-07")
tweetsPerWeek("2017-01-07", "2017-01-14");
tweetsPerWeek("2017-01-14", "2017-01-21");
tweetsPerWeek("2017-01-21", "2017-01-28");
tweetsPerWeek("2017-01-28", "2017-01-31");
*/