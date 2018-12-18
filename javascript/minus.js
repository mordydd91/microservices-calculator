let get = require("./getParam.js")
var minus = function(a,b){
    return a-b
}

var service = function() {
  try{
    let x = get.getParam()
    return minus(x.a,x.b)
  }
  catch(err){
    return err.toString();
  }
}

if (require.main === module) {
  console.log(service())
}
