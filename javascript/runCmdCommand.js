const util = require("util");
const path = require('path')
const fs = require("fs")
const exec = util.promisify(require('child_process').exec);

let js = "node"
let folders = ["" , "bin" , "python" , "javascript"]
var execute_microservice = async function (a,b, microName){
    let microPath = find(microName);
    if(!microPath){return "could'nt find " + microName}
    if(a == null){a=""}
    if(b == null){b=""}
    let command = js + " " + '"' + microPath + '"' + " " + a + " " + b
    return run_command(command)
}
var find = function(microName){
    if(!(microName.includes(".js"))){microName+=".js"}
    let microPath = ""
    for (let folder of folders){
        microPath = folder + ((folder !="") ? "\\" : "") + microName
        if(fs.existsSync(microPath)){
            return microPath
        }
    }
    return null
}

var run_command = async function (command) {
  const { stdout, stderr } = await exec(command);
  console.log(stdout);
  return stdout
}

module.exports = {
    execute_microservice: execute_microservice
}

execute_microservice(5, 3, "minus.js")
