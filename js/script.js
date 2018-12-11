class Service{
  constructor(name,symbol,ip=null){
    this.name = name
    this.symbol = symbol
	this.ip = ip
	this.createElement()
  }
	
  createElement(){
	let e = document.createElement("div");
	e.className = "col-xs-1"
	e.id = this.name;
	let b = document.createElement("button")
	b.className = "btn btn-default"
	b.type = "button"
	b.innerHTML = this.symbol
	e.appendChild(b)
	/*
    let rep = "<div class=\"col-xs-1\" id=\"" + this.name + "\" >"+
            "<button type=\"button\" class=\"btn btn-default\">" + this.symbol + "</button>"+
          "</div>"
    return rep
	*/
	this.element = e
	this.button = b
	return e
  }
  
  addService(){
    document.getElementById('microservices').appendChild(this.element)
  }
  
  useService(){
  }
}

function addServices(){
  for(let s of services){
    console.log(s)
    s.addService()
  }
}
var services = {
	plusService : new Service("plus","+"),
	minusService : new Service("minus","-"),
	multService : new Service("mult","*"),
	divService : new Service("div","/")
}
document.addEventListener("DOMContentLoaded",()=>{
	for(let s in services){services[s].addService()}
})
