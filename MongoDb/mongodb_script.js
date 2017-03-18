/**
String extension method
**/
String.prototype.replaceAll = function(search, replacement) {
    var target = this;
    return target.replace(new RegExp(search, 'g'), replacement);
};


function splitByMonth(firstDay, lastDay, month) {

    for (var day = startDay; day < endDay; day += 7) {

        var startDay = ("0" + day).slice(-2);
        var endDay = ("0" + (day + 7)).slice(-2);
        var month = ("0" + (month)).slice(-2);

        var startDate = "2017-" + month + "-" + startDay;
        var endDate = "2017-" + month + "-" + endDay;

        db.tweets.all.aggregate([{
            $match: {
                "created_at": {
                    $gte: ISODate(startDate + "00:00:00.000Z"),
                    $lt: ISODate(endDate + "00:00:00.000Z")
                }
            }
        }, {
            $out: "tweets.From_" + startDate.replaceAll("-", "_") + "_To_" + endDate.replaceAll("-", "_")
        }]);
    }
}

splitByMonth(1, 31, 1);

splitByMonth(1, 28, 2);
show collections

var collectionNames = db.getCollectionNames()

for (var index = 0; index < collectionNames.length; index++) {
    var collectionName = collectionNames[index]
    print("#Collection " + collectionName + "#")
    print("DocumentCount: " + db.getCollection(collectionName).count())
}

db.tweets.From_2017_01_01_To_2017_01_08