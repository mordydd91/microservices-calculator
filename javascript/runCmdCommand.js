const util = require("util");
const fs = require("fs")
const exec = util.promisify(require('child_process').exec);

let js = "node"
let folders = ["" , "bin" , "python" , "javascript"]
var execute_microservice = function (a,b, microName){
    let microPath = find(microName);
    if(!microPath){return "could'nt find " + microName}
    if(a == null){a=""}
    if(b == null){b=""}
    let command = js + " " + '"' + microPath + '"' + " " + str(a) + " " + str(b)
    return run_command(command)
}
var find = function(microName){
    if(!(".js" in microName)){microName+=".js"}
    let microPath = ""
    for (folder of folders){
        microPath = folder+"\\"+microName
        if(Path(microPath).is_file()){
            return microPath
        }
    }
    let x = __dirname
    for (folder of folders){
        microPath = x+"\\" + folder + ((folder !="") ? "\\" : "") +microName
        if(Path(microPath).is_file()){
            return microPath
        }
    }
    return None
}

var run_command = async function (command) {
  const { stdout, stderr } = await exec(command);
  return stdout
}
