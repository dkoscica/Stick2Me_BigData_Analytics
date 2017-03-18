/**
String extension method
**/
String.prototype.replaceAll = function(search, replacement) {
    var target = this;
    return target.replace(new RegExp(search, 'g'), replacement);
};

/**
 * Splits tweets from the tweets.all collection by months and weeks
 * @param firstDayOfTheMonth 
 * @param lastDayOfTheMonth
 * @param month
 * @param year
 * @param interval, for a week interval use 7 as the interval value
 */
function splitByInterval(firstDayOfTheMonth, lastDayOfTheMonth, month, year, interval) {

    for (var day = firstDayOfTheMonth; day <= lastDayOfTheMonth; day += interval) {

        var calculatedEndDay = day + interval
        if(calculatedEndDay > lastDayOfTheMonth) {
          calculatedEndDay = lastDayOfTheMonth
        }
        
        var startDay = ("0" + day).slice(-2)
        var endDay = ("0" + calculatedEndDay).slice(-2)
        var month = ("0" + (month)).slice(-2)

        var startDate = year + "-" + month + "-" + startDay
        var endDate = year + "-" + month + "-" + endDay

        db.tweets.all.aggregate([{
            $match: {
                "created_at": {
                    $gte: ISODate(startDate + "00:00:00.000Z"),
                    $lt: ISODate(endDate + "00:00:00.000Z")
                }
            },
        }, {
            $out: "tweets.From_" + startDate.replaceAll("-", "_") + "_To_" + endDate.replaceAll("-", "_")
        }])
    }
}

/**
Split all tweets from the tweets.all collection to smaller collections
**/
splitByInterval(23, 31, 12, 2016, 7);
splitByInterval(1, 31, 1, 2017, 7);
splitByInterval(1, 28, 2, 2017, 7);

//show collections

var collectionNames = db.getCollectionNames()

for (var index = 0; index < collectionNames.length; index++) {
    var collectionName = collectionNames[index]
    print("Collection " + collectionName)
    print("DocumentCount: " + db.getCollection(collectionName).count())
}

//db.tweets.From_2017_01_01_To_2017_01_08