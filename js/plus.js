var getParam = function(){
    let argCount = process.argv.length - 2
    if(argCount<2)
      throw new Error("not enough args, argCount=" + argCount + "<2")
    try{
      let a = parseFloat(process.argv[2])
      let b = parseFloat(process.argv[3])
      return {a : a, b : b}
    }
    catch(err){
      throw new Error("NaN")
    }
}

var plus = function(a,b){
    return a+b
}

var service = function() {
  try{
    let x = getParam()
    return plus(x.a,x.b)
  }
  catch(err){
    return err.toString();
  }
}

if (require.main === module) {
  console.log(service())
}
