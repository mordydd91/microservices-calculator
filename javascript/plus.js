let get = require("./getParam.js")
var plus = function(a,b){
    return a+b
}

var service = function() {
  try{
    let x = get.getParam()
    return plus(x.a,x.b)
  }
  catch(err){
    return err.toString();
  }
}

if (require.main === module) {
  console.log(service())
}
