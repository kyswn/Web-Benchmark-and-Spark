val lines = sc.textFile("twitter.edges")
val split = lines.map(line=>line.split(": "))
val followed = split.flatMap(arr=>{
	val list = arr(1)
	val followings = list.split(",")
	followings.map(folloing=>(folloing,1))
})
val followerCount = followed.reduceByKey((a,b)=>(a+b))
//followerCount.saveAsTextFile("temp")
val topUsers = followerCount.filter{case(a,b)=>b>1000}
topUsers.saveAsTextFile("output")

System.exit(0)
