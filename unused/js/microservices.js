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
	this.element = e
	this.button = b
	return e
  }
  
  addService(e){
    e.appendChild(this.element)
  }
  
  useService(){
  }
}

var services = {
	plusService : new Service("plus","+"),
	minusService : new Service("minus","-"),
	multService : new Service("mult","*"),
	divService : new Service("div","/")
}
document.addEventListener("DOMContentLoaded",()=>{
	let e = document.getElementById('microservices')
	for(let s in services){services[s].addService(e)}
})
