getParam = function(){
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

module.exports = {
  getParam: getParam
}
